#Object orientation in python

#class an object 
class Animal:
    #intialise with parameter
    def __init__(self,name):
        self.name = name
    #parent method   
    def eat(self,food):
        self.food = food
        print("eating "+ food)
#creating object form parent      
dog = Animal("ruby")
dog.eat("roti")


#abstraction
'''
A class abstracts the real-world entity it represents, 
focusing on essential properties and behaviors while hiding the implementation details.
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Usage
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


#Encapsulation
'''
Encapsulation involves bundling data (attributes) and methods that operate on the data within a class.
'''
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Encapsulation

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

#Polymorphism compile time
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Usage
math_ops = MathOperations()
print(math_ops.add(2, 3))      # Calls the second add method
print(math_ops.add(2, 3, 4))   # Calls the third add method

#Polymorphism run-time
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Calls Dog's make_sound method
print(cat.make_sound())  # Calls Cat's make_sound method

#Access modifiers in python

class MyClass:
    def __init__(self):
        #public
        self.public_attribute = "I'm public"

    def public_method(self):
        return "This is a public method"

obj = MyClass()
print(obj.public_attribute)
print(obj.public_method())
 
 
#protected
class MyClass:
    def __init__(self):
        #protected
        self._protected_attribute = "I'm protected"

    def _protected_method(self):
        return "This is a protected method"

#private
class MyClass:
    def __init__(self):
        self.__private_attribute = "I'm private"

    def __private_method(self):
        return "This is a private method"

