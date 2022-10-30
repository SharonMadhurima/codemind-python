a,b=map(int,input().split())
greater=a if a >b else b

while(1):
    if (greater%a==0) and (greater%b==0):
        break 
    greater+=1
    
print(greater)