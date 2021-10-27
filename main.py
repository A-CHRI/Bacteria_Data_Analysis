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
    c_1 = np.count_nonzero(data[:, 2] == 1)
    c_2 = np.count_nonzero(data[:, 2] == 2)
    c_3 = np.count_nonzero(data[:, 2] == 3)
    c_4 = np.count_nonzero(data[:, 2] == 4)

    bar = plt.subplots()[1]
    names = ["Salmonella\nenterica", "Bascillus cereus", "Listeria", "Brochothrix\nthermosphacta"]
    bar.set_xlabel("Bacteria Type")
    bar.set_ylabel("Number of samples")
    plt.bar(names, [c_1, c_2, c_3, c_4])

    # Growth Rate by Temperature
    graph = plt.subplots()[1]
    plt.axis([10,60,0,1.5])
    datasort = data[np.argsort(data[:, 0])]
    for i in range(4):
        plt.plot(datasort[np.where(datasort[:, 2] == i+1)][:, 0], datasort[np.where(datasort[:, 2] == i+1)][:, 1], marker='o', label=str(names[i]))
    plt.legend()
    graph.set_xlabel("Temperature")
    graph.set_ylabel("Growth Rate")
    plt.show()

# Main Script
if __name__ == '__main__':
    while True:
        data = np.empty((0,3))
        choice = input("Please choose one of the following options by entering its corresponding number:\n1. Load data\n2. Filter data\n3. Display statistics\n4. Generate plots\n5. Quit\n")
        if choice == "1":
            filename = input("Please input the filename including .txt (ex. file.txt):\n")
            try:
                data = dataLoad(filename)
            except:
                print("Ineligible filename.")
                continue
            data = dataLoad(filename)
            print("\nData has been loaded into the program.\n")
            continue
        if choice == "2":
            # Filter
            continue
        if choice == "3":
            inp = input("Please input the statistic you want to have calculated by entering the corresponding number. Your options are as follows:\n1. Mean Temperature.\n2. Mean Growth rate.\n3. Standard deviation of Temperature.\n4. Standard deviation of Growth rate.\n5. Number of samples.\n6. Mean Growth rate for cold samples.\n7. Mean Growth rate for hot samples.\n")
            statistics = ["Mean Temperature", "Mean Growth rate", "Std Temperature", "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"]
            print(data)
            try:
                print(dataStatistics(data, statistics[int(inp)-1]) + " is the computed " + str(statistics[int(inp)-1]) + "\n")
            except:
                print("Ineligible input, or lack of loaded data.")
            continue
        if choice == "4":
            dataPlot(data)
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