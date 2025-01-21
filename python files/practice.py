#Advanced Questions

#Write a function that generates a list of squares of numbers using list comprehension.
# squares = [x*x for x in range(10)]
# print(squares)

#Implement a lambda function to sort a list of tuples based on the second value.
# data = [(1, 3), (4, 1), (2, 2), (5, 0)]
# s = sorted(data,key = lambda x: x[1])
# print(s) 
 
#Create a function using the global keyword to modify a global variable.
# x = 10
# def update_global():
#     global x
#     x = 20
#     print(x)

# update_global()
# print(x)

# x = 10 
# def fun():
#     global x
#     x = 20
# fun()
# print(x)

#Write a function that demonstrates the use of nonlocal to modify a variable in the enclosing scope.
# def outer_fun():
#     x = 10 
#     def inner_fun():
#         nonlocal x
#         x = 20
        
#         return x 
#     print(inner_fun())
#     return x

# print(outer_fun())

# Challenges with Real-World Use Cases

# Create a function that takes a dictionary of student marks and returns a 
# new dictionary with the names of students who scored above 75.
 
# dic = {'a' : 90, 'b' : 32, 'c' : 78, 'd' : 23}
# fil = {key : value for key,value in dic.items() if value > 75} 
# print(fil)

#Write a function to perform basic mathematical operations 
#(add, subtract, multiply, divide) based on a keyword argument (operation='add', etc.).

# def cal(a,b,operation):
#     if operation == "add":
#         return a+b 
#     elif operation == "sub":
#         return a-b 
#     elif operation == "mul":
#         return a*b 
#     elif operation == "div":
#         if b != 0:
#             return a//b
#         else:
#             ValueError("cant divide with zero")
#     else:
#         ValueError("invalid input")
# x = str(input("Enter operation:"))
# print(cal(3,7,x))

# Implement a function that takes a list of dictionaries(representing items with prices) 
# and returns the total cost after applying a discount using a lambda function.

# Special Scope-Based Questions

# Write a function with a local variable and show how it’s inaccessible outside the function.
# def fun():
#     x = 10 
#     print(x) 
# fun()
# print(x)

#Demonstrate the difference between global and nonlocal using a nested function structure.
# glo = 10 
# def outer_fun():
#     x = "inside outer_fun"
#     global glo 
#     glo = 20
#     def inner_fun():
#         nonlocal x 
#         x = "inner_fun"
#         print(x)
#         print(glo)
#     inner_fun()
    
#     print(glo)
#     print(x)
# outer_fun()
# print(glo)  

# Write a function that creates another function dynamically (closure) and returns it.

# Testing Concepts: Combine Features

# Combine zip and enumerate in a function to iterate over two lists with their indices.

# def fun(list1,lis2):
#     for i,(list1,lis2) in enumerate(zip(l1,l2)):
#         print(f"{i} {list1} is {lis2} years old")
# l1 = ["jack","ally","Ram"]
# l2 = [20, 18, 19]
# fun(l1,l2)

# l1 = ["jack","ally","Ram"]
# l2 = [20, 18, 19]
# zipped = list(zip(l1,l2))
# x = enumerate(zipped)
# print(x)

# Write a function that accepts a list of numbers and returns a dictionary with the square of each number as a key-value pair using dictionary comprehension.

# lis = [1,2,3,4,5]
# squares = {x:x*x for x in lis}
# print(squares)

# Create a function that uses map to convert a list of strings to uppercase and filter to remove strings shorter than 4 characters.

# def process_strings(s):

#     uppercase_s = map(str.upper, s)
#     filtered_s = filter(lambda s: len(s) >= 4, uppercase_s)

#     return list(filtered_s)

# s = ["cat", "elephant", "dog", "python", "AI", "code"]
# x = process_strings(s)
# print(x)  

#Write a one-liner list comprehension to generate all numbers divisible by 3 and 5 within a range.

# nums = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
# print(nums)
# Functions:
# Write a function to calculate the factorial of a number using recursion.
# def fact(n):
#     if n <= 1:
#         return n 
#     return n*fact(n-1)
# print(fact(4))

