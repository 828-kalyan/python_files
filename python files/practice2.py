# x = list((1,2,3,4))
# print(x)

# s = ['apple','banana','cherry','orange','grape','papaya']
# s[2] = 'kiwi'
# print(s)

# s = ['apple','banana','cherry','orange','grape','papaya']
# s[1:3] = ["berry",'kiwi']
# print(s)

# s = ['apple','banana','cherry','orange','grape','papaya']
# s.insert(2,'kiwi')
# print(s)

# s = ['apple','banana','cherry','orange','grape','papaya']
# #s.append('berry')
# d = [1,2,3,4,5,6]
# s.extend(d)
# print(s)

#s = ['apple','banana','cherry','orange','grape','papaya']
# s.remove('cherry')
# print(s)
# s.pop(4)
# print(s)
# s.pop()
# print(s)
# del s[1]
# print(s)
# del s
# print(s)

#s = ['apple','banana','cherry','orange','grape','papaya']
# for x in s:
    #print(x)

# for i in range(len(s)):
#     print(s[i])
#[print(i) for i in s]

#list comprehension

# s = ['apple','banana','cherry','orange','grape','papaya']

# l = [x for x in s if 'a' not in x]
# l2 = [x for x in s]
# l3 = [x for x in s if x != 'apple']
# l4 = [x if x!= 'banana' else 'orange' for x in s]
# l5 = [x for x in range(10)]
# l6 = [x for x in range(10) if x <5]
# l7 = [x.upper() for x in s]
# l8 = ['hi' for x in s]
# print(l8)

#s = ['apple','banana','cherry','orange','grape','papaya']
#s.sort(key= str.lower)
#s.sort(reverse=True)
#s.reverse()
#print(s)
#print(sorted(s))

# l = [1,2,3,4]
# l2 = l.copy()
# l3 = l[:]
# l4 = l
# l.append(5)
# print(l2)
# print(l3)
# print(l4)

# l1 = [1,2,3]
# l2 = [4,5,6]
# l3= l1 + l2
# print(l3)

# l = ["Inception", "Titanic", "Avatar"]
# l.append("The matrix")
# l.remove('Titanic')
# print(l)
# print(len(l))
# l.sort()
# print(l)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l = 0
# for i in numbers:
#     l += i
# print(l)
# s = [x for x in numbers if x%2!= 0]
# print(s)
# s.sort(reverse= True)
# print(s)

#tuples

# t = ('a','b','c','d','e')
# print(t[0:4])
# u = ('f','g')
# t += u
# print(t)

#modifying tuples

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# l = list(fruits)
# l[1] = "berry"
# fruits = tuple(l)
# print(fruits)

#unpacking 

# t = (1,2,3)
# a,b,c = t
# print(a)

# x, _, z = t
# print(x,z)

# u = [1,2,3,4,5,6,7,8,9]
# a,b,*c = u
# print(b)
#print(c)

# s = (1,(2,3),4,5)
# a,(b,c),d,e = s
# print(a,b,c,d,e)

# word = "hello"
# a, b, *rest = word
# print(a, b, rest)  # Output: h e ['l', 'l', 'o']

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined = [*list1, *list2]
# print(combined)  # Output: [1, 2, 3, 4, 5, 6]

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits
# print(green)
# print(red)

#sets
#s = {1,2,3,4,5,5,6}
# print(s)
# s.add(7)
# print(s)
# s.remove(7)
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)
# t = {'a','b','c'}
# s.update(t)
# print(s)

#union
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
#s = set1.union(set2)
#print(s)
# s = set1 | set2
# #print(s)
# x = set1 | set2 | set3 | set4
# print(x)

#intersection
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)

# s = set1 & set2
# print(s)

#difference  = The difference() method will return a new set that will contain only 
# the items from the first set that are not present in the other set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)

# s = set1 - set2
# print(s)

