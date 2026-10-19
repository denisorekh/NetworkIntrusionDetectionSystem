# Тестовый дата-коллектор, создающий из pcap sessions
from scapy.all import PcapReader
from scapy.layers.inet import IP, TCP, UDP


def generate(pcap):
    sessions = {} # Словарь сессий

    with (PcapReader(pcap) as p):
        for packet in p:
            if packet.haslayer(IP):
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                if packet.haslayer(TCP):
                    proto = "TCP"
                    src_p = packet[TCP].sport
                    dst_p = packet[TCP].dport
                if packet.haslayer(UDP):
                    proto = "UDP"
                    src_p = packet[UDP].sport
                    dst_p = packet[UDP].dport

                    if (src_ip, src_p) < (dst_ip, dst_p):
                        key = (src_ip, src_p, dst_ip, dst_p, proto)
                        direction = "a->b"
                    else:
                        key = (dst_ip, dst_p, src_ip, src_p, proto)
                        direction = "a<-b"

                    if key not in sessions:
                        sessions[key] = {
                            "start": float(packet.time),
                            "end": float(packet.time),
                            "a->b": {
                                "packets": 0,
                                "bytes": 0
                            },
                            "a<-b": {
                                "packets": 0,
                                "bytes": 0
                            },
                            "packets_sizes": []
                        }

                    session = sessions[key]
                    session["end_time"] = float(packet.time)

                    session[direction]["packets"] += 1
                    session[direction]["bytes"] += (len(packet))
                    session["packets_sizes"].append(len(packet))

        return sessions


res = generate("../data/test1.pcap")
for i in res:
    print(i)