#Write a generator that yields Fibonacci numbers up to a given limit.
# def fibonacci_up_to(n):
#     a, b = 0, 1
#     while a <= n:
#         yield a
#         a, b = b, a + b

# num = int(input("Enter the number for Fibonacci numbers: "))
# for num in fibonacci_up_to(num):
#     print(num, end=" ")

#Validate an email address using regular expressions.
# import re
# def validate_email(s):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return bool(re.match(pattern, s))

# s = input("Enter an email: ")
# if validate_email(s):
#     print("Valid")
# else:
#     print("Invalid")


# Easy Level
# Shopping List Manager:
# Create a program that allows users to add, remove, and view items in a shopping list.
# class my_cart:
#     def __init__(self):
#         self.list1 = []
#     def add(self,item):
#         self.list1.append(item)
#     def remove(self,item):
#         if item in self.list1:
#             self.list1.remove(item)
#         else:
#             print(f"{item} not in the list")
#     def view(self):
#         return ", ".join(self.list1) if self.list1 else "your cart is empty"
        
# c = my_cart()
# c.add("shirt")
# c.add("Apple")
# c.add("boom boom")
# print(c.view(),end = " ")
# c.remove("boom boom")
# print(c.view())

# Temperature Converter:
# Build a tool to convert temperatures between Celsius, Fahrenheit, and Kelvin.

# def far_cel():
#     fahrenheit = float(input("Enter the Fahrenheit temperature to convert: "))
#     celsius = (fahrenheit -32) * 5/9
#     print(f"{celsius:.3f}°C")

# def cel_kel():
#     celsius = float(input("Enter the temperature in Celsius: "))
#     kel = celsius + 273.15
#     print(f"{round(kel,2)}K")

# def cel_far():
#     celsius = float(input("Enter the temperature in celsius: "))
#     far = (celsius * 9/5) + 32
#     print(f"{far}°F")
# def kel_cel():
#     kel = float(input("Enter the temperature in Kelvin: "))
#     cel =  kel - 273.15
#     print(f"{cel:.2f}°C")

# def menu():
#     print("1. Fahrenheit to Celsius\n")
#     print("2. Celsius to Kelvin\n")
#     print("3. Celsius to Fahrenheit\n")
#     print("4. Kelvin to Celsius")

# def main():
#     while True:
#         menu()
#         try:
#             choice = int(input("Enter your Choice : "))
#         except ValueError:
#             print("Invalid input. Please enter a number")
#             continue

#         if choice == 1:
#             far_cel()
#         elif choice == 2:
#             cel_kel()
#         elif choice == 3:
#             cel_far()
#         elif choice == 4:
#             kel_cel()
#         else:
#             print("Invalid choice. Please select from the menu.")

#         x = input("Do you want to perform another conversion? (y/n): ").strip().lower()
#         if x != "y":
#             print("bye")
#             break

# main()

# Basic Calculator:
# Develop a basic calculator that performs addition, subtraction, multiplication, and division based on user input.

# def add(x,y):
#     return x + y 
# def sub(x,y):
#     return x - y 
# def mul(x,y):
#     return x * y
# def div(x,y):
#     if y == 0:
#         print("Enter valid input")
#     else:
#         return x/y
# def menu():
#     print("1. addition\n")
#     print("2. subtraction\n")
#     print("3. Multiplication\n")
#     print("4. Division")

# def main():
#     while True:
#         menu()
#         choice =int(input("Enter your choice: "))

#         n1 = float(input("Enter the first number: "))
#         n2 = float(input("Enter the second number: "))

#         if choice == 1:
#             print(f"{n1} + {n2} = {add(n1,n2)}")
#         elif choice == 2:
#             print(f"{n1} + {n2} = {sub(n1,n2)}")
#         elif choice == 3:
#             print(f"{n1} + {n2} = {mul(n1,n2)}")
#         elif choice == 4:
#             print(f"{n1} + {n2} = {div(n1,n2)}")
#         else: 
#             print("Enter the valid input number")


