# Open Lab – Voice-Controlled Home Automation ⚡🏠

A full-stack **smart home automation** system that lets you control lights and fans using **voice commands** from a web dashboard.  
The project combines:

- 🎛️ A **React** frontend with voice recognition  
- 🌐 A **Node.js + Express + Socket.IO** backend  
- 🐍 **Python** firmware on a **Raspberry Pi 4**  
- 🔌 Real **hardware**: relay modules, DC fans, LED strips, and a cardboard house prototype  

---

## 📸 Demo Gallery

### 🔌 1. Hardware Setup

Complete hardware setup with Raspberry Pi 4, relay module, DC fans, LED strips and 12V SMPS powering the loads.

![Hardware Setup](./screenshots/hardware-setup.jpg)

---

### 🏠 2. Prototype House Model

A scaled cardboard house simulating **Living Room** and **Bedroom**.  
Each room has independent lighting and fan control via voice and web commands.

![Prototype Model](./screenshots/prototype-model.jpg)

---

### 📊 3. Circuit Schematic

GPIO pin mapping from Raspberry Pi 4 to fans and LEDs.  
Relays are used to safely switch higher-current loads from low-voltage GPIO pins.

![Circuit Schematic](./screenshots/circuit-schematic.jpg)

---

### 💻 4. Web Dashboard Interface

Minimal React UI for controlling and monitoring devices.  
Voice recognition runs in the browser, and device state syncs in real time.

![Web Dashboard Interface](./screenshots/web-dashboard-interface.jpg)

---

## 🔍 Project Overview

**Open Lab** is a voice-enabled home automation prototype that demonstrates:

- Real-time control of home appliances from a browser  
- Voice commands for turning lights and fans ON/OFF  
- Communication between frontend, backend and Raspberry Pi over sockets  
- Integration of **software + hardware + networking** in a single project  

It is designed as a **portfolio-ready IoT project** showing skills in:

- Full-stack web development  
- Embedded systems / hardware interfacing  
- Real-time communication  
- System design & prototyping  

---

## 🧱 System Architecture

**1. Frontend (React)**  
- Displays device status for **Living Room** and **Bedroom**  
- Uses Web Speech API for speech-to-text  
- Sends actions to backend using **Socket.IO**  
- Updates UI in real-time based on backend events

**2. Backend (Node.js + Express + Socket.IO)**  
- Exposes WebSocket endpoint for the frontend  
- Maintains global device state (`light1`, `fan1`, `light2`, `fan2`, etc.)  
- Forwards commands to Raspberry Pi (or hardware process)  
- Broadcasts status updates back to all connected clients

**3. Raspberry Pi Firmware (Python)**  
- Listens for incoming control messages  
- Drives GPIO pins connected to relay module  
- Relays switch power to DC fans and LED strips according to the schematic  

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
│   ├── App1.js                     # Simple React+Socket.IO demo app
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
│   ├── hardware-setup.jpg
│   ├── prototype-model.jpg
│   ├── circuit-schematic.jpg
│   └── web-dashboard-interface.jpg
└── README.md
