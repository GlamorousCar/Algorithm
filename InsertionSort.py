import random
a, b, s = 0, 100, 10
array = [random. randint (a, b) for _ in range (s)]

def InsertionSort(array):
    for i in range(2,len(array)):
        key = array[i]
        k = i - 1
        while k > 0 and array[k] > key:
            array[k+1] = array[k]
            k = k - 1
        array[k+1] = key
    return array
print(array)
print(InsertionSort(array))