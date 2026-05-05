from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw, wrpcap
from datetime import datetime

captured_packets = []

def process_packet(packet):
    if IP not in packet:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_layer = packet[IP]

    src_ip = ip_layer.src
    dst_ip = ip_layer.dst

    layer = "OTHER"
    src_port = ""
    dst_port = ""

    if TCP in packet:
        layer = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
    elif UDP in packet:
        layer = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
    elif ICMP in packet:
        layer = "ICMP"

    payload_size = len(packet[Raw].load) if Raw in packet else 0

    captured_packets.append(packet)

    print(f"[{timestamp}] {layer} {src_ip}:{src_port} -> {dst_ip}:{dst_port} | Payload: {payload_size} bytes")


def start_sniff(interface, packet_count, output_file):
    print(f"\n[*] Sniffing on {interface}... (Ctrl+C to stop)\n")

    try:
        sniff(iface=interface, prn=process_packet, count=packet_count, store=False)
    except KeyboardInterrupt:
        print("\n[!] Capture stopped.")

    if output_file and captured_packets:
        wrpcap(output_file, captured_packets)
        print(f"[+] Saved to {output_file}")
