import random
def MergeSort(spisok):
    if len(spisok) <= 1:
        return (spisok)
    midl = int(len(spisok) / 2)
    left = MergeSort(spisok[:midl])
    right = MergeSort(spisok[midl:])
    return merge(left, right)
def merge(left, right):
    res = []
    while int(len(left))> 0 and int(len(right)) > 0:
        if int(left[0]) > int(right[0]):
            res.append(int(left[0]))
            left = left[1:]
        else:
            res. append(int(right[0]))
            right = right[1:]
    if len(left) > 0:
        res += left
    if len(right):
        res += right
    return res
a, b, s = 0, 100, 30
list_a = [random. randint (a, b) for _ in range (s)]
print("Список до сортировки ---->", list_a)
print("Список после сортировки---->", MergeSort(list_a))