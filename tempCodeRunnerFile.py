    b=int(input())
    if b>=0:
        print(b)
    else:
        s=str(b)
        p1=int(s[:-1])
        p2=int(s[:-2] + s[-1])
        print(max(p1,p2))