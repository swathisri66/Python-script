#elif

name = input("enter a name:") 

if name == "Swathi":
    print("Name Entered is :", name)
elif name == "Capricon":
    print("Name Entered is: ", name)
elif name == "Kamani":
    print("Name Entered is:", name)
else: 
    print("The name entered is invalid")
    
    
#nested if

x = 10

if x < 0:
    print("x is negative")
else:
    print("x is positive")
    if (x%2) == 0:
        print("x is even")
    else:
        print("x is odd")
    
    
    