# main()

# Quiz Application:
# Write a program that quizzes the user on basic math problems and evaluates their score.

# Password Strength Checker:
# Create a program that checks if a password is strong by verifying its length and character composition (uppercase, lowercase, numbers, symbols).

# def pass_strength(password):
#     punct = ['@','#','$','%','&','-','_']
#     if len(password) >= 8:
#         has_upper = any(char.isupper() for char in password)
#         has_lower = any(char.islower() for char in password)
#         has_num = any(char.isdigit() for char in password)
#         has_punct = any(char in punct for char in password)
#         if has_lower and has_upper and has_num and has_punct:
#             print("Strong Password")
#         elif (has_num and has_lower and has_upper) or (has_punct and has_lower and has_upper):
#             print("Average Password")
#     else:
#         print("Weak Password")
    
# s = str(input("Enter the Password: "))
# pass_strength(s) 

# Student Grade Management System:
#Build a program where users can add students, assign grades, and calculate the class average.
# class stu_mang:
#     def __init__(self):
#         self.students = {}
#     def add_name(self,name):
#         if name not in self.students:
#             self.students[name]  = []
#             print(f"student {name} added")
#         else:
#             print(f"student {name} already exists")
#     def add_marks(self,name,marks):
#         if name in self.students:
#             self.students[name].append(marks)
#             print(f"marks added to {name}")
#     def class_avg(self):
#         s = 0
#         count = 0
#         for x in self.students.values():
#             s += sum(x) 
#             count = len(x)
#         return s/count 
    
#     def show(self):
#         if not self.students:
#             print("No students in the class.")
#             return
#         print("\nStudents and their average grades:")
#         for name, marks in self.students.items():
#             avg = sum(marks)/len(marks) 
#             print(f"{name}: {avg:.2f}")

# s = stu_mang()
# s.add_name("kalyan")
# s.add_name("Krishna")
# s.add_name("anil")
# s.add_marks("kalyan",78)
# s.add_marks("Krishna",90)
# s.add_marks("anil",67)
# s.add_marks("kalyan",86)
# s.add_marks("kalyan",77)
# print(s.class_avg())
# s.show()


# To-Do List:
# Create a to-do list application that lets users add, mark as completed, and delete tasks. Save the data in a file.




# class atm:
#     def __init__(self):
#         self.balance = 0
    
#     def credit(self,amount):
#         self.balance += amount
    
#     def withdraw(self,amount):
#         self.balance -= amount
    
#     def show(self):
#         print("Your balance is: ",self.balance)

# s = atm()
# s.credit(100000)
# s.show()
# s.withdraw(2000)
# s.show()
    

# i = 0
# while i < 5: 
#     print(i)  
#     j = 1
#     while j < 5:
#         print(j)
#         j += 0.1
#     i += 1
        

# print("Hello, World!\rGoodbye!")
# print("Hello\rGoodbye!")
# print("Hello, World!\r\nWelcome to Python.")
# print("Hello\tworld!")
# print("Hello\vworld!")
# print("Hello\fWorld")

# class MyIterable:
#     def __init__(self, limit):
#         self.limit = limit

#     def __iter__(self):
#         self.current = 0
#         return self

#     def __next__(self):
#         if self.current < self.limit:
#             self.current += 1
#             return self.current - 1
#         else:
#             raise StopIteration

# for num in MyIterable(5):
#     print(num)


# for i in range(0, 20, 5):
#     print(i)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()

# l = [1,2,3,4,5]
# x = [i+5 for i in l]
# print(x)

# def fun(n):
#     return ''.join(n.split()[::-1])
# print(fun("Hi mirafra"))


# lis = [1,102,32,49,5,23,65,87,29]
# lis.sort()
# print(lis)

#bubble sort

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j],arr[j + 1] = arr[j + 1],arr[j]
#     return arr
# #a = [2,5,3,1,4]
# a = [2,5,3,4,67,4,53,3,5,6,7,70,54,3,4,6,7,4,3,22,98]
# print(bubble_sort(a))


