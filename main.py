import numpy as np
from matplotlib import pyplot as plt

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

#This method takes a nx3 matrix of data as parameter, and makes 2 plots of the data, 1 barchart of the bacteria types, 1 graph of the ratio between temperature and growth rate
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

#This method takes a nx3 matrix of data as parameter, and filters the data based upon input from the user
def filter(data):
    #Get the users input on how the data should be filtered
    print("How would you like to filter your data? Choose by writing the corresponding number.")
    filterInput = input("1. By bacteria.\n2. By Growth rate\n3. By Temperature\n")
    #Here we make sure to catch any error based on input formatted wrong
    try: 
        if int(filterInput) == 1:
            #If the user chose to filter the data by bacteria type, get their input on which bacteria types should be included, put the choices into an array
            bactType = input("Which bacteria type would you like to see? Choose by writing the corresponding number, you may choose several by seperating the numbers with space.\n1. Salmonella enterica\n2. Bascillus cereus\n3. Listeria\n4. Brochothrix thermosphacta\n")
            bactTypeList = np.array(bactType.split(" "))
            bactTypeList = bactTypeList.astype(float)
            #Check if each element in the 3rd column of the data are in the list of chosen types, save a copy of the list with true/false values for each of the elements based on whether they were chosen or not
            mask = np.isin(data[:,2], bactTypeList)
            #Save the rows of data with true values in the mask-list, remove the rows with false values, print that the filter was applied
            data = data[mask]
            print("Your data has been filtered successfully.")
        elif int(filterInput) == 2:
            #If the user chose to filter the data by a growth rate interval, get their input on what interval should be included, put the lower and upper bound into a list
            growthInterval = input("What are the lower and upper bound for the Growth rate you want to see? Choose by writing the numbers seperated by a space, decimals are set with a dot (.).\n")
            growthIntervalList = np.array(growthInterval.split(" "))
            growthIntervalList = growthIntervalList.astype(float)
            #Save the rows of data with values in the second column between the bounds of the interval, remove the other rows, print that the filter was applied
            data = data[:][(data[:,1] >= growthIntervalList[0]) & (data[:,1] <= growthIntervalList[1])]
            print("Your data has been filtered successfully.")
        elif int(filterInput) == 3:
            #If the user chose to filter the data by a temperature interval, get their input on what interval should be included, put the lower and upper bound into a list
            tempInterval = input("What are the lower and upper bound for the Temperature you want to see? Choose by writing the numbers seperated by a space, decimals are set with a dot (.).\n")
            tempIntervalList = np.array(tempInterval.split(" "))
            tempIntervalList = tempIntervalList.astype(float)
            #Save the rows of data with values in the first column between the bounds of the interval, remove the other rows, print that the filter was applied
            data = data[:][(data[:,0] >= tempIntervalList[0]) & (data[:,0] <= tempIntervalList[1])]
            print("Your data has been filtered successfully.")
        else:
            #If their choice was another integer than 1-3, print invalid input, give a choice to try again
            inp = input("Invalid input. Would you like to try again? (y/n)\n")
            if inp.casefold() == "y":
                data = filter(data)
    except:
        #If any of the inputs were formatted incorrectly, catch the resulting error, and print invalid input, give a choice to try again
        inp = input("Invalid input. Would you like to try again? (y/n)\n")
        if inp.casefold() == "y":
            data = filter(data)
    #Return the filtered (or unfiltered) data
    return data

#This method tries to use the dataLoad method, and in case the user doesnt give a suitable input, catch the error
def tryLoad():
    #Get the users input
    filename = input("Please input the filename including .txt (ex. file.txt):\n")
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

#This method tries to use the dataStatistics method, and in case the user doesnt give a suitable input, catch the error
def tryStats(data):
    #Get the users input, make a list with the statistic names
    inp = input("Please input the statistic you want to have calculated by entering the corresponding number. Your options are as follows:\n1. Mean Temperature.\n2. Mean Growth rate.\n3. Standard deviation of Temperature.\n4. Standard deviation of Growth rate.\n5. Number of samples.\n6. Mean Growth rate for cold samples.\n7. Mean Growth rate for hot samples.\n")
    statistics = ["Mean Temperature", "Mean Growth rate", "Std Temperature", "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"]
    #Try to get the statistic based on the input, and print it out if it works
    try:
        print(str(dataStatistics(data, f"{statistics[int(inp)-1]}")) + " is the computed " + str(statistics[int(inp)-1]) + "\n")
    except:
        #In case it doesnt work, print that the input was ineligible, and an option to give another input
        inp = input("Ineligible input or missing dataset. Would you like to try again? (y/n)\n") 
        if inp.casefold() == "y":
            tryStats(data)

    

#Old function to make the interface before we read that the interface couldn't be made as a function.
def menu(data):
    choice = input("Please choose one of the following options by entering its corresponding number:\n1. Load data\n2. Filter data\n3. Display statistics\n4. Generate plots\n5. Quit\n")
    if choice == "1":
        data = tryLoad()
        menu(data)
    if choice == "2":
        data = filter(data)
        menu(data)
    if choice == "3":
        tryStats(data)
        menu(data)
    if choice == "4":
        try:
            dataPlot(data)
            menu(data)
        except:
            print("No eligible data to plot, please load data first.\n")
            menu(data)
    else:
        return


#Main Script, only runs if the file is run directly, this isn't executed if the file is imported to use as a library
if __name__ == '__main__':
    #Create empty array to store data in
    data = np.empty((0,3))
    #While loop to make sure the user returns to the menu of the interface
    while True:
        #Get the users input on what they want the program to do
        choice = input("\nPlease choose one of the following options by entering its corresponding number:\n1. Load data\n2. Filter data\n3. Display statistics\n4. Generate plots\n5. Quit\n")
        if choice == "1":
            #If they want to load data into the data, call the tryLoad method, save the returned data in the data variable
            data = tryLoad()
        elif choice == "2":
            #If they want to filter the data, call the filter method with data as parameter, save the returned data in the data variable
            data = filter(data)
        elif choice == "3":
            #If they want to compute stats based on the data, call the tryStats method with data as a parameter
            tryStats(data)
        elif choice == "4":
            #If they want to plot the data, try to call the dataPlot method with data as a parameter
            try:
                dataPlot(data)
            except:
                #This throws an exception if the data variable doesn't contain any data, and in that case, print that there are no eligible data to plot
                print("No eligible data to plot, please load data first.\n")
        elif choice == "5":
            #If they want to quit the program, break the while-loop
            break
        else:
            #If none of the given options were chosen as an input, print that they gave an ineligible input
            print("Ineligible input, please try again.")