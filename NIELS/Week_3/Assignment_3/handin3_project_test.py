import handin3_project as h3p
data_list_returned = h3p.read_data2("Land_and_Ocean_summary.txt")
#print(data_list_returned)


year_range = (2015, 2018)
temp_anomaly_data = h3p.read_data3("Land_and_Ocean_summary.txt", year_range)
print(temp_anomaly_data)