class Car:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
        self.__speed = 0

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        if self.__speed >= 10:
            self.__speed -= 10

    def get_speed(self):
        return self.__speed

Car1 = Car("Toyota", 1200000, "Red")
Car2 = Car("Honda", 1500000, "Blue")
Car3 = Car("Ford", 2500000, "Black")
Car4 = Car("BMW", 4000000, "White")
Car5 = Car("Tesla", 3000000, "Silver")

Car1.accelerate()
Car1.accelerate()

Car2.accelerate()

Car3.accelerate()
Car3.accelerate()
Car3.accelerate()

Car4.accelerate()

Car5.accelerate()
Car5.accelerate()

print(Car1.brand, Car1.price, Car1.color, Car1.get_speed())
print(Car2.brand, Car2.price, Car2.color, Car2.get_speed())
print(Car3.brand, Car3.price, Car3.color, Car3.get_speed())
print(Car4.brand, Car4.price, Car4.color, Car4.get_speed())
print(Car5.brand, Car5.price, Car5.color, Car5.get_speed())

##Credits to Ethan Solano for helping me understand the basic concepts.
