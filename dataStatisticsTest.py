import numpy as np
import math
def dataStatistics(data, statistic):
    if np.shape(data)[0] < 1:
        return 0

    if statistic == "Mean Temperature":
        return np.mean(data, axis=0)[0]

    if statistic == "Mean Growth rate":
        return np.mean(data, axis=0)[1]

    if statistic == "Std Temperature":
        return np.std(data, axis=0)[0]

    if statistic == "Std Growth rate":
        return np.std(data, axis=0)[1]

    if statistic == "Rows":
        return np.shape(data)[0]

    if statistic == "Mean Cold Growth rate":
        colddata = data[np.where(data[:, 0] < 20)]
        if np.shape(colddata)[0] > 0:
            return np.mean(colddata, axis=0)[1]
        else:
            return 0

    if statistic == "Mean Hot Growth rate":
        hotdata = data[np.where(data[:, 0] > 50)]
        if np.shape(hotdata)[0] > 0:
            return np.mean(hotdata, axis=0)[1]
        else:
            return 0

# Test scenario
data = np.array([[11, 0.560, 2], [12, 0.777, 1]])

mt = dataStatistics(data, "Mean Temperature")
print(f"Mean Temperature: {mt}")

mgr = dataStatistics(data, "Mean Growth Rate")
print(f"Mean Growth Rate: {mgr}")

st = dataStatistics(data, "Std Temperature")
print(f"Std Temperature: {st}")

sgr = dataStatistics(data, "Std Growth Rate")
print(f"Std Growth Rate: {sgr}")

rows = dataStatistics(data, "Rows")
print(f"Rows: {rows}")

mcgr = dataStatistics(data, "Mean Cold Growth Rate")
print(f"Mean Cold Growth Rate: {mcgr}")

mhgr = dataStatistics(data, "Mean Hot Growth Rate")
print(f"Mean Hot Growth Rate: {mhgr}")