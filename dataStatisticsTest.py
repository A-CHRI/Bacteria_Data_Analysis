import numpy as np

def dataStatistics(data, statistic):
    if statistic == "Mean Temperature":
        sum = 0
        count = 0
        for x in data:
            sum += float(x[0])
            count += 1
        return sum / count

    if statistic == "Mean Growth Rate":
        sum = 0
        count = 0
        for x in data:
            sum += float(x[1])
            count += 1
        return sum / count

    if statistic == "Std Temperature":
        sum = 0
        total = 0
        for x in data:
            sum += (float(x[0]) - dataStatistics(data, "Mean Temperature"))**2
            total += 1
        return math.sqrt(sum / total)

    if statistic == "Std Growth Rate":
        sum = 0
        total = 0
        for x in data:
            sum += (float(x[1]) - dataStatistics(data, "Mean Growth Rate"))**2
            total += 1
        return math.sqrt(sum / total)

    if statistic == "Rows":
        count = 0
        for x in data:
            count += 1
        return count

    if statistic == "Mean Cold Growth Rate":
        sum = 0
        count = 0
        for x in data:
            if float(x[0]) < 20:
                sum += float(x[1])
                count += 1
        if count > 0: return sum / count
        else: return 0

    if statistic == "Mean Hot Growth Rate":
        sum = 0
        count = 0
        for x in data:
            if float(x[0]) > 50:
                sum += float(x[1])
                count += 1
        if count > 0: return sum / count
        else: return 0

data = np.array([[25., 0.109, 1.], [20., 0.096, 2.], [15., 0.517, 3.], [35., 1.086, 4.], [40., 0.934, 2.], [35., 0.109, 1.], [15., 0.123, 4.]])