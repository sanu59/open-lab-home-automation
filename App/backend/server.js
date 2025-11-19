const express = require("express");
const http = require("http");
const socketIo = require("socket.io");
const { exec } = require("child_process");

const app = express();
const server = http.createServer(app);
const io = socketIo(server, { cors: { origin: "*" } });

app.use(express.json());

const PORT = 5000;

// Store actual device states
let deviceStatus = {
  light1: false,
  fan1: false,
  light2: false,
  fan2: false,
};

// Handle socket connections
io.on("connection", (socket) => {
  console.log("Client connected");
  socket.onAny((event, ...args) => {
  console.log(`Received event: ${event}`, args);
  });
socket.on("test_event", (data) => {
  console.log("Received test_event:", data);
});

  // Send current device status to the client on connect
  socket.emit("statusUpdate", deviceStatus);

  // Receive command from frontend
  socket.on("toggle", ({ device, state }) => {
    console.log(`Received command: ${device} -> ${state}`);

    // Run a Python script to control Raspberry Pi devices
    exec(`python3 ledblink.py ${device} ${state}`, (error, stdout) => {
      if (error) {
        console.error(`Error executing command: ${error.message}`);
        return;
      }

      console.log(stdout);

      // Update device status only when the command succeeds
      deviceStatus[device] = state;

      // Send updated status to all clients
      io.emit("statusUpdate", deviceStatus);
    });
  });

  socket.on("disconnect", () => {
    console.log("Client disconnected");
  });
});

// Start server
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
