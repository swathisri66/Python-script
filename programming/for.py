A = [0,1,2,3,4,5] #list
B = (0,1,2,3,4,5) #tuple
C = {0,1,2,3,4,5} #set
D = '012345' #string
E = {"name":"swathi", "age":36, "year": 1984}

for x in E.values():
    print(x)

for x in E.keys():
    print(x)
    
for key, value in E.items():
    print(key, ' ', value)
    
for x in range(6):
    print(x)
    
for x in E.range(2,6):
    print(x)
    
for x in E.range(2,30,3):
    print(x)
