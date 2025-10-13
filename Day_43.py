# Ilya and Bank Account-900

b=input()

if int(b)>=0 :
    print(int(b))
else:
        if int(b[-1]) > int(b[-2]):
            print(int(b[:-1]))
            
        else:
            print(int(b[:-2]+ b[-1]))
       
# type-2
n = int(input())

if n >= 0:
    print(n)
else:
    s = str(n)               
    option1 = int(s[:-1])        
    option2 = int(s[:-2] + s[-1])  
    print(max(option1, option2)) 