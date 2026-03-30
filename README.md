# Prodigy_CS_05
# 🌐 Network Packet Analyzer

A **Python-based Network Packet Analyzer** built using **Scapy** that captures and analyzes network traffic in real-time. This tool helps in understanding how data flows across a network by displaying packet-level details.

---

## 📌 Project Description

This project captures live network packets from a specified interface and extracts useful information such as:

* Source and Destination IP addresses
* Protocol type (TCP, UDP, ICMP)
* HTTP request details (if available)
* Packet payload data

It is designed for **educational purposes** to learn about networking and packet inspection.

---

## 🚀 Features

* 📡 Live packet capture from network interface
* 🔍 Displays IP address and protocol information
* 🌍 Detects and prints HTTP request details
* 📦 Shows packet payload (limited preview)
* 🔢 Packet counter for tracking captured packets
* ⚠️ Error handling and logging support

---

## 🛠️ Technologies Used

* Python 3
* Scapy Library
* Built-in modules:

  * `argparse`
  * `sys`
  * `logging`

---

## ⚙️ Requirements

Make sure you have the following installed:

```bash id="yq2p8a"
pip install scapy
```

> ⚠️ Run the program as **Administrator** for proper packet capturing.

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash id="xj3n8f"
git clone https://github.com/your-username/network-packet-analyzer.git
```

### Step 2: Navigate to Project Folder

```bash id="3t9n2p"
cd network-packet-analyzer
```

### Step 3: Run the Script

```bash id="8h2k1q"
python Task\ 5.py -i Wi-Fi -c 10
```

---

## 🧪 Example Command

```bash id="b7k3f2"
python Task\ 5.py -i Wi-Fi -c 5
```

* `-i` → Network interface (e.g., Wi-Fi, Ethernet)
* `-c` → Number of packets to capture (0 = unlimited)

---

## 🖥️ Sample Output

```id="p2m9k4"
--------------------------------------------------------------------------------
NETWORK PACKET ANALYZER
--------------------------------------------------------------------------------
WARNING: This tool is for educational purposes only.
Unauthorized packet capture may violate privacy laws.
Use only on networks you own or have permission to monitor.
--------------------------------------------------------------------------------

[+] Starting packet capture on interface: Wi-Fi
[!] Press Ctrl+C to stop

-------- Packet #1 --------
Source IP      : 192.168.1.2
Destination IP : 142.250.183.14
Protocol       : TCP
Type           : TCP Packet
Payload        : b'GET / HTTP/1.1...'
```

---


## 👨‍💻 Author

**Sushmita Suryakant Sangle**
Task 5 : Network Packet Analyzer - Completed

---


