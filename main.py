import os
os.system('cls')

class Animal:
    def eat(self):
        print("Animal is eating!")
    
    def run(self):
        print("Animal is running!")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog1 = Dog()
cat1 = Cat()

# dog1.eat()
# dog1.run()

cat1.eat()