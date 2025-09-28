# A. Anton and Letters-800
# type-1
L=input()

s=L.replace("{", "").replace(",","").replace("}","").replace(" ", "")

print(len(s))

# type-2

l=input()
s=l[1:-1].replace(",", "").replace(" ", "")
print(len(s))