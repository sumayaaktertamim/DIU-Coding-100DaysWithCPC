# # A. Odd Divisor -900

# type-1
t=int(input())
for i in range(t):
    
    n=int(input())
    
    if n & (n-1)==0:
        print("NO")
    else:
        print("YES")
        
# type-2

t=int(input()) # ei problem ta thik moto kaj kore na timie limit  error dekhay but code thik ache

for i in range(t):
    
    n=int(input())
    a=1
    if n%2 !=0 :
           a=i
        
    if a>1:
        print("YES")
    else:
        print("NO")
        