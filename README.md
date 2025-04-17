# NetSniff

NetSniff is a lightweight and fast network traffic sniffer developed for Kali Linux and similar systems.

## 🚀 Features
- Select a specific network interface (e.g., `wlan0`, `eth0`)
- Filter by packet type (`tcp`, `udp`, `icmp`)
- Capture a specified number of packets
- Clean and colorful terminal output
- Requires root permissions
- Simple, fast, and minimal (only Python + Scapy)

## 🛠 Requirements
- Python 3.7+
- Kali Linux or similar Linux distribution
- Root privileges
- Python libraries:
  - scapy
  - colorama

Install with:
\`\`\`bash
pip install scapy colorama
\`\`\`

## 📦 Installation
1. Clone the repository:
    \`\`\`bash
    git clone https://github.com/Xliofpir/netsniff.git
    cd netsniff
    \`\`\`

2. Set up the environment:
    \`\`\`bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    \`\`\`

3. Run the tool:
    \`\`\`bash
    sudo python3 main.py
    \`\`\`

## ⚡ Usage
When the program starts, it will ask:
- Which interface you want to listen to (\`wlan0\`, \`eth0\`, etc.)
- Which packet type you want to capture (\`tcp\`, \`udp\`, \`icmp\`, leave empty for all)
- How many packets you want to capture

Example:
\`\`\`
Select interface [wlan0 / eth0]: wlan0
Type packet type (leave empty for all packets): tcp
How many packets do you want to display: 50
\`\`\`

Example output:
\`\`\`
[TCP] 192.168.1.2 --> 8.8.8.8
[UDP] 192.168.1.2 --> 192.168.1.1
\`\`\`

## 📚 FAQ (Frequently Asked Questions)

**Q:** Can I run it without root permissions?  
**A:** No, capturing network traffic directly requires root privileges.

**Q:** Can I filter by specific ports?  
**A:** Currently, filtering is based only on protocols. Port-based filtering is planned for future versions.

**Q:** Does it work on Windows?  
**A:** Theoretically yes, but it is optimized for Linux systems.

## 📝 To-Do List
- [ ] Save captured packets into a `.pcap` file
- [ ] Display port numbers and MAC addresses
- [ ] Multi-interface listening
- [ ] Basic GUI (Graphical User Interface)
- [ ] Live filter update during capture

## 🤝 Contributing
Pull requests and suggestions are welcome! 🎉  
For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
