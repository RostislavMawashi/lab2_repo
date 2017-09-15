def min(arr):
    my_min = float('Inf')
    for el in arr:
        if el < my_min:
            my_min = el
    return my_min

def average(arr):
    avrg = 0
    for el in arr:
        avrg += el
    avrg /= len(arr)
    return avrg

arr1 = [15, 50, 45, 23, 2, 45]
arr2 = range (10)
print (min(arr1))
print (average(arr2))