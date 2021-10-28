import numpy as np
from matplotlib import pyplot as plt

data1 = np.empty((0,3))

def dataLoad (filename):
    #Create empty matrix of correct dimensions, set number to give linenumber for errors in the data
    data = np.empty((0,3))
    n = 0

    #Open the file, make list with each line of text, close the file
    with open(filename, "r") as f:
        fs = f.read().splitlines()
        f.close
        
        for line in fs:
            #Add 1 to the line-counter, split each element in the line of data into a new array, convert everything to float.
            n += 1
            bacteria = np.array(line.split(' '))
            bacteria = bacteria.astype(float)

            #If the data is anomalous, print corresponding error-code, go to next element in for-loop
            if bacteria[0] < 10 or bacteria[0] > 60:
                print(f"Error: Temperature exeeds limit (Line {n})")
                continue
            if bacteria[1] < 0:
                print(f"Error: Negative growth rate (Line {n})")
                continue
            if bacteria[2] not in [1,2,3,4]:
                print(f"Error: Unknown bacteria (Line {n})")
                continue
            #Add the new array to the matrix
            data = np.append(data, np.array([bacteria]), axis=0)
    return data
    

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


def dataPlot(data):
    #Count sample size for each bacteria
    c_1 = np.count_nonzero(data[:, 2] == 1)
    c_2 = np.count_nonzero(data[:, 2] == 2)
    c_3 = np.count_nonzero(data[:, 2] == 3)
    c_4 = np.count_nonzero(data[:, 2] == 4)

    #Start subplot for bar-chart
    bar = plt.subplots()[1]

    #List names of bacteria, and names for x- and y-axis
    names = ["Salmonella\nenterica", "Bascillus cereus", "Listeria", "Brochothrix\nthermosphacta"]
    bar.set_xlabel("Bacteria Type")
    bar.set_ylabel("Number of samples")

    #Plot and show the bar-chart
    plt.bar(names, [c_1, c_2, c_3, c_4])

    # Start subplot for Growth Rate by Temperature
    graph = plt.subplots()[1]

    #Set axis sizes
    plt.axis([10,60,0,1.5])

    #Sort the data after temperature
    datasort = data[np.argsort(data[:, 0])]

    #Plot each type of bacteria with points and graph, add color-label
    for i in range(4):
        plt.plot(datasort[np.where(datasort[:, 2] == i+1)][:, 0], datasort[np.where(datasort[:, 2] == i+1)][:, 1], marker='o', label=str(names[i]))

    #Show color-labels, set names for x- and y-axis, and plot/show the graph
    plt.legend()
    graph.set_xlabel("Temperature")
    graph.set_ylabel("Growth Rate")
    plt.show()


def tryLoad():
    filename = input("Please input the filename including .txt (ex. file.txt):\n")
    try:
        dataLoad(filename)
    except:
        print("Ineligible filename.")
        return tryLoad()
    print("\nData has been loaded into the program.\n")
    return dataLoad(filename)

def tryStats(data):
    inp = input("Please input the statistic you want to have calculated by entering the corresponding number. Your options are as follows:\n1. Mean Temperature.\n2. Mean Growth rate.\n3. Standard deviation of Temperature.\n4. Standard deviation of Growth rate.\n5. Number of samples.\n6. Mean Growth rate for cold samples.\n7. Mean Growth rate for hot samples.\n")
    statistics = ["Mean Temperature", "Mean Growth rate", "Std Temperature", "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"]
    print(data)
    try:
        print(dataStatistics(data, statistics[int(inp)-1]) + " is the computed " + str(statistics[int(inp)-1]) + "\n")
    except:
        print("Ineligible input, or lack of loaded data.\n") 


def menu():
    choice = input("Please choose one of the following options by entering its corresponding number:\n1. Load data\n2. Filter data\n3. Display statistics\n4. Generate plots\n5. Quit\n")
    if choice == "1":
        data1 = tryLoad()
        menu()
    if choice == "2":
        # Filter
        menu()
    if choice == "3":
        tryStats(data1)
        menu()
    if choice == "4":
        try:
            dataPlot(data1)
        except:
            print("No eligible data to plot, please load data first.\n")
            menu()
    if choice == "5":
        return


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
