import random

class Car:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
        self.__speed = 0
        self.driver = None

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        if self.__speed >= 10:
            self.__speed -= 10

    def get_speed(self):
        return self.__speed


class Driver:
    def __init__(self, race, condition, clothing):
        self.race = race
        self.condition = condition
        self.clothing = clothing
        self.__luck = 0
        self.cars = []

    def luck(self):
        self.__luck += 3

    def check_crash(self):
        chance = random.randint(1, 20)

        if chance <= self.__luck:
            return True
        else:
            return False

    def get_luck(self):
        return self.__luck

    def add_car(self, car):
        self.cars.append(car)
        car.driver = self

    def display_info(self):
        print("Race:", self.race)
        print("Condition:", self.condition)
        print("Clothing:", self.clothing)
        print("Crash Chance:", self.__luck, "/20 rating")
        print("Cars:")

        for car in self.cars:
            print(car.brand, car.color)


driver1 = Driver("Human", "Healthy", "Racing Suit")

car1 = Car("Toyota", 1200000, "Red")
car2 = Car("Honda", 1500000, "Blue")
car3 = Car("Ford", 2500000, "Black")
car4 = Car("BMW", 4000000, "White")
car5 = Car("Tesla", 3000000, "Silver")


driver1.add_car(car1)
driver1.add_car(car2)
driver1.add_car(car3)
driver1.add_car(car4)
driver1.add_car(car5)

print("Cars connected")

driver1.display_info()


for car in driver1.cars:
    print(
        car.brand,
        "Price:", car.price,
        "Color:", car.color,
        "Speed:", car.get_speed(),
        "Driver Race:", car.driver.race,
    )

driver1.luck()

print("Updated Crash Chance:", driver1.get_luck(), "/20 rating")

if driver1.check_crash():
    print("The driver crashed!")
else:
    print("The driver did not crash.")

# Needed research for random int (https://www.geeksforgeeks.org/python/python-random-module/)
# Needed research for connecting classes mainly from (https://stackoverflow.com/questions/75256287/create-a-link-between-2-classes)
