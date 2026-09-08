class Car:
  def __init__(self, type, price, color):
  self.type = type
  self.price = price
  self.color = color
  self.__speed = 0

  def accelerate(self):
    self.__speed += 10

  def brake(self):
    if self.__speed >= 10
      self.__speed -= 10

  def get_speed(self):
    return self.__speed
    
Car1 = (Toyata, 500000, Red)
Car2 = (Tesla, 10000000, Silver)
Car3 = (Ford, 750000, Yellow)
Car4 = (BMW, 1000000, Black)

Car1.accelerate()
Car1.accelerate()
Car1.accelerate()

Car2.accelerate()
Car2.accelerate()

Car3.accelerate()
Car3.accelerate()
Car3.accelerate()
Car3.accelerate()
Car3.accelerate()

Car4.accelerate()

print(Car1.brand, Car1.price, Car1.color, Car1.get_speed())
print(Car2.brand, Car2.price, Car2.color, Car2.get_speed())
print(Car3.brand, Car3.price, Car3.color, Car3.get_speed())
print(Car4.brand, Car4.price, Car4.color, Car4.get_speed())
