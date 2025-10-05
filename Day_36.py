# A. Game With Sticks-900
# type-1
n,m=map(int,input().split())
if n>m:
    count=m
    if count%2==0:
        print("Malvika")
    else:
        print("Akshat")
else:
    count=n
    if count%2==0:
        print("Malvika")
    else:
        print("Akshat")
# type-2
    
n,m=map(int,input().split())
count=min(n,m)
if count%2==0:
    print("Malvika")
else:
    print("Akshat")