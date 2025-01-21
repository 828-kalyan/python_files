# class demo:
#     s = "hello world" #static variable (class levl variable)
#     def greet():  
#         print("hi")
#     def fun(self):
#         print("Hello")
# d = demo()
# print(demo.s)
# demo.greet()
# d.fun()
# print(d.s)

# class demo:
#     """this class demo """
#     def __init__(self):  #constructor is special method. its name is always __init__()
#         print("in init")
#         self.name = "kalyan"
    
# s = demo()
# print(demo.__doc__)

# class demo:
#     def __init__(self):   #constructor (first arugument to constructor is always self)
#         self.name = "kalyan" #instance variable (object level variable)
#         self.roll = 101
#     def show(self):      #instance method(first arugument to instance method is always self)
#         print(self.name)
#         print(self.roll) #we always use self to access intance variables

# s  = demo()
# s.show()
# print(s.name) #we use reference variable "s" to access instance variables in outside the class
# print(s.roll)

# class demo:
#     def __init__(self):
#         print(id(self)) #2609656797552
    
# d = demo()
# print(id(d)) #2609656797552 both same

# class demo:
#     def __init__(delf): #self is not keyword we can use name 
#         delf.name = "kalyan"

#     def fun(kelf): #self is not keyword we can use any thing
#         print(kelf.name)
# d= demo()
# d.fun()
    
# class demo:
#     def __init__(self): 
#         print("constructor")
# d = demo()
# d.__init__() #we can explicitly call constructor like normal method.
# d.__init__()
# d.__init__()
# d.__init__()

# class demo:
#     def __init__(self):
#         print("constructor")
#     def __init__(self,x):
#         print("new constructor")
# demo(1) #o/p: new constructor. because new constructor overrides old constructor. thre is no constructor overloading 

# Defining a class
# class Dog:
#     # Constructor method to initialize object properties
#     def __init__(self, name, age):
#         self.name = name  # Instance variable for the dog's name
#         self.age = age    # Instance variable for the dog's age

#     # Method to display dog's details
#     def bark(self):
#         print(f"{self.name} says Woof!")

# # Creating objects (instances) of the Dog class
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Bella", 5)

# # Accessing object properties and calling methods
# print(f"Dog 1: {dog1.name}, Age: {dog1.age}")
# dog1.bark()

# print(f"Dog 2: {dog2.name}, Age: {dog2.age}")
# dog2.bark()



# class movie:
#     def __init__(self,title,hero,heroine):
#         self.title = title
#         self.hero = hero
#         self.heroine = heroine

#     def show(self):
#         print("movie name",self.title)
#         print("Heo:",self.hero)
#         print("heroine:",self.heroine)

# lis = []
# while True:
#     title = input("enter movie name: ")
#     hero = input("Enter hero name: ")
#     heroine = input("Enter heroine name: ")
#     m = movie(title,hero,heroine)
#     lis.append(m)
#     choice = input("Do you want to add another 'y' or 'n': ")
#     if choice == 'n':
#         break
# print(lis)
# for i in lis:
#     i.show()


#attribute(variables) 
# 1.instance variable
# 2. class variable
# 3.local variable

# methods
# 1.intance method
# 2. class method
# 3. static method

#1.instance variable and 1.instance method
# class dog:
#     def __init__(self,name,age):
#         self.name = name #instance variable
#         self.age = age   #instance variable
#     def description(self): 
#         print(f"the dog's name is {self.name} and age is {self.age}") # Instance method: Accessing instance attributes
#     def bark(self):
#         # Instance method: Accessing instance attributes
#         print(f"{self.name} says Woof!")

# d = dog("buddy", 3)
# # Accessing instance attributes and calling instance methods
# print(d.name)
# d.description()
# d.bark()

#Class Attributes and Class Methods
# class dog:
#     species = "golden retriver" #class varible
#     def __init__(self,name,age):
#         self.name = name #instance variable
#         self.age = age   #instance variable
#     def description(self): 
#         print(f"the dog's name is {self.name} and age is {self.age}") # Instance method: Accessing instance attributes
#     @classmethod
#     def info(cls):
#         print(f"the dog belons to {cls.species}") #Accessing class attributes
        

# d = dog("buddy", 3)
# # Accessing class attributes and calling class methods
# print(d.species) #with reference var
# print(dog.species) #with class 
# d.info()

