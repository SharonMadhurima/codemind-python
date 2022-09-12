n=int(input())
s=0
for i in range( n):
    if n>9: 
        r=n%10
        n=n//10+r
print(n)
