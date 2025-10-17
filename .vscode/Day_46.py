
# A. Candies-900
t = int(input())
for i in range(t):
    n = int(input())
    k = 2
    while True:
        if n % (2**k - 1) == 0:
            x = n // (2**k - 1)
            print(x)
            break
        k += 1