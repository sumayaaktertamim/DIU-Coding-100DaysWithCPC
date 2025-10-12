
# B. Multiply by 2, divide by 6-900



t = int(input())

for i in range(t):
    n = int(input())
    moves = 0

    while n != 1:
        if n % 6 == 0:
            n = n//6
            moves += 1
        else:
            n =n  * 2
            moves += 1
        
        if n > 10**18:
            moves = -1
            break

    if n == 1 :
        print(moves)
    else:
        print(-1)
