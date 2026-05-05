# Advanced Network Packet Sniffer (Python + Scapy)

A lightweight yet powerful network traffic capture and analysis tool built with Python and Scapy. This tool is designed for cybersecurity learning, traffic inspection, and basic intrusion detection experimentation.

## 🚀 Features

- Live packet capture from selected network interface
- Supports TCP, UDP, ICMP, and IP packet analysis
- Extracts:
  - Source & Destination IP
  - Ports (TCP/UDP)
  - Protocol type
  - Payload size
- Real-time terminal output
- Save captured traffic to `.pcap` (Wireshark compatible)
- Modular design for extensibility

## 🛠️ Tech Stack

- Python 3
- Scapy
- argparse

## 📦 Installation

```bash
git clone https://github.com/kingsooko/Advanced-Network-Sniffer-Tool-1.0.git
cd Advanced-Network-Sniffer-Tool-1.0
pip3 install -r requirements.txt

▶️ Usage
sudo python3 sniffer.py -i <interface>

Example:
sudo python3 sniffer.py -i wlan0

Capture a limited number of packets:

sudo python3 sniffer.py -i eth0 -c 100

Save to a PCAP file:

sudo python3 sniffer.py -i eth0 -o capture.pcap

⚙️ Arguments
Argument	Description
-i, --interface	Network interface (required)
-c, --count	Number of packets (default: unlimited)
-o, --output	Output file (.pcap)

📁 Project Structure
project-name/
├── main.py              # Entry point
├── requirements.txt    # Dependencies
├── README.md           # Documentation
├── .gitignore          # Ignored files
└── modules/            # Modular packet processing logic
⚠️ Disclaimer

This tool is intended for educational purposes and authorized environments only.
Do not use it on networks without explicit permission.

👨‍💻 Author

HRH PRINCE ADEWOYE OYINDAMOLA
Cybersecurity Analyst | Ethical Hacker/Penetration Tester
