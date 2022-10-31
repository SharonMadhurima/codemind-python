n=int(input())
max=0
while(n>0):
    a=n%10
    if(max<a):
        max=a
    n=n//10
print(max)
    