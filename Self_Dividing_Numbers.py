a=int(input())
b=int(input())
l=[]
for i in range (a,b+1):
    if i<=9:
        l.append(i)
    elif i>=10 and i%10!=0:
        c=str(i)
        cnt=0
        for j in c:
            if i%int(j)==0:
                cnt+=1
        if len(c)==cnt:
            l.append(i)
print(*l)