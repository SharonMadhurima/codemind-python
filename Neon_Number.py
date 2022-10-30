a=int(input())
b=a*a
s1=0
while(b>0):
    s1=s1+b%10
    b=b//10
if (a==s1):
    print("Neon Number")
else:
    print("Not Neon Number")