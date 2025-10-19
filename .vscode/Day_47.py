# A. Vasya and Socks-900
# type -1
n,m=map(int,input().split())


days = 0  
socks = n 

while socks > 0:
    days += 1     
    socks -= 1  

    if days % m == 0:  
        socks += 1     

print(days)

# type-2
n, m = map(int, input().split())

days = 0
socks = n

for day in range(1, 1000):  # 1000 শুধু একটা বড় সংখ্যা, লুপ থামবে যখন socks শেষ হবে
    if socks == 0:
        break  # মোজা শেষ হয়ে গেলে লুপ বন্ধ
    
    days += 1      # একদিন কেটে গেল
    socks -= 1     # একজোড়া মোজা ব্যবহার হলো

    if days % m == 0:
        socks += 1  # মা নতুন মোজা কিনে দিলেন

print(days)