#Static Methods and local variables
# class dog:
#     species = "golden retiver" #class varible
#     def __init__(self,name,age):
#         self.name = name #instance variable
#         self.age = age   #instance variable
#     def description(self): 
#         print(f"the dog's name is {self.name} and age is {self.age}") # Instance method: Accessing instance attributes
#     @classmethod
#     def info(cls):
#         print(f"the dog belons to {cls.species}") #Accessing class attributes
#     @staticmethod
#     def is_domestic(): #Static methods don’t take self or cls as their first parameter
#         x = 5      #local var
#         print(x)
#         print("yes, is domestic")
        

# d = dog("buddy", 3)
# # Calling a static method
# d.is_domestic()  

# Instance Attributes and Methods work on object-specific data
# Class Attributes and Methods work on class-level data and can be accessed through any instance of the class or directly via the class.
# Static Methods are independent of both instance and class and are used for general utility purposes.

# class Person:
#     def __init__(self, name, age):
#         self.name = name  # Public attribute
#         self.__age = age  # Private attribute

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

#     def get_age(self):
#         # Private method
#         return self.__age

# p = Person("Alice", 30)

# print(p.name)  

# # Accessing private attribute directly will result in an error
# # print(person.__age)  # This will raise an AttributeError

# # Calling private method directly will result in an error
# # print(person.__get_age())  # This will raise an AttributeError
# p.greet()
# print(p.get_age())

#Getters and Setters
#To maintain control over the access and modification of private variables, we use getters and setters.
#  These are methods that provide controlled access to private attributes.
# class demo:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
    
#     def get_age(self):
#         print(self.__age)
    
#     def set_age(self,age):
#         self.__age = age
    
# d = demo("kalyan",21)
# d.get_age()
# d.set_age(22)
# d.get_age()

# class demo:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     @property
#     def get_age(self):
#         print(self.__age)
#     @get_age.setter
#     def set_age(self,age):
#         self.__age = age
    
# d = demo("kalyan",21)
# d.get_age
# d.set_age = 22
# d.get_age

#inheritance
# class parent:
#     def __init__(self,name):
#         self.name = name
#     def info(self):
#         print(self.name)
# class child(parent):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
#     def info1(Self):
#         print(f"{Self.name} is {Self.age} years old")

# c = child("ramesh",27)
# c.info()
# c.info1()

# class parent:
#     def __init__(self,name):
#         self.name = name
#     def info(self):
#         print(self.name)

# class child(parent):
#     def info1(Self):
#         super().info()
#         print("is 29 years old")

# c = child("ramesh")
# c.info1()

# class A:
#     def speak(self):
#         print("A speaks")

# class B:
#     def speak(self):
#         print("B speaks")

# class C(A, B):
#     pass

# obj = C()
# obj.speak()  

# # Display MRO of class C
# print(C.mro())  


# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# # Creating objects
# animals = [Dog(), Cat()]

# # Using polymorphism: method is resolved at runtime based on the object type
# for animal in animals:
#     animal.speak()


# class Bird:
#     def sound(self):
#         print("Bird chirps")

# class Airplane:
#     def sound(self):
#         print("Airplane engine roar")

# # Polymorphic behavior
# def make_sound(obj):
#     obj.sound()

# bird = Bird()
# plane = Airplane()

# make_sound(bird)  # Output: Bird chirps
# make_sound(plane) # Output: Airplane engine roar


# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * (self.radius ** 2)

# # Polymorphism in action
# shapes = [Rectangle(2, 3), Circle(5)]

# for shape in shapes:
#     print(f"Area: {shape.area()}")


# from abc import ABC, abstractmethod

# # Creating an abstract class
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

#     @abstractmethod
#     def eat(self):
#         pass

# # Subclass that implements the abstract methods
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

#     def eat(self):
#         print("Dog eats bones")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

#     def eat(self):
#         print("Cat eats fish")

# # Creating objects
# dog = Dog()
# dog.sound()  # Output: Dog barks
# dog.eat()    # Output: Dog eats bones

# cat = Cat()
# cat.sound()  # Output: Cat meows
# cat.eat()    # Output: Cat eats fish


# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Car is starting.")

# class Bike(Vehicle):
#     def start(self):
#         print("Bike is starting.")

# # Creating objects
# car = Car()
# bike = Bike()

# # Using polymorphism with abstraction
# def start_vehicle(vehicle: Vehicle):
#     vehicle.start()

# start_vehicle(car)  # Output: Car is starting.
# start_vehicle(bike)  # Output: Bike is starting.




