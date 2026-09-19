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
        check = random.randint(1,20)

    if chance <= self.__luck:
        return True
    else:
        return False
  
    def get_luck(self, car):
        return self.__luck

    def add_cars(self):
        self.cars.append(car)
        car.driver = self

    def display_info(self)
        print("Race:", self.race)
        print("Condition:", self.condition)
        print("Clothing:", self.clothing)
        print("Crash Chance:", self.__luck, "/20 rating")
        print("Cars:")

        for car in self.cars:
            print(car.brand, car.color)

driver1 = Driver("Human", "Healthy", "Racing Suit")
