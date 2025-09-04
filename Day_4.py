y= int((input()))
while True:
    y=y+1
    if  len(str(y))== len(set(str(y))):
        print (y)
        break