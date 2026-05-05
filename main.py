#!/usr/bin/env python3

import argparse
from modules.sniffer import start_sniff

def main():
    parser = argparse.ArgumentParser(description="Advanced Packet Sniffer")

    parser.add_argument("-i", "--interface", required=True, help="Network interface")
    parser.add_argument("-c", "--count", type=int, default=0, help="Packet count (0 = unlimited)")
    parser.add_argument("-o", "--output", help="Output PCAP file")

    args = parser.parse_args()

    start_sniff(args.interface, args.count, args.output)

if __name__ == "__main__":
    main()
