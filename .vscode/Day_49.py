# A. Business trip-900

k = int(input())
a = list(map(int, input().split()))

if k == 0:
    print(0)
else:
    a.sort(reverse=True)
    total = 0
    count = 0
    for i in a:
        total += i
        count += 1
        if total >= k:
            print(count)
            break
    else:
        print(-1)