# l = []
# l2 = []
# a = [1,2,3,4,5,6,7,8,9,10]
# b = 'abcdefghi'

# for i in a:
#        if i %2!=0:
#               l.append(i)
# for j in range(len(b)-2,-1,-2):
#        l2.append(b[j])
    
# result = [x for x in zip(l,l2) for x in x]
# print(result)

#1.Convert this to dict. Use only dict comprehension.
# string = "A - 13, B - 14, C - 15"
# string = string.replace(" - ", " ").replace(", ", " ")
# x =string.split(" ")
# print(x)
# d = {x[i]:x[i+1] for i in range(0,len(x),2) }
# print(d)

# string = "11 - 13, 12 - 14, 13 - 15"
# string = string.replace(" - "," ")
# string = string.replace(", "," ")
# s = string.split(" ")
# d = {int(s[i]):int(s[i+1]) for i in range(0,len(s),2)}
# print(d)

# r = int(input("Enter the rows: "))
# c = int(input("Enter the columns: "))
# a = []
# b = []

# for i in range(r):
#     a= []
#     for j in range(c):
#         v = int(input())
#         a.append(v)
#     b.append(a)

# for i in range(r):
#     for j in range(c):
#         print(b[i][j],end= " ")
#     print()
        


# a = [[1,2,3],
# [4,5,6],
# [7,8,9]]

# for i in range(len(a)):
#     for j in range(len(a)):
#         print(a[i][j],end= " ")
#     print()



# s = [1,2,3,4,5,6]
# for i in s:
#     print(i)
# a = iter(s)
# print()
# print(next(a))
# print(next(a))

# def ten():
#     n=1
#     while n<=10:
#         sq=n*n#9
#         yield sq
#         n+=1
# value=ten()#1,4,9
# print(value)
# for i in value:print(i)

# a = []
# def ten():
#     n=1
#     while n<=10:
#         sq=n*n#9
#         n+=1
#         a.append(sq)
#     return a
        
# value=ten()#1,4,9
# print(value)
# for i in value:print(i)


# inf = iter(int,1)
# print(next(inf))
# print(next(inf))
# print(next(inf))

# def fun():
#     yield 1
#     yield 'a','b',1
#     yield 5
# s = fun()
# print(s)
# print(fun)
# print(next(s))
# print(next(s))


#Write a generator function that produces the Fibonacci sequence indefinitely. 
# Use yield to return the next number in the sequence.

# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
    

# f = fib()
# for i in range(6):
#     print(next(f))


# def numberGenerator(n):
#     number = yield
#     #print(number)
#     while number < n:
#         number = yield number
#         #print(number)
#         number += 1

# g = numberGenerator(10)    # Create our generator
# g.send(None)

# print(g.send(5))
# print(g.send(6))
# print(g.send(5))



# class gen:
#     def __init__(self, n):
#         self.n = n       
#         self.count = 0    
#         self.current = 2  
#     def __iter__(self):
#         return self  
#     def __next__(self):
#         if self.count < self.n:
#             while not self._is_prime(self.current):
#                 self.current += 1  
#             prime = self.current
#             self.current += 1  
#             self.count += 1     
#             return prime
#         else:
#             raise StopIteration  

#     def is_prime(self, num):

#         if num <= 1:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

# n = 5 
# g = gen(n)

# for i in g:
#     print(i)





# class demo:
#     x = 10
#     def __init__(self,age):
#         self.age = age   
#     def fun(name):
#         print(f"Hello {name}")
#     def fun1(self):
#         print(f"{self.age}")

# s = demo(21)
# print(s.x)
# print(demo.x)
# demo.fun("kalyan")
# #s.fun()#standalone function accesing through instance raises an error
# s.fun1()
# demo.fun1(s) #instance function accesing through class


# class demo:
#     x = 10 
#     def __init__(self,age):
#         self.age = age
#     def fun(self,name):
#         print(f"Hello i am {name} my age is {self.age}")
#     def greet(self):
#         print('Hello')

