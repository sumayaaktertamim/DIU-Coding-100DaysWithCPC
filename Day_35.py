# A. Keyboard-900
direction = input()
k = input()
 
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
result = ""
 
for ch in k:
    a = keyboard.index(ch)
    if direction == 'L':
        result += keyboard[a+1]
    else:
        result += keyboard[a-1]
 
print(result)   
        
        
                                                                                                                                                                                
    
    
        
    
      
