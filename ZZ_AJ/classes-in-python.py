# example of classes in python

# define the class
class Animal:
    def __init__(self, name): # constructor
        self.name = name
    
    def sleep(self):
        print(self.name + " is sleeping")
        
# create a new object 
cat = Animal("Kitty")
cat.sleep()

# inheritance
class Cat(Animal):
    def meow (self):
        print(self.name + " is meowing")
cat = Cat("Kitty")
cat.meow()
cat.sleep()
