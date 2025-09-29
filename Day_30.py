# A. Hit the Lottery-800
# n = int(input())

# a = n // 100
# n = n % 100    

# b = n // 20
# n = n % 20

# c = n // 10
# n = n % 10

# d = n // 5
# n = n % 5

# e = n // 1
# n = n % 1

# total = a + b + c + d + e
# print(total)

# type-2 
n=int(input())
total=0
m=[100,20,10,5,1]
for i in range(5):
    total+=n//m[i]
    n=n%m[i]
    
print(total)

