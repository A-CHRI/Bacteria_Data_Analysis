import numpy as np
from matplotlib import pyplot as plt
from numpy.lib import emath
### Project Bacteria Data Analysis ###
# s214656 #
# s214614 #
# s214618 #

# The Numpy-library's documentation has been a much used source in the development of this script

### DataLoad function ###
# Erik has worked on this method

#This method takes a string as parameter, and reads a file based on the given string, then returns a matrix of data read from the string
def dataLoad (filename):
    #Create empty matrix of correct dimensions, set number to give linenumber for errors in the data
    data = np.empty((0,3))
    n = 0

    #Open the file, make list with each line of text, close the file
    with open(filename, "r") as f:
        fs = f.read().splitlines()
        
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
    
### DataStatistics functions ###
# Erik has worked on this method

#This method takes a nx3 matrix of data and a string as parameter, and returns a statistic from the data. Which statistic gets returned is based on the string
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

### DataPlot functions ###
# Erik has worked on this method

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


### Filter function ###

# Functions for the various filters
def temperatureFilter(data):
    while True:
        # Creates a seperator for the layout
        print("\n---------------------------------------")
        # Prompts the user to enter the temperature range
        print("\nPlease enter the temperature range you would like to filter by, and enter 'done' to continue")
        tempMin = input("\nMinimum Temperature: ")
        tempMax = input("Maximum Temperature: ")
        if tempMin.casefold() == "done" or tempMax.casefold() == "done":
            break
        else:
            try:
                tempMin = int(tempMin)
                tempMax = int(tempMax)
                if tempMin > tempMax:
                    print("\nInvalid input, please try again.")
                else:
                    break
            except:
                print("\nInvalid input, please try again.")
    # Filters the data based on the temperature range
    data = data[data[:,0].astype(float) >= tempMin]
    data = data[data[:,0].astype(float) <= tempMax]
    print("\nSuccesfully applied the filter.")
    return data

def bacteriaFilter(data):
    bacteria = ["Salmonella enterica", "Bascillus cereus", "Listeria", "Brochothrix thermosphacta"]
    while True:
        # Creates a seperator for the layout
        print("\n---------------------------------------")
        # Prompts the user to apply or unapply the varous filters
        print("\nYou are about to filter the following bacteria:")

        # Prints the already filtered bacteria
        if len(appliedBacteria) > 0:
            for i,v in enumerate(appliedBacteria):
                print(i+1, ":", v)
        else:
            print("None")

        # Prints the list of bacteria to choose from
        print("\nPlease enter the bacteria you would like to add or remove from the filter, and enter 'done' to continue (Choose by entering the corresponding number)")
        for i,v in enumerate(bacteria):
            print(i+1, ":", v)

        # Gets the users input
        inp = input("\nBacteria: ")
        if inp.casefold() == "done":
            print("\nThe filter has been applied")
            break
        
        # If the input matches a bacterias number, add the bacteria to the list of applied bacteria-filters, or remove it if it already was in the list
        if inp in ["1","2","3","4"]:
            intc = int(inp) - 1
            if bacteria[intc] in appliedBacteria:
                appliedBacteria.remove(bacteria[intc])
                print("\nRemoved bacteria filter for", bacteria[intc])
            else:
                appliedBacteria.append(bacteria[intc])
                print("\nAdded bacteria filter for", bacteria[intc])
    
    # Get the filtered bacterias corresponding numbers
    bactNumbs = []
    for i in appliedBacteria:
        bactNumbs.append(bacteria.index(i)+1)

    # Filter the bacterias that aren't chosen from the data
    mask = np.isin(data[:,2], bactNumbs)
    print("\nSuccesfully applied the filters.")
    return data[mask]

def growthRateFilter(data):
    while True:
        # Creates a seperator for the layout
        print("\n---------------------------------------")
        # Prompts the user to enter the growthrate range
        print("\nPlease enter the growthrate range you would like to filter by, and enter 'done' to continue (decimals are set with a dot ('.')")
        growthMin = input("\nLower bound: ")
        growthMax = input("Upper bound: ")
        if growthMin.casefold() == "done" or growthMax.casefold() == "done":
            break
        else:
            try:
                growthMin = float(growthMin)
                growthMax = float(growthMax)
                if growthMin > growthMax:
                    print("\nInvalid input, please try again.")
                else:
                    break
            except:
                print("\nInvalid input, please try again.")
    # Filters the data based on the temperature range
    data = data[data[:,1].astype(float) >= growthMin]
    data = data[data[:,1].astype(float) <= growthMax]
    print("\nSuccesfully applied the filter.")
    return data

