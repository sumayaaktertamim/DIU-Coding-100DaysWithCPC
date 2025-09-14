# A. Next Round(codeforces-800 rate prblm)
n,k= map(int,input().split())
s= list(map(int,input().split()))
total=0
for i in range(n):
    if s[i] >=s[k-1] and s[i]>0:
        total+=1
print(total)
       
   