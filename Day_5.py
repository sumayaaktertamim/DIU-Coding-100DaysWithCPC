n= int(input())
total =0
for i  in range (n):
     a= input()

     if a.count("1") >=2:
          total= total+1
          
print (total)