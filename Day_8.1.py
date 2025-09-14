# sum-800
n=int(input())

for i in range(n):
      a,b,c=map(int,input().split())

      if  a+b==c or b+c==a or a+c==b:
            print("YES")
      else:
            print("NO")