#symetric difference  = The symmetric_difference() method will keep only the elements that are NOT present in both sets
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)
# print(set3)

# s = set1 ^ set2
# print(s)

# Passed_test = {"Alice", "Bob", "Charlie", "David"}
# Completed_survey = {"Charlie", "David", "Edward", "Fay"}

# # Union of sets.
# u= Passed_test | Completed_survey
# print(u)
# # Intersection of sets.
# i = Passed_test & Completed_survey
# print(i)
# # Difference of sets.
# d = Passed_test - Completed_survey
# print(d)

# words = ["apple", "banana", "apple", "orange", "banana", "grape"]

# # Set with unique words.
# s = set(words)
# print(s)
# # Count of unique words.
# print(len(s))
# # Check for a specific word (e.g., "orange").
# x = "orange" in s
# print(x)

#dictionary
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020,
#   'y': 2020
# }
# print(thisdict)
# print(type(thisdict))
# print(len(thisdict))

# x = thisdict["model"]
# print(x)

# s = thisdict.get("model")
# print(s)

# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())

# if "y" in thisdict:
#   print("yes")

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) 

# car["color"] = "red"

# print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

#add item
# car["color"] = 'red'
# print(car)
# #modify item
# car["year"] = 2020
# print(car)
#remove
# car.pop("year")
# print(car)

# car.popitem()
# print(car)

# del car["brand"]
# print(car)

#loop
# for x in car:
#     print(x)

# for x in car:
#     print(car[x])

# for x in car.keys():
#     print(x)

# for x in car.values():
#     print(x)

# for x in car.items():
#     print(x)

# d = {"Alice": "12345", "Bob": "67890"}
# # Add contact: "Charlie": "112233"
# d.update({"Charlie": "112233"})
# print(d)
# # Remove contact: "Bob"
# d.pop("Bob")
# print(d)

s = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

# Average score.
# x = 0
# c = 0
# for i in s.values():
#     c += 1
#     x += i
# print("Avg",x//c)

# Name of the student with the highest score.
# x = max(s.values())
# print(x)
# Updated dictionary after adding a new student’s score.
# s["kalyan"] = 100
# print(s)


# If-Else Practice:
# Write a program that checks whether a number is positive, negative, or zero.
# num = int(input("Enter a number: "))


# For Loop Practice:
# Write a program to print all even numbers from 1 to 20.

# x = [x for x in range(21) if x %2==0]
# print(x)


# While Loop Practice:
# Write a program that prints the factorial of a number (use while loop).
# n = int(input("Enter a number: "))
# s = 1
# while n > 0:
#     s *= n
#     n -= 1
# print(s)

# Logical Operators Practice:
# Write a program that checks if a number is both even and greater than 10.
# n = int(input("Enter a number: "))
# if n > 10 and n%2==0:
#     print("true")
# else:
#     print("false")


# Function with Parameters:
# Write a function that calculates the square of a given number.
# def square(num):
#     print(num**2)
# square(6)

# Function with Default Parameter:
# Write a function that greets the user with their name. If no name is provided, greet them as "Guest".

# def greet(name="Guest"):
#     print(f"hello {name}")
# greet("kalyan")
# greet()

# Function with Multiple Return Values:
# Write a function that returns both the sum and the product of two numbers.

# def sum_and_product(a, b):
#     s = a + b
#     m = a * b
#     return s, m
# print(sum_and_product(5,6))

# Global and Local Variables:
# Write a function that modifies a global variable and prints 
x = 50  # Global variable

# def modify_global():
#     global x
#     x = 100
#     print(x)

# modify_global()  
# print(x)


# 1. Review Basic Python Concepts:
# Syntax and data types: Strings, integers, floats, lists, tuples, sets, dictionaries.
# Control structures: If-else, loops (for, while), and logical operators.
# Functions: Definition, parameters, return statements, and variable scope (global vs local).
# OOP basics: Classes, objects, inheritance, encapsulation, and polymorphism.
# Error handling: Try-except blocks and handling exceptions.
# I will make sure that I understand these basic concepts thoroughly because scenario-based questions often require applying these fundamentals.

