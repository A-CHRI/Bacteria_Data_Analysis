import numpy as np
from matplotlib import pyplot as plt
from dataLoadTest import dataLoad

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

data = dataLoad("fil.txt")
dataPlot(data)