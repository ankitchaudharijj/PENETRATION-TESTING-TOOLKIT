# 🛠️ Pentest Toolkit

A modular penetration testing toolkit built with Python. This toolkit provides various essential functionalities used in ethical hacking and security testing, including port scanning, brute-forcing, subdomain enumeration, banner grabbing, and WHOIS lookup.

## 📦 Features

- 🔍 Port Scanner (TCP)
- 🔐 SSH Brute Forcer (via Paramiko)
- 🔐 FTP Brute Forcer
- 🌐 WHOIS Domain Lookup
- 🌐 Subdomain Enumerator
- 🧾 Banner Grabber
- 📟 Menu-driven CLI interface

## 🧰 Requirements

Install all dependencies:
```bash
pip install -r requirements.txt
```

Dependencies:
- paramiko
- python-whois
- requests

## 🚀 Usage

Run the toolkit:
```bash
python pentest_toolkit.py
```

Then follow the interactive menu:
```
1. Port Scanner
2. SSH Brute Force
3. FTP Brute Force
4. WHOIS Lookup
5. Subdomain Enumeration
6. Banner Grabbing
7. Exit
```

## 📁 File Requirements

- passwords.txt — used by brute-force modules
- subdomains.txt — used for subdomain enumeration

## ⚠️ Legal Disclaimer

This toolkit is intended for educational and authorized security testing purposes only. 
Do not use against systems or networks you don’t have explicit permission to test.

## 💡 Author

Made by Ankit (with ❤️ and a pinch of ⚔️ by ChatGPT)