# 2. Practice with Code Examples:
# I will write simple code snippets to reinforce the theory.
# Use tools like Jupyter Notebooks or Python's interactive shell to practice running and debugging code.
# Focus on problems that can combine different topics like loops, functions, and conditionals.
# 3. Understand Common Python Libraries:
# Standard libraries like math, datetime, random, and os are often used in Python exams.
# I will make sure to familiarize myself with their functions and usage.

# 4. Scenario-Based Practice:
# Since the exam may involve scenario-based questions, I will focus on problems that involve applying Python to real-world situations. Here’s how I would practice:

# Think of possible scenarios that might be asked, such as:
# Write a Python function to calculate the factorial of a number.
# Create a program that takes input from the user, processes it, and outputs the result (e.g., calculating the area of a circle).
# Given a list of numbers, write a function to return only even numbers.
# Work on mini-projects or exercises:
# Create a small project that uses file handling (reading/writing files).
# Work on manipulating data in lists, dictionaries, or sets.
# Solve problems related to sorting or searching algorithms, as they might be part of the exam.


# 7. Key Areas to Focus On:
# Data structures: Lists, dictionaries, and sets, as scenario-based questions often require manipulation of data.
# Algorithms: Simple algorithms for searching, sorting, and processing data.
# Functions and modular programming: Writing clean and modular code to solve complex problems.
# Object-Oriented Programming: This is commonly asked in company exams as it shows an understanding of clean code principles.
# 8. Test Edge Cases:
# For each scenario, I will think of edge cases to ensure the code is robust (e.g., handling invalid inputs or large numbers).
# 9. Stay Calm and Think Logically During the Exam:
# During the exam, I will carefully read each scenario, identify the requirements, and break the problem down into smaller manageable tasks.
# I will take a few moments to plan out the structure of the solution before writing the code.
# By following these steps, I can effectively prepare for the Python exam and increase my chances of passing with confidence!





# file_object = open("filename", "mode")
# "filename": The name of the file (can be a path to the file).
# "mode": Specifies the mode in which the file should be opened:
# 'r': Read (default mode).
# 'w': Write (creates a new file or overwrites an existing file).
# 'a': Append (adds data to an existing file).
# 'rb'/'wb': Read/Write in binary mode.
# 'r+': Read and write.


# file = open("example.txt", "r")  # Open the file in read mode
# content = file.read()  # Read the content of the file
# print(content)  # Output: Contents of example.txt
# file.close()  # Always close the file after use
# 2. Reading from a File
# Once the file is opened in read mode ('r'), you can read the contents in several ways:

# read(): Reads the entire file as a single string.
# readline(): Reads the next line from the file.
# readlines(): Returns a list of lines in the file.
# Examples:
# python
# Copy
# # Using read()
# file = open("example.txt", "r")
# content = file.read()  # Read the entire file content
# print(content)
# file.close()

# # Using readline()
# file = open("example.txt", "r")
# line = file.readline()  # Read one line from the file
# print(line)
# file.close()

# # Using readlines()
# file = open("example.txt", "r")
# lines = file.readlines()  # Read all lines as a list
# print(lines)
# file.close()
# 3. Writing to a File
# You can write to a file in Python using the write() or writelines() methods.

# write(): Writes a string to the file (if the file is opened in write or append mode).
# writelines(): Writes a list of strings to the file.

# # Using write()
# file = open("output.txt", "w")  # Open file in write mode (creates a new file)
# file.write("Hello, World!")  # Write text to the file
# file.close()

