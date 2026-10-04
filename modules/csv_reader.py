import pandas as pd

import zipfile as zip
# import csv

with zip.ZipFile("../data/archive.zip") as z:
    with z.open("Monday-WorkingHours.pcap_ISCX.csv") as mon:
        monday = pd.read_csv(mon)
    # with z.open("Tuesday-WorkingHours.pcap_ISCX.csv") as tue:
    #     tuesday = pd.read_csv(tue)
    # with z.open("Wednesday-workingHours.pcap_ISCX.csv") as wed:
    #     wednesday = pd.read_csv(wed)
    # with z.open("Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv") as thu1:
    #     thursday1 = pd.read_csv(thu1)
    # with z.open("Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv") as thu2:
    #     thursday2 = pd.read_csv(thu2)
    # with z.open("Friday-WorkingHours-Morning.pcap_ISCX.csv") as fri1:
    #     friday1 = pd.read_csv(fri1)
    # with z.open("Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv") as fri2:
    #     friday2 = pd.read_csv(fri2)
    # with z.open("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv") as fri3:
    #     fri3 = pd.read_csv(fri3)

print(len(monday.columns.tolist()))

monday = monday.replace([float("inf"), float("-inf")], pd.NA)

# Удаляем строки с NaN
monday = monday.dropna()




