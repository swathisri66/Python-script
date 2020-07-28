def student (name, age, **marks):
    print("name:", name)
    print("age:", age)
    for x in marks:
        print(x)
    print("marks:", marks)
    
student('swathi', 36, biology= 48, Maths= 89, Science= 98)    

#can also add key and value 
def student (name, age, **marks):
    print("name:", name)
    print("age:", age)
    for key, value in marks.items():
        print(key, ' ', value)
            
student('swathi', 36, biology= 48, Maths= 89, Science= 98)    
