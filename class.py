class Car:
    def __init__(self,color,speed,model):
        self.color = color
        self.speed = speed
        self.model = model
    def start(self):
        print("The car has started.")
    def accelerate(self,value):
        print("Cars acceleration is: ", value)

car1 = Car("blue",68,"a1")
print(car1.model)
car1.start()
car1.accelerate(5)