# s = demo(21)
# print(s.x)
# print(demo.x)
# s.fun("kalyan")
# s.greet()
#demo.fun("kalyan")
#demo.greet()

# class Person:
#     "This is a person class"
#     age = 10
#     def greet(self):
#         print('Hello')
# print(Person.age)
# print(Person.greet)
# print(Person.__doc__)
# harry = Person()
# harry.greet()

#static method
# class Calculator:
    
#     @staticmethod
#     def multiply(x, y):  #
#         return x * y

# calc = Calculator()         

# print(Calculator.multiply(5, 3))  #staticmethod can acces using class
# print(calc.multiply(5, 3))   #staticmethod can be accesed using instance

# class demo:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         demo.count += 1

#     @classmethod
#     def fun(cls):
#         return cls.count

# s1 = demo("kalyan")
# s2 = demo("Ram")

# print(s1.fun())
# print(demo.fun())

# class bank:
#     intrest = 0.05
    
#     def __init__(self,balance):
#         self.balance = balance
    
#     @classmethod
#     def set_intrest(cls,new_rate):
#         cls.intrest = new_rate

#     def claculate_intrest(self):
#         print(bank.intrest * self.balance)

# s = bank(1000)
# s.claculate_intrest()

# s.set_intrest(0.07)
# s.claculate_intrest()



# class demo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @property
#     def name(self):
#         print(self._name)

#     @name.setter
#     def name(self,value):
#         self._name = value
    
#     @property
#     def age(self):
#         print(self._age)
    
#     @age.setter
#     def age(self,v):
#         self._age = v 
    
# s = demo("kalyan",21)
# s.name

# s.name = "Kumar"
# s.name

# s.age
# s.age = 22

# s.age


# class bill:
#     def __init__(self, m, u):
#         self.m = m
#         self.u = u

#     def __add__(self, other):
#         m = self.m + other.m
#         u = self.u + other.u
#         bill1 = bill(m, u)
#         return bill1
    
#     def __gt__(self, other):
#         if self.m + other.m > self.u + other.u:
#             return "my bill is greater"
#         else:
#             return "your bill is greater"



# a1 = bill(5000, 15000)
# a2 = bill(25000, 5000)
# a = a1 + a2
# print('Your bill=', a.u)
# print('My bill=', a.m)

# x = a1 > a2
# print(x)
 
# class demo:
#     def __init__(self,value):
#         self.__value = value
    
#     def __fun(self):
#         print(self.__value)

# s= demo(10)
# print(s._demo__value)
# s._demo__fun()

# class parent:
#     _v = 20
#     def __init__(self,value):
#         self.__value = value
#     def _fun(self):
#         print("I am parent class")
#         print(self.__value)

# class child(parent): 
#     def child_fun(self):
#         print("I am child class")
#     #print(parent.__v)  

# s = child(10)
# #print(s._v)
# s._fun()
# #s.child_fun() 
"""Protected members (those with a single underscore _) are accessible from outside the class, but it’s recommended not to access them directly. They are intended to be used inside the class and by subclasses.
Private members (those with a double leading underscore __) are not accessible directly from outside the class. They are name-mangled, meaning they are stored with an internal name (e.g., _Parent__value), but accessing them this way is considered bad practice."""

# class parent:
#     def __init__(self,value):
#         self.value = value
#     def fun(self):
#         print("I am parent class",self.value)
    
# class child(parent):
#     def __init__(self,value,name):
#         super().__init__(value)
#         self.name = name
#     def child_fun(self):
#         print("I am child class",self.value,self.name)

# s = child(10,"kalyan")
# s.fun()
# s.child_fun() 

# class parent:
#     def __init__(self,value):
#         self.value = value
#     def fun(self):
#         print("I am parent class",self.value)
    
# class child(parent):
#     def child_fun(self):
#         print("I am child class")
        
# s = child(10)
# s.fun()
# s.child_fun()

# class parent:
#     _v = 10
#     def fun(self):
#         print("public method")
#     def _fun1(self):
#         print("protected method")


# # s = parent()
# # s._fun1()
# print(parent._fun1(1))

