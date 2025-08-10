from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[+] New Packet: {ip_layer.src} -> {ip_layer.dst}")
        print(f"    Protocol: {ip_layer.proto}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            payload = bytes(tcp_layer.payload)
            print(f"    TCP Payload: {payload[:50]}")

        elif UDP in packet:
            udp_layer = packet[UDP]
            payload = bytes(udp_layer.payload)
            print(f"    UDP Payload: {payload[:50]}")
            

print("Starting packet sniffer...")
sniff(prn=packet_callback, store=0)
