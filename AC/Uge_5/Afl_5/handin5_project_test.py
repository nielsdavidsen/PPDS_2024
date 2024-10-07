import numpy as np

anomaly_data = np.genfromtxt('Land_and_Ocean_summary.txt', delimiter='', comments='%')

print((anomaly_data[1]))