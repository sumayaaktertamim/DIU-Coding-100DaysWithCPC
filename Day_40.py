
#puzzels-900

    
    
#  type-1   
    
n,m = map(int,input().split())
f = list(map(int,input().split()))

f.sort()  

arr = []  

for i in range(m - n + 1):
    diff = f[i + n - 1] - f[i]
    arr.append(diff) 

print(min(arr))  




# type-2

n,m = map(int,input().split())
f = list(map(int,input().split()))

f.sort()  
min_diff = 10000  

for i in range(m - n + 1):
    diff = f[i + n - 1] - f[i]  
    if diff < min_diff:
        min_diff = diff

print(min_diff)

    
    
    