# # Using writelines()
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# file = open("output.txt", "w")
# file.writelines(lines)  # Write a list of lines to the file
# file.close()
# If the file already exists, opening it with "w" will overwrite the existing content.
# Append Mode:
# If you want to append data to an existing file, use "a" mode.
# python
# Copy
# file = open("output.txt", "a")  # Open file in append mode
# file.write("Appending a new line\n")  # Add new content to the file
# file.close()
# 4. Using with to Open Files (Context Manager)
# It's a best practice to use the with statement when opening files because it automatically closes the file after the block of code is executed, even if an exception occurs.

# Example:
# python
# Copy
# with open("example.txt", "r") as file:
#     content = file.read()  # Read the content of the file
#     print(content)
# # No need to call file.close(), it is automatically closed after the block ends.
# This ensures that the file is always closed after the operations are done.
# 5. Handling Exceptions in File Operations
# When working with files, it’s important to handle potential exceptions, such as trying to read from a non-existent file or a file that is not accessible.

# Common exceptions:
# FileNotFoundError: Raised when trying to open a file that doesn't exist.
# PermissionError: Raised when there are insufficient permissions to access the file.
# Example:
# python
# Copy
# try:
#     with open("nonexistent_file.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File not found!")
# except PermissionError:
#     print("You don't have permission to access this file!")
# 6. File Positioning: seek() and tell()
# seek(offset): Moves the file pointer to the specified position. The offset is given in bytes (from the beginning of the file).
# tell(): Returns the current position of the file pointer.
# Example:
# python
# Copy
# with open("example.txt", "r") as file:
#     print(file.tell())  # Output the current position (0 at the beginning)
#     file.seek(5)  # Move the pointer to the 5th byte
#     print(file.tell())  # Output: 5
#     content = file.read(10)  # Read 10 characters from the current position
#     print(content)
# 7. Working with CSV Files
# Python has a built-in library called csv to work with CSV (Comma Separated Values) files.

# Reading CSV Files:
# python
# Copy
# import csv

# with open('data.csv', newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)  # Each row is a list of values
# Writing to CSV Files:
# python
# Copy
# import csv

# data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]

# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
# csv.reader() reads the CSV file, and csv.writer() writes data into the CSV file.
# Practice Problems:
# File Reading and Writing:

# Write a program that reads a text file, counts the number of words in it, and writes the word count to another file.
# Append Mode:

# Write a program that asks the user to input a string and appends it to an existing file.
# CSV File Handling:

# Write a program that reads a CSV file containing employee names and ages and prints out the names of employees who are over 30 years old.
# Exception Handling:

# Write a program that handles FileNotFoundError and PermissionError while opening a file for reading.
# Recap of File Handling:
# Opening Files: Use open() with the appropriate mode ('r', 'w', 'a').
# Reading Files: Use methods like read(), readline(), and readlines().
# Writing Files: Use write() and writelines() for writing data to files.
# Context Manager: Use with to ensure files are properly closed.
# Exceptions: Handle errors like FileNotFoundError and PermissionError.
# CSV Files: Use the csv module to read and write CSV files.
# Next Steps:
# Practice handling different types of files (text files, CSV files).
# Implement file reading and writing with exception handling.
# Test your skills with larger files to understand how file handling works in memory.
# Let me know when you’re ready for the next topic or if you need more examples!


# 8. Regular Expressions (Regex) in Python

# re.search(): Searches for a pattern in a string.
# re.match(): Tries to match the pattern at the start of the string.
# re.findall(): Returns all occurrences of the pattern in the string.
# re.sub(): Replaces occurrences of a pattern with a string.


# .: Matches any character except a newline.
# ^: Matches the start of the string.
# $: Matches the end of the string.
# []: Matches any single character inside the brackets.
# |: Acts as a logical OR between two expressions.
# \d: Matches any digit (equivalent to [0-9]).
# \w: Matches any word character (letters, digits, and underscores).
# \s: Matches any whitespace character (spaces, tabs, newlines).
# *: Matches zero or more of the preceding character.
# +: Matches one or more of the preceding character.
# {n}: Matches exactly n occurrences of the preceding character.
# {n, m}: Matches between n and m occurrences of the preceding character.


