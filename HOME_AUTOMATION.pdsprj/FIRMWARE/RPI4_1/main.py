import spidev
import time
import RPi.GPIO as GPIO
import pio
import Ports

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pio.uart = Ports.UART()  # Define serial port

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E = 11
LCD_D4 = 12
LCD_D5 = 13
LCD_D6 = 15
LCD_D7 = 16
bulb_pin = 32
motor_pin = 18
pir_pin = 31
ldr_channel = 0
temp_channel = 1

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT)  # RS
GPIO.setup(LCD_D4, GPIO.OUT)  # DB4
GPIO.setup(LCD_D5, GPIO.OUT)  # DB5
GPIO.setup(LCD_D6, GPIO.OUT)  # DB6
GPIO.setup(LCD_D7, GPIO.OUT)  # DB7
GPIO.setup(bulb_pin, GPIO.OUT)
GPIO.setup(motor_pin, GPIO.OUT)
GPIO.setup(pir_pin, GPIO.IN)

# Define some device constants
LCD_WIDTH = 16  # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line


def lcd_init():
    # Initialise display
    lcd_byte(0x33, LCD_CMD)  # 110011 Initialise
    lcd_byte(0x32, LCD_CMD)  # 110010 Initialise
    lcd_byte(0x06, LCD_CMD)  # 000110 Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # 001100 Display On, Cursor Off, Blink Off
    lcd_byte(0x28, LCD_CMD)  # 101000 Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # 000001 Clear display
    time.sleep(E_DELAY)


def lcd_byte(bits, mode):
    GPIO.output(LCD_RS, mode)  # RS

    # High bits
    GPIO.output(LCD_D4, bits & 0x10 == 0x10)
    GPIO.output(LCD_D5, bits & 0x20 == 0x20)
    GPIO.output(LCD_D6, bits & 0x40 == 0x40)
    GPIO.output(LCD_D7, bits & 0x80 == 0x80)

    lcd_toggle_enable()

    # Low bits
    GPIO.output(LCD_D4, bits & 0x01 == 0x01)
    GPIO.output(LCD_D5, bits & 0x02 == 0x02)
    GPIO.output(LCD_D6, bits & 0x04 == 0x04)
    GPIO.output(LCD_D7, bits & 0x08 == 0x08)

    lcd_toggle_enable()


def lcd_toggle_enable():
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)


def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for char in message:
        lcd_byte(ord(char), LCD_CHR)


def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


def ConvertTemp(data, places):
    temp = ((data * 330) / float(1023))
    return round(temp, places)


lcd_init()
lcd_string("Welcome", LCD_LINE_1)
time.sleep(1)

while True:
    pir_data = GPIO.input(pir_pin)

    if pir_data:
        light_level = ReadChannel(ldr_channel)
        time.sleep(0.2)

        lcd_byte(0x01, LCD_CMD)  # Clear display
        lcd_string("Person Detected", LCD_LINE_1)
        time.sleep(1)

        lcd_byte(0x01, LCD_CMD)
        lcd_string("Light Intensity", LCD_LINE_1)
        lcd_string(str(light_level), LCD_LINE_2)
        time.sleep(0.5)

        if light_level < 100:
            lcd_byte(0x01, LCD_CMD)
            lcd_string("Bulb ON", LCD_LINE_1)
            GPIO.output(bulb_pin, True)
            time.sleep(0.5)
        else:
            lcd_byte(0x01, LCD_CMD)
            lcd_string("Bulb OFF", LCD_LINE_1)
            GPIO.output(bulb_pin, False)
            time.sleep(0.5)

        temp_level = ReadChannel(temp_channel)
        temperature = ConvertTemp(temp_level, 2)

        lcd_byte(0x01, LCD_CMD)
        lcd_string("Temperature", LCD_LINE_1)
        lcd_string(f"{temperature}C", LCD_LINE_2)
        time.sleep(1)

        if temperature > 30:
            lcd_byte(0x01, LCD_CMD)
            lcd_string("Fan ON", LCD_LINE_1)
            GPIO.output(motor_pin, True)
            time.sleep(0.5)
        else:
            lcd_byte(0x01, LCD_CMD)
            lcd_string("Fan OFF", LCD_LINE_1)
            GPIO.output(motor_pin, False)
            time.sleep(0.5)
    else:
        lcd_byte(0x01, LCD_CMD)
        lcd_string("No Person Detected", LCD_LINE_1)
        GPIO.output(bulb_pin, False)
        GPIO.output(motor_pin, False)

    time.sleep(0.5)
