import math
X,Y,M=map(int,input().split())
a=math.pow(X,Y)
b=a%M
print(int(b))