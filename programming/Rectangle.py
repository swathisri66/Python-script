class Rectangle:
    pass

rect1 = Rectangle()
rect2 = Rectangle()

rect1.height = 20
rect1.weight = 20

rect2.height = 30
rect2.weight = 30

print("area of rect1", rect1.height * rect1.weight)
print("area of rect2", rect2.height * rect2.weight)



#example of class, object, attribute 2

class Car:
    pass

Ford = Car()
Honda = Car()

Ford.color = 'red'
Honda.color ='blue'

Ford.speed = 250
Honda.speed = 300

print(Ford.color)
print(Honda.speed)
