class Vehicle:
    def __init__(self, length):
        self.time = length
class Bus(Vehicle):
    def __init__(self, length):
        self.price = 100
        Vehicle.__init__(self, length)
    def display(self):
        print(self.price * self.time, "tk")
length = int(input("Enter length of ride (in hours): "))
bus = Bus(length)
bus.display()