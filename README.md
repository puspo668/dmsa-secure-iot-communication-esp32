# DMSA-Based Secure IoT Communication System Using ESP32 and DHT11 Sensor

## Overview

This project demonstrates a secure IoT communication system using ESP32 and DHT11 sensor with DMSA-based communication techniques. The system is designed to monitor temperature and humidity data and securely transmit the information between devices using wireless communication.

The project combines IoT hardware, sensor monitoring, and secure data communication using ESP32 microcontroller and Python-based sender-receiver applications.

---

## Features

* Real-time temperature monitoring
* Real-time humidity monitoring
* Secure communication system
* ESP32 WiFi-based data transmission
* Python sender and receiver applications
* IoT device integration
* Sensor data processing



## Technologies Used

* ESP32
* DHT11 Sensor
* Arduino IDE
* Python
* C++
* IoT Communication
* Wireless Networking

---


## Project Structure

```bash
├── sketch_may20a.ino
├── sender_app.py
├── receiver_app.py
```



## Files Description

### `sketch_may20a.ino`

Arduino code for ESP32 that reads temperature and humidity data from the DHT11 sensor and handles communication.

### `sender_app.py`

Python sender application used for transmitting data securely.

### `receiver_app.py`

Python receiver application used for receiving and processing transmitted data.

---

## Hardware Components

### ESP32 Microcontroller

ESP32 is a low-power and high-performance microcontroller used as the main processing unit of the proposed system. It is responsible for collecting real-time sensor data from the DHT11 sensor and transmitting the data to the sender application through serial communication. ESP32 provides built-in Wi-Fi and efficient processing capability suitable for IoT-based secure communication systems.

### DHT11 Temperature and Humidity Sensor

The DHT11 sensor is used to measure real-time temperature and humidity values from the surrounding environment. The sensor transmits digital data to the ESP32 microcontroller through a single data pin. The collected sensor information is later encrypted using the proposed DMSA algorithm before transmission.

### Breadboard

A breadboard is used to create temporary hardware connections between ESP32 and DHT11 without soldering. It helps organize circuit connections and simplifies hardware testing and prototyping during the implementation process.

### Jumper Wires

Jumper wires are used to establish electrical connections between ESP32, DHT11 sensor, and the breadboard. Male-to-male jumper wires were used for stable circuit communication.

### Hardware Connections

The DHT11 sensor was connected to the ESP32 microcontroller using the following pin configuration:

| Component  | ESP32 Pin Connection |
| ---------- | -------------------- |
| DHT11 VCC  | 3.3V                 |
| DHT11 GND  | GND                  |
| DHT11 DATA | GPIO 4               |

The ESP32 was connected to the computer using a USB cable for power supply and serial communication with the sender application.


## Applications

* Smart Home Monitoring
* Secure IoT Systems
* Environmental Monitoring
* Wireless Sensor Networks
* Research & Educational Projects

---

## Future Improvements

* Cloud integration
* Mobile application support
* Advanced encryption algorithms
* Real-time dashboard visualization
* Database integration

---

## Team Members

1. KUMARI PUSPO RANI
2. MD YOUNUS
3. Tayeb Hassan
4. Redwanul Islam Rabbi

---

## Author

Developed as an IoT and Secure Communication System project for academic and research purposes.
