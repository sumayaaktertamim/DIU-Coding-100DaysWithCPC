# B. Chemistry-900
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
        