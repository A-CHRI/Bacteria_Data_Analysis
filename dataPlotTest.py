import numpy as np
from matplotlib import pyplot as plt
from dataLoadTest import dataLoad

#This method takes a nx3 matrix of data as parameter, and makes 2 plots of the data, 1 barchart of the bacteria types, 1 graph of the ratio between temperature and growth rate
def dataPlot(data):
    #Count sample size for each bacteria
    c_1 = np.count_nonzero(data[:, 2] == 1)
    c_2 = np.count_nonzero(data[:, 2] == 2)
    c_3 = np.count_nonzero(data[:, 2] == 3)
    c_4 = np.count_nonzero(data[:, 2] == 4)

    fig, (ax1,ax2) = plt.subplots(1, 2)
    fig.set_size_inches(12, 6)
    fig.suptitle("Bacteria data analysis")

    #List names of bacteria, and names for x- and y-axis
    names = ["Salmonella\nenterica", "Bascillus cereus", "Listeria", "Brochothrix\nthermosphacta"]
    ax1.set_xlabel("Bacteria Type")
    ax1.set_ylabel("Number of samples")

    #Plot and show the bar-chart
    ax1.bar(names, [c_1, c_2, c_3, c_4])

    # #Set axis sizes
    # ax1.axis([10,60,0,1.5])

    #Sort the data after temperature
    datasort = data[np.argsort(data[:, 0])]

    #Plot each type of bacteria with points and graph, add color-label
    for i in range(4):
        ax2.plot(datasort[np.where(datasort[:, 2] == i+1)][:, 0], datasort[np.where(datasort[:, 2] == i+1)][:, 1], marker='o', label=str(names[i]))

    #Show color-labels, set names for x- and y-axis, and plot/show the graph
    ax2.legend()
    ax2.set_xlabel("Temperature")
    ax2.set_ylabel("Growth Rate")
    fig.show()


data = dataLoad("fil.txt")
dataPlot(data)