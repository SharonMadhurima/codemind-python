n=int(input())
s1=0
s2=1
while(n!=0):
    r=n%10
    s1=s1+r
    s2=s2*r
    n=n//10
if (s1==s2):
    print("Spy Number")
else:    
    print("Not Spy Number")