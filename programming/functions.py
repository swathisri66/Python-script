#group of statements
#built in functions - built, input, min
#user defined function

def sum(arg1, arg2):
    print(arg1 + arg2)
    
sum(15, 8)    
sum('Hello ','world')   
sum(87.9, 78.9) 

def sum(arg1, arg2):
    if type(arg1) != type(arg2):
       print("Please give the args of same type")
       return
    return(arg1 + arg2)
    
a = sum(15, 8)    
print(a)
print(sum('Hello ','world'))   
print(sum(87.9, 78.9) )
print(sum('Hello', 7))
