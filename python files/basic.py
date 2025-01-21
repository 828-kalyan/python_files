#input 
# name = input("Enter your name: ")
# print("Hi " + name)

#simple excercise to tahe input of name and fav color and print
# name = input("Enter your name: ")
# fav_color = input("Enter your fav color: ")
# print(name + " likes " + fav_color)

#simple excercise to take input of users weight in pounds and convert it into kg's
# user_weight = int(input("Enter your weiht in (pounds): "))
# weight_in_kg = user_weight * 0.4536
# print("Your weight in kilograms is: ",weight_in_kg)

#strings
# s = "python"
# print(s[::-1])

# s = "python" 
# print(s * 4)

#string methods

# s = "kalyan"
# print(s.replace('k','j'))

# s = "kalyan"
# print(s.count('a'))

# s = "kalyan"
# print(s.find('a'))

# s = "apple banana orange"
# x = s.split()
# print(x)
# print(" ".join(x))

# s = "apple banana orange"
# print("apple" in s)
# print("cherry" not in s)

# s = " Python "
# print(s.strip())
# print(s.lstrip())
# print(s.rsplit())

# s = "123ggfg"
# print(s.isdigit())
# print(s.isalpha())
# print(s.isalnum())

# name = "Kalyan"
# age = 21
# print(f"{name} is {age} years old")
# Write a Python program to reverse a string using slicing.
# s = 'kalyan'
# reversed_str = s[::-1]
# print(reversed_str)

# Check if a given string is a palindrome.
# s = input("Enter a string: ")
# reversed_str = s[::-1] == s 
# if (reversed_str):
#     print("palindrome")
# else:
#     print("Not a palindrome")

# Count the number of vowels in a string.
# s = input("Enter a string: ")
# vowels  = "aeiouAEIOU"
# count = 0
# for c in s:
#     if c in vowels:
#         count += 1
# print(count)

# Convert a string to uppercase, lowercase, and capitalize the first letter.
# s = "python"
# upper = s.upper()
# lower = s.lower()
# cap = s.capitalize()
# print(upper)
# print(lower)
# print(cap)

#conditonal statements

# temp = int(input("Enter the temprature: "))
# if temp > 30:
#     print("Its a Hot day.")
# elif temp < 18:
#     print("Its a cold day")
# else: 
#     print("its a nice day")

# has_good_credit =True
# has_good_income = False
# if (has_good_credit and has_good_income):
#     print("Loan granted")
# else:
#     print("Loan is declined")

# has_good_credit =True
# has_criminal_background = True
# if has_good_credit and not has_criminal_background:
#     print("Loan granted")
# else:
#     print("Loan declined")

# name = input("Enter your name: ")
# if len(name) < 3:
#     print("name must be atleast 3 characters length")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good")

#weight converter
# print("Enter one option: 'L' for lbs and 'k' for kgs ")
# choice = input("Enter your choice: ").upper()
# weight = int(input("Enter your weight: "))
# if choice == 'K':
#     weight_pounds = weight * 2.205
#     print(f"your weight in pounds: {weight_pounds}") 
# elif choice == 'L':
#     weight_kgs = weight * 0.4536
#     print(f"your weight in Kg: {weight_kgs}")
# else:
#     print("Invalid choice entered")

#guess thw number game
# no = 9
# guess_count = 0
# guess_limit = 3 
# while guess_count < guess_limit:
#     guess = int(input("Enter the number:"))
#     guess_count += 1
#     if guess == no:
#         print("you won!")
#         break
# else:
#     print("You lost")

#type casting

#str to int and float
# s = '123'
# n = int(s)
# print(n)
# print(type(n))
# f = float(s)
# print()

#int to str
# n = 12
# s = str(n)
# print(s)
# print(type(s))
#float to string
# n = 34.8
# s = str(n)
# print(type(s))
# print(s)

#boolean 
# print(bool("hi"))
# print(bool(1))
# print(bool([]))
# print(bool(""))
# print(bool(None))
# print(bool([4,7,8]))

#nested loops
# for i in range(4):
#     for j in range(3):
#         print(f"{i}, {j}")


# assignment to print char 'F' using nested loops
# for i in range(5):
#     if i == 1 or i == 3 or i == 4 :
#         for j in range(2):
#             print("x",end=" ")
#     else:
#         for k in range(5):
#             print("x",end=" ")
#     print()

#pint char 'L' pattern using nested loops
# l1 = [5,2,5,2,2]
# for i in l1:
#     output = " "
#     for j in range(i):
#         output += 'X'
#     print(output)

#pint char 'L' pattern using nested loops
# l1 = [2,2,2,2,6]
# for i in l1:
#     output = " "
#     for j in range(i):
#         output += 'X'
#     print(output)

#lists
# fruits = ['apple','banana','cherry','orange']
# print(fruits[-4:len(fruits)])

#find largest element in the list
# list1 = [2,6,3,5,8,3,7,0,2,1]
# maxi = list1[0]
# for x in list1:
#     if x > maxi:
#         maxi = x
# print(maxi) 