# 3. Using re.search()
# The re.search() function searches the entire string for a match to the regular expression and returns the first match.


# match = re.search(pattern, string)
# If a match is found, it returns a Match object. If not, it returns None.

# import re

# pattern = r"apple"
# text = "I like apple pie"
# match = re.search(pattern, text)
# if match:
#     print(f"Found: {match.group()}")
# else:
#     print("No match")


# 4. Using re.match()
# The re.match() function checks for a match only at the beginning of the string.

# import re
# pattern = r"apple"
# text = "apple pie is tasty"
# match = re.match(pattern, text)
# if match:
#     print(f"Match: {match.group()}")
# else:
#     print("No match")
# The output will be: Match: apple because the string starts with "apple".
# 5. Using re.findall()
# The re.findall() function returns all non-overlapping matches of the pattern in a string as a list.


# import re

# pattern = r"\d+"  # Find all sequences of digits
# text = "My number is 123, and my friend's number is 456."
# matches = re.findall(pattern, text)
# print(matches)  # Output: ['123', '456']
# The output is a list of all sequences of digits: ['123', '456'].

# 6. Using re.sub()
# The re.sub() function replaces occurrences of the pattern in the string with a replacement string.

# new_string = re.sub(pattern, replacement, string)

# import re

# pattern = r"pie"
# replacement = "cake"
# text = "I like apple pie"
# new_text = re.sub(pattern, replacement, text)
# print(new_text)  # Output: "I like apple cake"
# The output will be: I like apple cake.

# 7. More Advanced Examples of Regular Expressions
# Example 1: Matching Email Addresses

# import re

# pattern = r"[^@]+@[^@]+\.[^@]+"
# text = "My email is example@domain.com"
# match = re.search(pattern, text)
# if match:
#     print(f"Found email: {match.group()}")
# else:
#     print("No email found")
# This regular expression matches text that contains an "@" symbol with some text before and after it, followed by a period (.) and some characters.

# Example 2: Matching Phone Numbers

# import re

# pattern = r"\(\d{3}\) \d{3}-\d{4}"
# text = "My phone number is (123) 456-7890."
# match = re.search(pattern, text)
# if match:
#     print(f"Found phone number: {match.group()}")
# else:
#     print("No phone number found")
# This regular expression looks for a phone number in the format (xxx) xxx-xxxx.

# Example 3: Matching Dates (DD/MM/YYYY)

# import re

# pattern = r"\d{2}/\d{2}/\d{4}"
# text = "Today's date is 25/12/2021."
# match = re.search(pattern, text)
# if match:
#     print(f"Found date: {match.group()}")
# else:
#     print("No date found")
# This matches dates in the format DD/MM/YYYY.

# 8. Practice Problems with Regex
# Extracting Numbers: Write a program that extracts all the numbers from a given string and returns them as a list.

# Validating Email: Write a program that checks if a given string is a valid email address (simple validation).

# Finding IP Addresses: Write a program that finds all IP addresses in the form of xxx.xxx.xxx.xxx in a given string.

# Password Validation: Write a program that checks if a given string is a valid password. The password must meet these conditions:

# At least 8 characters long
# Contains at least one uppercase letter
# Contains at least one digit
# Contains at least one special character (e.g., @, #, !)
# Recap of Regular Expressions:
# Regular expressions provide powerful tools for searching, matching, and manipulating text.

# The re module is used for working with regex patterns.

# Key functions:

# re.search(): Finds the first match.
# re.match(): Checks if the pattern matches at the start of the string.
# re.findall(): Returns all matches.
# re.sub(): Replaces patterns in the string.
# Regex Syntax:

