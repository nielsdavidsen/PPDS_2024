import sys 
sys.path.append('AC/Uge_3/Afl_3')

import handin3_project as h3p

data_filtered = h3p.read_data2("Land_and_Ocean_summary.txt", (2000, 2010))

all_data = h3p.read_data2("Land_and_Ocean_summary.txt")

temp_anomaly_data = h3p.read_data3("Land_and_Ocean_summary.txt", (2015, 2018))

print(temp_anomaly_data)


