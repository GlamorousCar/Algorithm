def BinaryExponentiation(a,n):
    if n == 0:
        return 1
    if n%2 == 1:
        return BinaryExponentiation(a, n-1) * a
    else:
        b = BinaryExponentiation(a,n/2)
        return b * b
a,b = input("Please input the number and extent").split()
print(BinaryExponentiation(a,b))

