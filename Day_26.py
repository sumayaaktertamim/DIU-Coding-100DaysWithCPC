# A. Pangram-800
n=int(input())
string=input()
s= set(string.upper()) #lower() use kora jabe
if len (s)==26:
   print("YES")
else:
    print("NO")