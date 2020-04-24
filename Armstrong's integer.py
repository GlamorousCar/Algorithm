#This program calculates all Armstrong numbers at a given interval
a,b =input("Please input interval").split(' ')
a,b = int(a),int(b)
s = 0
j = 0
for i in  range(a,b):
    f = len(str(i))
    l = i
    while l!=0:
        p = l%10
        s+=p**f
        l = l//10
    if s == i:
        print(i)
    else:
        j +=1
    s = 0
if b-a == j:
    print(-1)
