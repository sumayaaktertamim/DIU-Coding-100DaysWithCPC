# bit++ prblm-800
n=int(input())
x=0
for i in range(n):
     i=input()
     if i=="X++" or i=="++X":
        x+=1
    
     elif i=="X--" or i== "--X":
      x-=1
     
print(x)