# define the class 
class Animal: 
    def __init__(self, name):
        self.name = name 

    def sleep(self):
        print(self.name + ' is sleeping')

# create a new object
cat = Animal('Kitty')
cat.sleep()

class Cat(Animal):
    def meow(self):
        print(self.name + ' says "meow"')   
cat = Cat('Kitty')
cat.meow()
cat.sleep()