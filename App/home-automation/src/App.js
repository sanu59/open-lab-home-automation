import React, { useState, useEffect } from "react";
import SpeechRecognition, { useSpeechRecognition } from "react-speech-recognition";
import io from "socket.io-client";

const socket = io("http://172.20.10.3:5001"); // Replace with Raspberry Pi's IP

function App() {
  const [devices, setDevices] = useState({
    light1: false,
    fan1: false,
    light2: false,
    fan2: false,
  });

  const { transcript, listening, resetTranscript } = useSpeechRecognition();

  useEffect(() => {
    if (!SpeechRecognition.browserSupportsSpeechRecognition()) {
      alert("Your browser does not support voice recognition.");
      return;
    }

    SpeechRecognition.startListening({ continuous: true });
    console.log("Listening started...");
  }, []);

  useEffect(() => {
    console.log("Transcript:", transcript);
    
    if (!transcript) return;
    
    const command = transcript.toLowerCase();

    if (command.includes("living room light on")) {
      sendCommand("light1", true);
    } else if (command.includes("living room light of")) {
      sendCommand("light1", false);
    } else if (command.includes("living room fan on")) {
      sendCommand("fan1", true);
    } else if (command.includes("living room fan of")) {
      sendCommand("fan1", false);
    } else if (command.includes("bedroom light on")) {
      sendCommand("light2", true);
    } else if (command.includes("bedroom light of")) {
      sendCommand("light2", false);
    } else if (command.includes("bedroom fan on")) {
      sendCommand("fan2", true);
    } else if (command.includes("bedroom fan of")) {
      sendCommand("fan2", false);
    }

    setTimeout(() => {
      SpeechRecognition.stopListening();
      console.log("Listening stopped due to inactivity");
      resetTranscript();
    }, 3000); 
  }, [transcript]);

  useEffect(() => {
    socket.on("statusUpdate", (status) => {
      setDevices(status);
    });
    return () => socket.off("statusUpdate");
  }, []);

  const sendCommand = (device, state) => {
    console.log(`Sending command: ${device} -> ${state}`);
    socket.emit("toggle", { device, state });
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1> Home Automation Control</h1>
      <button 
        onClick={() => SpeechRecognition.startListening({ continuous: true })}
        style={{ marginRight: "10px", padding: "10px", backgroundColor: "green", color: "white", borderRadius: "5px" }}
      >
         Start Voice Control
      </button>
      <button 
        onClick={SpeechRecognition.stopListening}
        style={{ padding: "10px", backgroundColor: "red", color: "white", borderRadius: "5px" }}
      >
         Stop Voice Control
      </button>

      <div style={{ marginTop: "20px", fontSize: "18px", fontWeight: "bold" }}>
        Voice Command: <span style={{ color: listening ? "blue" : "black", marginLeft: "10px" }}>
          {transcript || "Waiting for command..."}
        </span>
      </div>

      <div style={{ marginTop: "20px" }}>
        <h2>Living Room</h2>
        <p>Light: {devices.light1 ? "ON" : "OFF"}</p>
        <p>Fan: {devices.fan1 ? "ON" : "OFF"}</p>
      </div>

      <div style={{ marginTop: "20px" }}>
        <h2>Bedroom</h2>
        <p>Light: {devices.light2 ? "ON" : "OFF"}</p>
        <p>Fan: {devices.fan2 ? "ON" : "OFF"}</p>
      </div>
    </div>
  );
}

export default App;
