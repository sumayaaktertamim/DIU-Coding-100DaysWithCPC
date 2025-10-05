# B. Chemistry-900
t=int(input())
count=0
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    b=s.replace(s[i],"",1)
    for ch in b:
        c=s.index(ch)
        if c%2==0 and c==1:
            print("YES")
        else:
            print("NO")
            
# type-2
t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    s = input()

    odd = 0
    for ch in set(s):
        if s.count(ch) % 2 != 0:
            odd += 1

    # এখানে k টা অক্ষর remove করে palindrome করা সম্ভব কিনা দেখি
    if k >= odd - 1:
        print("YES")
    else:
        print("NO")
        