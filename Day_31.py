# A. Football-900
# n=input()
# if "1111111"  in n or "0000000" in n:
#     print("YES")
# else:
#     print("NO")
    
# type-2

    
n = input()  # ইনপুট স্ট্রিং

count = 1    # টানা একই সংখ্যার কাউন্টার, প্রথমটি 1 ধরে নিই
danger = False

for i in range(1, len(n)):
    if n[i] == n[i-1]:   # আগের ক্যারেক্টারের সাথে মিল
        count += 1
        if count == 7:   # টানা ৭ হয়ে গেলে
            danger = True
            break
    else:
        count = 1        # ভিন্ন হলে কাউন্টার রিসেট

if danger:
    print("YES")
else:
    print("NO")