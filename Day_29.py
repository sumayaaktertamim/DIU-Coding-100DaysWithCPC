# A. I Wanna Be the Guy-800
n = int(input())
Lx = list(map(int, input().split()))[1:]   
Ly = list(map(int, input().split()))[1:] 
sum_set = set(Lx + Ly)
if len(sum_set) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")