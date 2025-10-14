# B. Sale-900

n,m=map(int,input().split())
price=list(map(int,input().split()))
count=0
total=0
for p in sorted(price):

    if p<0 and count<m :
        total+= abs(p)
        count+=1
    
        
print(total)
