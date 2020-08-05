class Car:
    def __init__(self, speed, color):
        print('__init__')
        print(speed)
        print(color)


Ford = Car(200 , 'red')
Honda = Car(250, 'blue')

Ford.color = 'red'
Honda.color ='blue'

Ford.speed = 250
Honda.speed = 300

print(Ford.color)
print(Honda.speed)
