import numpy as np


def dataStatistics(data, statistic):
    #If there are no rows in the data, return 0
    if np.shape(data)[0] < 1:
        return 0

    #If mean temp is to be computed, return mean temp
    if statistic == "Mean Temperature":
        return np.mean(data, axis=0)[0]

    #If mean growth rate is to be computed, return mean growth rate
    if statistic == "Mean Growth rate":
        return np.mean(data, axis=0)[1]

    #If std of temp is to be computed, return std of temp
    if statistic == "Std Temperature":
        return np.std(data, axis=0)[0]

    #If std of growth rate is to be computed, return std of growth rate
    if statistic == "Std Growth rate":
        return np.std(data, axis=0)[1]

    #If rows are to be computed, return rows
    if statistic == "Rows":
        return np.shape(data)[0]

    #If mean growth rate of cold samples is to be computed, choose cold samples
    if statistic == "Mean Cold Growth rate":
        colddata = data[np.where(data[:, 0] < 20)]
        
        #If there are no cold samples, return 0, otherwise return mean growth rate of the cold samples
        if np.shape(colddata)[0] > 0:
            return np.mean(colddata, axis=0)[1]
        else:
            return 0

    #If mean growth rate of hot samples is to be computed, choose hot samples
    if statistic == "Mean Hot Growth rate":
        hotdata = data[np.where(data[:, 0] > 50)]

        #If there are no hot samples, return 0, otherwise return mean growth rate of the hot samples
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