# 💊 Medipal
Disclaimer: The code organisation might be a little messy for this repository :P Sorry about that.

## 📟 1. Sensors and Hardware Integration:
Micro:bits (4 units): Utilized for collecting and transmitting data wirelessly via sensors (temperature, accelerometer, radio, touch).
Central Hub: Processes data from other Micro:bits and forwards it to ThingSpeak or a webpage for visualization.
Laptop: Facilitates serial communication via USB, processes data in real-time, and interfaces with the system.

## 💻 2. Software Components:
MakeCode: Handles wireless communication between Micro:bits.
Python Script (received_string.py): Processes data from Micro:bits, checks data integrity, and updates webpages or ThingSpeak.

## 🌐 3. Networking:
AWS Server: Hosts HTML resources (index, how-it-works, FAQ pages) accessible via public IP.
Local Server: Hosts a real-time data page accessible through a private IP within the local network.

## 🔗 4. Communication Protocols:
HTTP: Facilitates data exchange between client browsers and servers.
Serial Communication: Ensures reliable data transfer between Micro:bits and laptops using a consistent baud rate (115200).
Radio Communication: Short-range wireless transmission between Micro:bits in the same radio group (213).

## 🔧 5. Functional Modules:
Pill Counter: Tracks pills in the medicine box using accelerometer data.
Temperature Monitoring: Measures and transmits environmental temperature every 5 seconds.
Box Locator: Plays sound on the box Micro:bit based on signal strength from the wristband Micro:bit.

## 👤 6. User Features:
Login Function: Secures data access with Firebase Firestore storing user details.
Wi-Fi Status Detection: Visual indicator for connectivity loss.
Data Visualization: Displays real-time and historical data using HTML pages and ThingSpeak.
