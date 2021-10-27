import math
import numpy as np
from matplotlib import pyplot as plt

def dataLoad (filename):
    data = np.empty((0,3))
    n = 0
    with open(filename, "r") as f:
        fs = f.read().splitlines()
        for line in fs:
            n += 1
            bacteria = np.array(line.split(' '))
            bacteria = bacteria.astype(float)
            if bacteria[0] < 10 or bacteria[0] > 60:
                print(f"Error: Temperature exeeds limit (Line {n})")
                continue
            if bacteria[1] < 0:
                print(f"Error: Negative growth rate (Line {n})")
                continue
            if bacteria[2] not in [1,2,3,4]:
                print(f"Error: Unknown bacteria (Line {n})")
                continue
            data = np.append(data, np.array([bacteria]), axis=0)
    return data

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

def dataPlot(data):
    # Number of bacteria
    c_1,c_2,c_3,c_4 = 0,0,0,0
    for x in data:
        if int(x[2]) == 1: c_1 += 1
        if int(x[2]) == 2: c_2 += 1
        if int(x[2]) == 3: c_3 += 1
        if int(x[2]) == 4: c_4 += 1
    names = ["Salmonella enterica", "Bascillus cereus", "Listeria", "Brochothrix thermosphacta"]
    plt.figure(1)
    plt.bar(names, [c_1, c_2, c_3, c_4])

    # Growth Rate by Temperature
    growthRate = []
    temperature = []
    for x in data:
        growthRate.append(float(x[1]))
        temperature.append(float(x[0]))
    plt.figure(2)
    plt.axis([10,60,0,1.5])
    plt.scatter(temperature, growthRate)
    plt.show()

# Main Script
while True:
    print("Please choose one of the following options:\n1. Load data\n2. Filter data\n3. Display statistics\n4. Generate plots\n5. Quit")
    choice = input()
    if choice == "1":
        data = input("Please input the filename including .txt (ex. file.txt):")
        if data[-4] != ".txt":
            print("File does not end with .txt")
            continue
        dataLoad(data)
        continue
    if choice == "2":
        # Filter
        continue
    if choice == "3":
        # Display statistics
        continue
    if choice == "4":
        # Display plots
        continue
    if choice == "5":
        break


# Test scenarios
print("--- TEST: dataLoad function ---")
file = "fil.txt"
data = dataLoad(file)
for x in data:
    for y in x:
        print(y, end = " ")
    print()

print("--- TEST: Statistics function ---")

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

print("--- TEST: dataPlot function ---")
dataPlot(data)