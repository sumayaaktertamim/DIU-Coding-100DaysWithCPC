# A. Magic Numbers-900

n = input()
i = 0
ok = True
 
while i < len(n):
    if n[i:i+3] == "144":
        i += 3
    elif n[i:i+2] == "14":
        i += 2
    elif n[i:i+1] == "1":
        i += 1
    else:
        ok = False
        break
 
if ok:
    print("YES")
else:
    print("NO")