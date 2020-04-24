import math
def f(x):
    return x * x
def f2(x):
    return 0
def area(a , b , h):
    s = 0
    x = 0
    while x < b:
        s = s + f(x) - f2(x) + f(x+h) - f2(x+h)
        x = x + h
    s = h*s / 2
    return s
print(area(0,10,1))
