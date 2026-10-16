# Тестовый дата-коллектор, создающий из pcap sessions
from scapy.all import PcapReader
from scapy.layers.inet import IP


def generate(pcap):
    sessions = {} # Словарь сессий

    """
        timeof the session = ...
        a -> b packets = ...
        a <- b packets = ...
        a -> b bytes = ...
        a <- b bytes = ...
        min bytes = ...
        max bytes = ...
        median bytes = ...
    """

    with PcapReader(pcap) as p:
        for packet in p:
            if packet.haslayer(IP):
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                src_p = packet[IP].sport
                dst_p = packet[IP].dport


                if (src_ip, src_p) < (dst_ip, dst_p):
                    key = (src_ip, src_p, dst_ip, dst_p)
                else:
                    key = (dst_ip, dst_p, src_ip, src_p)

                if key not in sessions.keys():
                    sessions[(src_ip, src_p, dst_ip, dst_p)] = {
                        "timeoff":      None,
                        "a->b":         1,
                        "a<-b":         0,
                        "a->b_bytes":   len(packet),
                        "a<-b_bytes":   0,
                        "min_b":        len(packet),
                        "max_b":        len(packet),
                        "med_b":        len(packet)
                    }
                    print(f"src: {packet[IP].src} -> dst: {packet[IP].dst}")
                else:
                    sessions[key] = {
                        "timeoff":      None,
                        "a->b":         "??????",
                        "a<-b":         "??????",
                        "a->b_bytes":   "??????",
                        "a<-b_bytes":   "??????",
                        "min_b":        "??????",
                        "max_b":        "??????",
                        "med_b":        "??????"
                    }

"""
ПРОБЛЕМЫ С ТЕКУЩИМ ОБРАБОТЧИКОМ
1. порты беруться не с того уровня
2. неправильно обновляются метрики
3. не сделан подсчёт метрик timeof, min, max, med
"""

generate("../data/test1.pcap")
