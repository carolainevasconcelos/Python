def MinMax(temperatura):
    print("A menor temperatura do mes foi: ", minima(temperatura), "C.")
    print("A maior temperatura do mes foi: ", maxima(temperatura), "C.")

def minima(temps):
    min = 0
    i = 0
    while i < len(temps):
        if temps[i] > min:
            min = temps[i]
        i = i + 1
    return min

def maxima(temps):
    max = 0
    i = 0
    while i < len(temps):
        if temps[i] < max:
            max = temps[i]
        i = i + 1
    return max