# Special characters like ^, $, ., *, +, and \d define patterns.
# You can create complex patterns to match various text structures (emails, phone numbers, dates, etc.).
# Next Steps:
# Practice solving problems using regular expressions.
# Try to implement more complex patterns for text validation and extraction.
# Work on real-world use cases like validating inputs or processing log files.
# Let me know when you're ready for the next topic or if you'd like more examples and practice exercises!


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # Test the function
# number = 5
# print(f"The factorial of {number} is {factorial(number)}")

# Exercise 2: Check Prime Number

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# # Test the function
# number = 7
# print(f"Is {number} a prime number? {is_prime(number)}")
# Explanation: The function checks if the given number is divisible by any number between 2 and itself, and if so, it’s not prime.

# Exercise 3: Print Fibonacci Sequence Using Loops

# def fibonacci(n):
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         next_term = fib_sequence[i-1] + fib_sequence[i-2]
#         fib_sequence.append(next_term)
#     return fib_sequence

# # Test the function
# terms = 10
# print(f"The first {terms} terms of Fibonacci sequence: {fibonacci(terms)}")
# Explanation: This function generates the Fibonacci sequence using a loop, where each term is the sum of the two preceding terms.

# Exercise 4: Simple Voting System

# def voting_system(votes):
#     candidate_1 = 0
#     candidate_2 = 0
#     for vote in votes:
#         if vote == 1:
#             candidate_1 += 1
#         elif vote == 2:
#             candidate_2 += 1
#     return candidate_1, candidate_2

# # Test the function
# votes = [1, 2, 1, 1, 2, 1, 2, 2, 1]
# c1, c2 = voting_system(votes)
# print(f"Candidate 1 received {c1} votes.")
# print(f"Candidate 2 received {c2} votes.")


# 1. math Library
# The math module provides mathematical functions like square roots, trigonometric functions, and constants like pi and e.

# import math
# # Square root
# num = 16
# print(f"The square root of {num} is {math.sqrt(num)}")

# # Factorial
# print(f"The factorial of 5 is {math.factorial(5)}")

# # Pi constant
# print(f"The value of pi is approximately {math.pi}")

# Key Functions:
# math.sqrt(x): Returns the square root of x.
# math.factorial(x): Returns the factorial of x.
# math.pi: Returns the mathematical constant pi.

# 2. datetime Library
# The datetime module is used for working with dates and times.

import datetime

# # Get the current date and time
# now = datetime.datetime.now()
# print(f"Current date and time: {now}")

# # Get the current date
# current_date = datetime.date.today()
# print(f"Today's date: {current_date}")

# # Create a specific date
# specific_date = datetime.date(2025, 1, 1)
# print(f"Specific date: {specific_date}")

# Key Functions:
# datetime.now(): Returns the current date and time.
# date.today(): Returns the current date.
# datetime(year, month, day): Creates a specific date object.

# 3. random Library
# The random module provides functions for generating random numbers and performing random actions.

# import random

# # Generate a random number between 1 and 10
# random_num = random.randint(1, 10)
# print(f"Random number between 1 and 10: {random_num}")

# # Choose a random item from a list
# items = ['apple', 'banana', 'cherry']
# random_item = random.choice(items)
# print(f"Random item from the list: {random_item}")

# Key Functions:
# random.randint(a, b): Returns a random integer between a and b.
# random.choice(sequence): Returns a randomly chosen element from a sequence.

# 4. os Library
# The os module provides functions for interacting with the operating system, such as reading and writing to files, changing directories, and checking file properties.

#import os
# # Get the current working directory
#current_dir = os.getcwd()
# print(f"Current working directory: {current_dir}")

# # List all files and directories in the current directory
# files = os.listdir(current_dir)
# print(f"Files and directories: {files}")

# # Create a new directory
# new_dir = "new_folder"
# os.mkdir(new_dir)
# print(f"Created directory: {new_dir}")

# Key Functions:
# os.getcwd(): Returns the current working directory.
# os.listdir(path): Returns a list of files and directories in a given path.
# os.mkdir(path): Creates a directory.


