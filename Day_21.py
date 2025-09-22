# Drinks-800
n= int(input())
x=list(map(int,input().split()))
total=(sum(x))/n
print(total)

# type-2

n = int(input())                     
x = list(map(int, input().split()))  
total = 0                           
for i in range(n):                   
    total += x[i]                    

Mean = total / n                  
print(Mean)