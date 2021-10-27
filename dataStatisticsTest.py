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

data = np.array([[11, 0.560, 2], [12, 0.777, 1]])

print(dataStatistics(data, "Std Growth rate"))