from dataLoadTest import dataLoad
import numpy as np

# Creates a list for the different filters, and creates a list of the different applied filters
filters = ["Bacteria", "Temperature", "Growth rate"]
appliedFilters = []

# Creates a list of the different bacteria, and creates a list of the different applied bacteria filters
bacteria = ["Salmonella enterica", "Bascillus cereus", "Listeria", "Brochothrix thermosphacta"]
appliedBacteria = []

# Functions for the various filters
def temperatureFilter(data):
    while True:
        # Creates a seperator for the layout
        print("\n---------------------------------------")
        # Prompts the user to enter the temperature range
        print("\nPlease enter the temperature range you would like to filter by, and enter 'done' to continue")
        tempMin = input("\nMinimum Temperature: ")
        tempMax = input("Maximum Temperature: ")
        if tempMin == "done" or tempMax == "done":
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
    data = data[data[:,2].astype(float) >= tempMin]
    data = data[data[:,2].astype(float) <= tempMax]
    print("\nSuccesfully applied the filter.")
    return data

def bacteriaFilter(data):
    while True:
        # Creates a seperator for the layout
        print("\n---------------------------------------")
        # Prompts the user to apply or unapply the varous filters
        print("\nYou are about to filter the following bacteria:")
        if len(appliedBacteria) > 0:
            for i,v in enumerate(appliedBacteria):
                print(i+1, ":", v)
        else:
            print("None")

        print("\nPlease enter the bacteria you would like to add or remove from the filter, and enter 'done' to continue (Choose by entering the corresponding number)")
        for i,v in enumerate(bacteria):
            print(i+1, ":", v)

        inp = input("\nBacteria: ")
        if inp == "done":
            print("\nThe filter has been applied")
            break

        if inp in ["1","2","3","4"]:
            intc = int(inp) - 1
            if bacteria[intc] in appliedBacteria:
                appliedBacteria.remove(bacteria[intc])
                print("\nRemoved bacteria filter for", bacteria[intc])
            else:
                appliedBacteria.append(bacteria[intc])
                print("\nAdded bacteira filter for", bacteria[intc])
        
    bactNumbs = []
    for i in appliedBacteria:
        bactNumbs.append(bacteria.index(i))

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
        if growthMin == "done" or growthMax == "done":
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
        if inp == "done":
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
    else:
        print("No filters was applied.")

    # Returns the filtered data
    return data

# ----------------------------------------------------------------------------------------------------------------------

data = dataLoad("fil.txt")
print(filter(data))