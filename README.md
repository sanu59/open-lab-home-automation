# Open Lab – Voice-Controlled Home Automation ⚡🏠

A full-stack **smart home automation** system that lets you control lights and fans using **voice commands** from a web dashboard.  
The project combines:

- 🎛️ A **React** frontend with voice recognition  
- 🌐 A **Node.js + Express + Socket.IO** backend  
- 🐍 **Python** firmware on a **Raspberry Pi 4**  
- 🔌 Real **hardware**: relay modules, DC fans, LED strips, and a 3D cardboard house prototype  

---

## 📸 Demo Gallery

### 1. Hardware Setup

This is the complete hardware setup with Raspberry Pi 4, relay module, DC fans, LED strips and a 12V SMPS powering the loads.

![Hardware Setup](./screenshots/Hardware%20Setup.jpg)

---

### 2. Prototype House Model

A scaled cardboard house used to simulate **Living Room** and **Bedroom**.  
Each room has independent lighting and fan control via voice and web commands.

![Prototype Model](./screenshots/Prototype%20Model.jpg)

---

### 3. Circuit Schematic

GPIO pin mapping from Raspberry Pi 4 to the cooling fans and LEDs.  
The relays isolate the Pi from higher-current loads.

![Circuit Schematic](./screenshots/Circuit%20Schematic.jpg)

---

### 4. Web Dashboard Interface

Minimal React UI for controlling and monitoring devices.  
Voice recognition is integrated into the browser, and device state syncs in real time.

![Web Dashboard Interface](./screenshots/Web%20Dashboard%20Interface.jpg)

---

## 🔍 Project Overview

**Open Lab** is a voice-enabled home automation prototype that demonstrates:

- Real-time control of home appliances from a browser
- Voice commands for turning lights and fans ON/OFF
- Communication between frontend, backend and Raspberry Pi over sockets
- Integration of software + hardware + networking in a single project

It is designed as a **portfolio-ready IoT project** that shows skills in:

- Full-stack web development  
- Embedded systems / hardware interfacing  
- Real-time communication  
- System design & prototyping  

---

## 🧱 System Architecture

**1. Frontend (React)**  
- Displays device status for **Living Room** and **Bedroom**  
- Uses browser speech recognition to capture commands  
- Sends actions to backend via **Socket.IO**  
- Updates UI in real time based on responses

**2. Backend (Node.js + Express + Socket.IO)**  
- Listens for events like `toggleDevice` from the frontend  
- Maintains global device state (`light1`, `fan1`, `light2`, `fan2`, etc.)  
- Forwards commands to the Raspberry Pi (or corresponding hardware process)

**3. Raspberry Pi Firmware (Python)**  
- Listens for incoming control messages  
- Drives GPIO pins that control:  
  - Relay module → DC fans and LED strips  
- Uses the wiring shown in the circuit schematic

---

## 🧰 Tech Stack

| Layer        | Technologies                            |
|-------------|------------------------------------------|
| Frontend    | React, JavaScript, Web Speech API        |
| Backend     | Node.js, Express.js, Socket.IO           |
| Firmware    | Python 3, RPi.GPIO / spidev              |
| Hardware    | Raspberry Pi 4, Relay Module, DC Fans, LED Strips |
| Tools       | Git, npm, VS Code                        |

---

## 📂 Folder Structure

```text
open-lab-home-automation
├── App/
│   ├── App1.js                     # Simple React+Socket IO demo app
│   ├── backend/                    # Node.js backend
│   │   ├── package.json
│   │   └── server.js
│   └── home-automation/            # Main React app (Create React App)
│       ├── package.json
│       ├── public/
│       └── src/
├── HOME_AUTOMATION.pdsprj/         # PCB / hardware project files
│   ├── FIRMWARE/                   # Raspberry Pi firmware and helpers
│   └── (schematics, board files…)
├── screenshots/                    # Project images used in the README
│   ├── Hardware Setup.jpg
│   ├── Prototype Model.jpg
│   ├── Circuit Schematic.jpg
│   └── Web Dashboard Interface.jpg
└── README.md
