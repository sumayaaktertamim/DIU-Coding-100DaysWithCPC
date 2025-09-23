# presents-800
 
n = int(input())
g = list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(n):  
        if g[j] == i:     
            print(j+1, end=" ")