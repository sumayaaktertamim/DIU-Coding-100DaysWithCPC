# B. New Year's Number-900

t=int(input())
for i in range(t):
    n=int(input())
    if n%2020 <= n//2020:
        print("YES")
    else:
        print("NO")