import socket
import struct
import argparse

def get_protocol_name(proto):
    if proto == 6:
        return "TCP"
    elif proto == 17:
        return "UDP"
    elif proto == 1:
        return "ICMP"
    else:
        return str(proto)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", default="Wi-Fi")
    parser.add_argument("-c", "--count", type=int, default=5)
    args = parser.parse_args()

    print("="*70)
    print("NETWORK PACKET ANALYZER")
    print("="*70)
    print("WARNING: This tool is for educational purposes only.")
    print("Unauthorized packet capture may violate privacy laws.")
    print("Use only on networks you own or have permission to monitor.")
    print("="*70)

    print(f"\n[+] Starting packet capture on interface: {args.interface}")
    print("[!] Press Ctrl+C to stop")
    print("[!] Educational use only. Capture authorized traffic only.\n")

    try:
        # Create raw socket
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

        host = socket.gethostbyname(socket.gethostname())
        sniffer.bind((host, 0))

        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        packet_count = 1

        while packet_count <= args.count:
            raw_data, _ = sniffer.recvfrom(65565)

            # IP Header
            ip_header = raw_data[0:20]
            unpacked = struct.unpack("!BBHHHBBH4s4s", ip_header)

            src_ip = socket.inet_ntoa(unpacked[8])
            dest_ip = socket.inet_ntoa(unpacked[9])
            proto_num = unpacked[6]
            proto_name = get_protocol_name(proto_num)

            payload = raw_data[20:60]

            print(f"-------- Packet #{packet_count} --------")
            print(f"Source IP      : {src_ip}")
            print(f"Destination IP : {dest_ip}")
            print(f"Protocol       : {proto_name}")
            print(f"Type           : {proto_name} Packet")
            print(f"Payload        : {payload}")
            print()

            packet_count += 1

        # Turn off promiscuous mode
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

    except PermissionError:
        print("Run as Administrator!")
    except KeyboardInterrupt:
        print("\nStopped by user")

if __name__ == "__main__":
    main()