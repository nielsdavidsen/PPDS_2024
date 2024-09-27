import handin4_project as h4p

anomaly_data = h4p.AnomalyData('Land_and_Ocean_summary.txt')
value = anomaly_data.data[1990][0]
print(value)


decade_dict = anomaly_data.one_value_per_decade()
print(decade_dict)