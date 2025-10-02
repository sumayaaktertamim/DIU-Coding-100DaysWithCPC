# A. Even Odds-900
n,k=map(int,input().split())

if n%2==0:
    a=n//2
else:
    a=(n+1)//2
if k<= a :
    print((k*2)-1)
else:
    print((k-a)*2)
    
    
    
    