#This method takes a nx3 matrix of data as parameter, and filters the data based upon input from the user
def filter(data):
    filters = ["Bacteria", "Temperature", "Growth rate"]
    while True:
        # Creates a seperator for the layout
        print("\n---------------------------------------")
        # Prompts the user to apply or unapply the varous filters
        print("\nYou are about to apply the following filters:")
        if len(appliedFilters) > 0:
            for i,v in enumerate(appliedFilters):
                print(i+1, ":", v)
        else:
            print("None")

        print("\nPlease enter the filter you would like to apply or unapply, and enter 'done' to continue (Choose by entering the corresponding number)")
        for i,v in enumerate(filters):
            print(i+1, ":", v)

        inp = input("\nInput: ")
        if inp.casefold() == "done":
            break

        if inp in ["1","2","3"]:
            intc = int(inp) - 1 
            # Applies or unapplies the filter based upon the user's input
            if filters[intc] in appliedFilters:
                appliedFilters.remove(filters[intc])
                print("\nFilter removed")
            else:
                appliedFilters.append(filters[intc])
                print("\nFilter applied")

        else:
            print("\nInvalid input, please try again.")

    # Filters the data based on the list of applied filters
    if len(appliedFilters) > 0:
        for i in appliedFilters:
            if i == "Bacteria":
                data = bacteriaFilter(data)
            elif i == "Temperature":
                data = temperatureFilter(data)
            elif i == "Growth rate":
                data = growthRateFilter(data)

    # Returns the filtered data
    return data


## Tryload function ##
# Erik has worked on this method

#This method tries to use the dataLoad method, and in case the user doesnt give a suitable input, catch the error
def tryLoad():
    # Creates a seperator for the layout
    print("\n---------------------------------------")
    #Get the users input
    print("Please enter the filename of the files you wish to load including .txt (ex file.txt).")
    filename = input("\nFilename: ")
    #Try to load the file
    try:
        data = dataLoad(filename)
        #In case this works, notify the user, return the loaded data
        print("\nData has been loaded into the program.\n")
        return data
    except:
        #In case it doesnt work, print that the input was ineligible, and an option to give another input
        inp = input("Ineligible filename. Would you like to try again? (y/n)\n")
        if inp.casefold() == "y":
            return tryLoad()


### TryStats function ###
# Erik has worked on this method

#This method tries to use the dataStatistics method, and in case the user doesnt give a suitable input, catch the error
def tryStats(data):
    statistics = ["Mean Temperature", "Mean Growth rate", "Std Temperature", "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"]
    # Creates a seperator for the layout
    print("\n---------------------------------------")
    #Get the users input, make a list with the statistic names
    print("\nPlease enter the correspoinding number to the statistic you want calculated.")
    for i,v in enumerate(statistics):
        print(i+1, ":", v)
    inp = input("\nStatistic: ")
    #Try to get the statistic based on the input, and print it out if it works
    try:
        print(str(dataStatistics(data, f"{statistics[int(inp)-1]}")) + " is the computed " + str(statistics[int(inp)-1]) + "\n")
    except:
        #In case it doesnt work, print that the input was ineligible, and an option to give another input
        inp = input("Ineligible input or missing dataset. Would you like to try again? (y/n)\n") 
        if inp.casefold() == "y":
            tryStats(data)


### Main Script ###
# Erik has worked on this script

#Main Script, only runs if the file is run directly, this isn't executed if the file is imported to use as a library
if __name__ == '__main__':
    #Create empty array to store data in
    data = np.empty((0,3))
    dataRef = np.array([])

    # Creates a list for the different filters, and creates a list of the different applied filters
    appliedFilters = []

    # Creates a list of the different bacteria, and creates a list of the different applied bacteria filters
    appliedBacteria = []

    # List of options in the main menu
    options = ["Load data", "Filter data", "Display statistics", "Generate plots", "Quit"]

    #While loop to make sure the user returns to the menu of the interface
    while True:
        # Creates a seperator for the layout
        print("\n---------------------------------------")
        # Prints the options in the menu, and gets the users input
        print("\nPlease choose one of the following options by entering its corresponding number:\n")
        for i,v in enumerate(options):
            print(i+1, ":", v)
        inp = input("\nInput: ")

        if inp == "1":
            #If they want to load data into the data, call the tryLoad method, save the returned data in the data variable
            data = tryLoad()
            dataRef = np.array(data, copy=True)

        elif inp == "2":
            #If they want to filter the data, call the filter method with data as parameter, save the returned data in the data variable
            data = filter(dataRef)

        elif inp == "3":
            #If they want to compute stats based on the data, call the tryStats method with data as a parameter
            tryStats(data)

        elif inp == "4":
            #If they want to plot the data, try to call the dataPlot method with data as a parameter
            try:
                dataPlot(data)
            except:
                #This throws an exception if the data variable doesn't contain any data, and in that case, print that there are no eligible data to plot
                print("No eligible data to plot, please load data first.\n")

        elif inp == "5":
            #If they want to quit the program, break the while-loop
            break

        else:
            #If none of the given options were chosen as an input, print that they gave an ineligible input
            print("Ineligible input, please try again.")