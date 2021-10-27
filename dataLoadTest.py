import numpy as np

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

print(dataLoad("fil.txt"))