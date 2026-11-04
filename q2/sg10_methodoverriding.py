class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self): #Defines the eat method for the parent class
        print(f"{self.name} is eating.")
        
    def make_sound(self): #Defines the make_sound method for the parent class
        print("")
        
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name) #Initializes the constructor of the parent class to add the name attribute
        
    def make_sound(self): #Adds the make_sound method for the child class to make it different from the parent class
        print("The lion roars loudly.")
        
    def eat(self): #Overrides and adds the modified eat method for the Lion class
        print("The lion eats fresh meat.")
        
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name) #Initializes the constructor of the parent class to add the name attribute
        
    def make_sound(self): #Adds the make_sound method for the child class to make it different from the parent class
        print("The elephant trumpets.")
        
    def eat(self): #Overrides and adds the modified eat method for the Elephant class
        print("The elephant eats grass and fruits.")
        
class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name) #Initializes the constructor of the parent class to add the name attribute
        
    def make_sound(self): #Adds the make_sound method for the child class to make it different from the parent class
        print("The monkey chatters.")
        
    def eat(self): #Overrides the eat method for the Monkey class
        print("The monkey eats bananas.")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("---------------")

print(elephant.make_sound())
print(elephant.eat())
print("---------------")

print(monkey.make_sound())
print(monkey.eat())
print("---------------")
