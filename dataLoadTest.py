import numpy as np

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

print(dataLoad("fil.txt"))