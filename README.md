# 🔐 DMSA-Based Secure IoT Communication System Using ESP32 and DHT11 Sensor

##  Project Overview

This project presents a lightweight secure IoT communication system using ESP32, DHT11 sensor, Python Flask, and a custom Dynamic Matrix Shift Algorithm (DMSA). The system collects real-time temperature and humidity data from the environment and securely transmits the data between sender and receiver applications through encryption and decryption operations.

The proposed DMSA algorithm applies multiple lightweight matrix-based transformations including ASCII conversion, binary transformation, row shifting, column swapping, and binary rotation to generate encrypted cipher text for secure communication.



#  Features

* Real-time Temperature and Humidity Monitoring
* ESP32 and DHT11 Sensor Integration
* Lightweight Custom DMSA Encryption Algorithm
* Sender and Receiver Web Applications
* Real-Time Secure Data Transmission
* Encryption and Decryption Visualization
* Matrix-Based Secure Communication
* Flask-Based Web Interface



# Technologies Used

* ESP32 Microcontroller
* DHT11 Temperature and Humidity Sensor
* Python
* Flask Framework
* Arduino IDE
* PySerial
* Requests Library
* HTML/CSS
* VS Code



#  Hardware Components

| Component    | Description                                          |
| ------------ | ---------------------------------------------------- |
| ESP32        | Main microcontroller used for sensor data collection |
| DHT11 Sensor | Measures temperature and humidity                    |
| Breadboard   | Used for temporary hardware connections              |
| Jumper Wires | Used for circuit connections                         |
| USB Cable    | Used for power supply and serial communication       |



#  Hardware Connections

| DHT11 Pin | ESP32 Connection |
| --------- | ---------------- |
| VCC       | 3.3V             |
| GND       | GND              |
| DATA      | GPIO 4           |



#  DMSA Encryption Workflow

The proposed Dynamic Matrix Shift Algorithm (DMSA) performs the following operations:

1. Real-time sensor data collection
2. ASCII conversion
3. Binary transformation
4. Matrix generation
5. Row shifting using secret key
6. Column swapping
7. Binary rotation
8. Cipher text generation
9. Secure transmission to receiver
10. Reverse decryption process


#  System Architecture

ESP32 → Sender Application → DMSA Encryption → Receiver Application → DMSA Decryption → Original Sensor Data


#  Sender Application

The sender application receives real-time sensor data from ESP32 through serial communication. The collected data is encrypted using the proposed DMSA algorithm and transmitted to the receiver application using HTTP requests.


#  Receiver Application

The receiver application receives encrypted cipher text from the sender application and performs reverse DMSA operations to reconstruct the original temperature and humidity data.


#  Project Output

The system successfully demonstrates:

* Real-time sensor monitoring
* Lightweight secure communication
* Encryption and decryption workflow visualization
* Secure IoT data transmission


#  How to Run the Project

## Step 1: Upload Arduino Code

* Open Arduino IDE
* Connect ESP32
* Upload the DHT11 sensor code

## Step 2: Install Python Libraries


pip install flask pyserial requests


## Step 3: Run Receiver Application


python app.py


Receiver runs at:


http://127.0.0.1:5001


## Step 4: Run Sender Application


python app.py


Sender runs at:


http://127.0.0.1:5000




#  Project Screenshots

* ESP32 Hardware Setup
* Arduino Serial Monitor Output
* Sender Application Interface
* Receiver Application Interface
* DMSA Encryption Workflow
* Cipher Text Output



#  Research Contribution

This project introduces a lightweight matrix-based secure communication framework suitable for IoT environments and low-power embedded systems. The proposed DMSA algorithm provides secure real-time sensor communication with low computational complexity.



#  Future Improvements

* Cloud Integration
* Dynamic Key Generation
* Database Storage
* Advanced Cryptographic Techniques
* Mobile Application Integration
* Wireless Secure Communication



#  Authors

KUMARI PUSPO RANI
MD YOUNUS
Tayeb Hassan
Redwanul Islam Rabbi

Department of Computer Science and Engineering
Jamalpur Science and Technology University, Bangladesh


#  License

This project is developed for educational and research purposes.
