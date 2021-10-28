import numpy as np
from matplotlib import pyplot as plt
from dataLoadTest import dataLoad

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


data = dataLoad("fil.txt")
dataPlot(data)