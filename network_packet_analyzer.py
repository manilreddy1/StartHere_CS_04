from scapy.all import sniff, IP, TCP, UDP

# Function to process each captured packet
def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        # Get source and destination IP addresses
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "Unknown"
        
        # Determine if the packet is TCP, UDP, or just IP
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif IP in packet:
            protocol = "IP"
        
        # Print packet information
        print(f"Protocol: {protocol} | Source IP: {src_ip} -> Destination IP: {dst_ip}")

# Start sniffing packets
print("Starting packet capture...")
sniff(prn=packet_callback, count=15)  # Modify `count` for more or fewer packets
