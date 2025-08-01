
def calculateStats(numbers):
    l = len(numbers)
    compStats = {}
    if l == 0:
        compStats['avg'] = float('nan')
        compStats['min'] = float('nan')
        compStats['max'] = float('nan')
    else:
        minimum = sys.maxsize
        maximum = -sys.maxsize
        summation = 0
        average = 0
        for i in range(l):
            num = numbers[i]
            summation += num
            if num < minimum:
                minimum = num
            elif num > maximum:
                maximum = num
        compStats['avg'] = summation/l
        compStats['min'] = minimum
        compStats['max'] = maximum     
    return compStats
