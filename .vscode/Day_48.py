# B. Two-gram-900
n= int(input())
s=input()

max_count = 0

for i in range(n-1):
    s1 = s[i] + s[i+1]
    count = 0
    for j in range(n-1):
        if s[j] + s[j+1] == s1:
            count += 1

    if count > max_count:
        max_count = count
        ans = s1

print(ans)