#remove duplicates from a list
# list1 = [1,2,3,1,4,5,2,3,4,5]
# x = set(list1)
# print(x)
#another method
# list1 = [1,2,3,1,4,5,2,3,4,5]
# unique = []
# for i in list1:
#     if i not in unique:
#         unique.append(i)
# print(unique)

#dictionaries
#take input in 1,2,3 and print "one", "two","three"
# n = input("Enter your phone number: ")
# dict = {"1":"one",
#         "2": "Two",
#         "3":"Three",
#         "4":"Four",
#         "5":"Five",
#         "6":"Six",
#         "7":"Seven",
#         "8":"Eight",
#         "9":"Nine"}
# output= " "
# for i in n:
#     output += dict.get(i, "!") + " "
# print(output)





# set1 = {1, 2, 3}
# set2 = {3, 4, 5,6,7,8} 

# result = set1.union(set2)
# print(result)   
# result2 = set1.intersection(set2)
# print(result2) 
# result3 = set1.difference(set2)
# print(result3)
# result4 = set2.difference(set1)
# print(result4)
# result5 = set1 

# try:
#     # Code that may raise an exception
#     result = some_function()
# except Exception as e:
#     print(f"An error occurred: {e}")

# try:
#     # Code that may raise an exception
#     result = some_function()
# except Exception as e:
#     print(f"An error occurred: {e}")
#     print(f"Exception type: {type(e)}")

# import traceback
# try:
#     # Code that may raise an exception
#     result = some_function()
# except Exception as e:
#     print(f"An error occurred: {e}")
#     traceback.print_exc() 


#Write a Python program to print all prime numbers between 1 and 100.
#   # def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num%i==0:
#             return False
#     return True
# for i in range(1,101):
#     if is_prime(i):
#         print(i)

# Use a while loop to calculate the sum of the digits of a given number.
# sum = 0
# n = int(input("Enter the number:"))
# while n!=0:
#     rem = n%10
#     sum += rem
#     n = n//10 
# print(sum)

# Write a function that takes a list of numbers and returns the second largest number.
# def second_largest(arr):
#     lar = sec_lar = float('-inf')
#     for i in arr:
#         if i > lar:
#             sec_lar = lar
#             lar = i 
#         elif i > sec_lar and i != lar:
#             sec_lar = i
#     return sec_lar

# a =  list(map(int,input("Enter arr elements by space: ").split()))
# print(second_largest(a))

# Demonstrate the use of default arguments in a function.
# def add(a,b,c=10):
#     return a+b+c
# print(add(2,4))

# Write a Python program to remove duplicates from a list while maintaining the order.
# def remove_dup(arr):
#     s = []
#     for i in arr:
#         if i not in s:
#             s.append(i)
#     return s 
# a = [1,2,1,3,2,4,5,4]
# print(remove_dup(a))

# Implement a stack using a list with push, pop, and peek functionality.
# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         return(self.stack.pop())
#     def peek(self):
#         return(self.stack[-1])
#     def display(self):
#         return self.stack
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.display())
# print(s.peek())
# print(s.pop())
# print(s.peek())
# print(s.display())

# Create a class Rectangle with attributes length and width. Include a method to calculate the area and perimeter.
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2*(self.length + self.width)

# r = Rectangle(10,20)
# print(r.area())
# print(r.perimeter())
        
# Explain the difference between @classmethod, @staticmethod, and instance methods.


# Write a Python program to read a text file and count the number of words in it.
# Append a new line to an existing file without overwriting its content.


# Write a Python program using math module to calculate the factorial of a number.
# import math
# print(math.factorial(5))

# Use the datetime module to print the current date and time in the format YYYY-MM-DD HH:MM:SS.
# import datetime as d
# print(x = d.datetime.now())

# Write a Python program that handles ZeroDivisionError and prompts the user to enter another number.
# try:
#     a = int(input("enter the first num:"))
#     b = int(input("Enter the second num:"))
#     print(a//b)
# except ZeroDivisionError  as e:
#     print(f"{e}")


# Create a custom exception class NegativeNumberError that raises an error if a negative number is provided.
# class NegativeNumberError(Exception):
#     pass
# try:
#     n = int(input("Enter the number:"))
#     if n < 0 :
#         raise NegativeNumberError("Ngetaive number not allowed")
# except NegativeNumberError as e:
#     print(f"Error: {e}")

# Write a Python program demonstrating the use of a generator to yield Fibonacci numbers.
# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b, a+b
# f = fib()
# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# print("The first", n, "Fibonacci numbers are:")   
# for _ in range(n):
#         print(next(f), end=" ")

# # Implement a decorator that logs the arguments and return value of a function.

# # Write a Python program to implement binary search for a sorted list.
# def binary_search(arr,key):
#     left,right = 0, len(arr)-1
#     while left <= right:
#         mid = (left + right)//2
#         if arr[mid] == key:
#             return mid 
#         elif arr[mid] < key:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# a = [2,4,2,3,6,89,2,3,5,7]
# print("the element found at index:",binary_search(a,7))

# # Given an array of integers, find the contiguous subarray with the maximum sum (Kadane’s Algorithm.`