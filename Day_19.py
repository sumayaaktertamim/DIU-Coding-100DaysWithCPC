# A. Vanya and Fence-800
n,h= map(int,input().split())
hight=list(map(int,input().split()))
width=0
for i in range(n):
    if hight[i]<=h:
       width+=1
    elif hight[i]>h:
       width+=2
print(width) 
     
     
     
     