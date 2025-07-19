from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] Packet Captured:")
        print(f"    From: {ip_layer.src}")
        print(f"    To  : {ip_layer.dst}")
        print(f"    Protocol: {ip_layer.proto}")

        if TCP in packet:
            print("    Contains TCP")
        elif UDP in packet:
            print("    Contains UDP")

        print(f"    Payload: {str(bytes(packet.payload))[:100]}")  # limit display

print("Starting Packet Sniffer...\nPress Ctrl+C to stop.")
sniff(prn=packet_callback, count=10)
