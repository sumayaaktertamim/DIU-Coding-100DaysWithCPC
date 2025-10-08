# B. Chemistry-900
t=int(input())
count=0
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    b=s.replace(s[i],"",1)
    for ch in set(s):
        c=s.count(ch)
        if c%2==0 and c==1:
            print("YES")
        else:
            print("NO")
            
# type-2

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    s = input()

    a = 0
    for ch in set(s):
        if s.count(ch) % 2 != 0:
            a += 1    
    if k >= a - 1:
        print("YES")
    else:
        print("NO")
        