from binascii import hexlify
import sys
import struct

def read_pcap_packets(filename):
    """Read PCAP file and extract packets with timestamps"""
    packets = []
    with open(filename, 'rb') as f:
        # Skip PCAP global header (24 bytes)
        f.read(24)
        
        while True:
            # Read packet header (16 bytes)
            pkt_header = f.read(16)
            if len(pkt_header) < 16:
                break

            ts_sec, ts_usec, incl_len, orig_len = struct.unpack('<LLLL', pkt_header)

            # Read packet data
            pkt_data = f.read(incl_len)
            if len(pkt_data) < incl_len:
                break

            # Calculate timestamp in milliseconds
            timestamp = ts_sec * 1000 + ts_usec // 1000
            packets.append({'timestamp': timestamp, 'data': pkt_data})
    
    return packets

def main():
    s = ""
    last_t = 0
    
    if len(sys.argv) != 2:
        print("Usage: python parsePcap.py <pcap.file>")
        return

    filename = sys.argv[1]
    packets = read_pcap_packets(filename)

    for packet in packets:
        # Check for 65-byte packets (0x41 = 65, hexlify makes it 130 chars)
        if len(hexlify(packet['data'])) == 0x41 * 2:
            # Get last byte (NumLock LED state)
            leftover_packet_data = hexlify(packet['data'])[-2:].decode()

            t = packet['timestamp']
            diff = t - last_t
            last_t = t
            
            # Skip very large time gaps (> 100 seconds)
            if diff > 100000:
                continue
            
            # NumLock LED decoding:
            # 0x01 = NumLock OFF, 0x02 = NumLock ON
            # Modified from original CapsLock (0x01 OFF, 0x03 ON)
            
            if leftover_packet_data != "02":  # NumLock OFF (0x01)
                if diff > 300:
                    s += "_"  # Long gap = letter separator
                else:
                    s += "."  # Short gap = symbol separator
            else:  # NumLock ON (0x02)
                if diff < 300:
                    s += ""   # Very short = ignore
                else:
                    s += " "  # Space between elements
    
    print(s)

if __name__ == "__main__":
    main()
