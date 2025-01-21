#list comprehensions

#[expression for item in iterable]
#ex:
#squares = [x ** 2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]

#When you add a condition, the structure becomes:
#syntax
#[expression for item in iterable if condition]
#example:
# even_sqaures = [x**2 for x in range(10) if x%2==0]
# [0, 4, 16, 36, 64]


#What Happens When You Add Multiple Loops?
#If you have nested loops, the order changes slightly. You have to write the inner loop first, then the outer loop.

#[expression for item1 in iterable1 for item2 in iterable2]
#The inner loop comes before the outer loop.

# pairs = [(x, y) for x in range(2) for y in range(2)]
# print(pairs)
# Output: [(0, 0), (0, 1), (1, 0), (1, 1)]


# Combining Loops and Conditions
# You can also have conditions along with multiple loops, and the condition will always be placed after all the loops.

# [expression for item1 in iterable1 for item2 in iterable2 if condition]
#p = [(x,y) for x in range(3) for y in range(3) if x+y < 3]
#output : [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]

# [expression_if_true if condition else expression_if_false for item in iterable]

# numbers = [1, 2, 3, 4, 5]
# result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
# Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']


#basic 

# Create a list of squares of numbers from 0 to 9.
# s = [x**2 for x in range(10)]
# print(s) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list of all even numbers between 1 and 20.
# even_nums = [x for x in range(20) if x%2==0]
# print(even_nums) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Create a list of all numbers divisible by 3 from 1 to 30.
# odd = [x for x in range(30) if x%3==0]
# print(odd) #[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

#intermediate

# Create a list of the first 10 positive integers, each raised to the power of 3.
# s = [x**3 for x in range(10)]
# print(s) #[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Create a list of tuples (x, y) where x is from 0 to 2 and y is from 3 to 5.
# s = [(x,y) for x in range(2) for y in range(3,5)]
# print(s)

# Create a list of the strings "even" or "odd" for numbers from 1 to 10, depending on whether the number is even or odd.
# s = ['even' if x%2==0 else "odd" for x in range(10)]
# print(s)

#advanced 

# Create a list of all pairs (x, y) where x is from 0 to 2 and y is from 0 to 2, and the sum x + y is greater than 2.
# s = [(x,y) for x in range(3) for y in range(3) if x+y > 2]
# print(s)

# Create a list of squares of even numbers from 0 to 20.
# s = [x**2 for x in range(20) if x%2==0]
# print(s)

# Create a list of numbers from 1 to 10 where the number is divisible by both 2 and 3.
# s = [x for x in range(10) if x %2 ==0 and x%3==0]
# print(s)

# Create a list of strings that are palindromes from a given list of words: ["madam", "hello", "racecar", "world", "level"].
# words= ["madam", "hello", "racecar", "world", "level"]
# s = [x for x in words if x == x[::-1]]
# print(s)

# Set Comprehension Questions

# 1. Create a set of squares of numbers from 1 to 9.
# Write a set comprehension that generates the squares of numbers from 1 to 9.
# s = {x**2 for x in range(1,10)}
# print(s)

# 2. Create a set of all even numbers between 10 and 30.
# Write a set comprehension that generates all even numbers in the range from 10 to 30.
# s = {x for x in range(10,31) if x % 2 == 0}
# print(s)

# 3. Create a set of all multiples of 5 from 0 to 50.
# Write a set comprehension to generate multiples of 5 between 0 and 50.
# s = {x for x in range(51) if x %5 == 0}
# print(s)

# 4. Create a set of the first 10 numbers that are divisible by both 3 and 4.
# Write a set comprehension to find numbers that are divisible by both 3 and 4 from 0 to 100.
# s = {x for x in range(100) if x %3 ==0 and x%4==0}
# print(s)

# 5. Create a set of the first 10 positive numbers whose square is greater than 50.
# Write a set comprehension to return numbers whose square is greater than 50 and is less than 100.
# s = {x for x in range(18) if x**2 > 50}
# print(s)

# Dictionary Comprehension Questions

# 6. Create a dictionary with numbers from 1 to 5 as keys and their squares as values.
# Write a dictionary comprehension where the key is a number from 1 to 5, and the value is its square.
# d = {x:x**2 for x in range(1,6)}
# print(d)

# 7. Create a dictionary where the keys are names of countries and the values are their capital cities.
# Given a list of country-capital pairs, create a dictionary comprehension to store this data.
# Example list: countries = [("USA", "Washington, D.C."), ("France", "Paris"), ("Japan", "Tokyo")].
# c = [("USA", "Washington, D.C."), ("France", "Paris"), ("Japan", "Tokyo")]
# d = {a:b for a,b in c}
# print(d)

# 8. Create a dictionary where the keys are characters from a string and the values are the frequency of each character in that string.
# Write a dictionary comprehension that counts how many times each character appears in the string "hello world".
# s = "hello world"
# d = {char: s.count(char) for char in s}  
# print(d)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# 9. Create a dictionary where the keys are words and the values are the lengths of those words.
# Write a dictionary comprehension to generate a dictionary where the keys are words from the list 
# ["apple", "banana", "cherry"], and the values are the lengths of those words.
# words = ["apple", "banana", "cherry"]
# d = {x:len(x) for x in words}
# print(d)

# 10. Create a dictionary where the keys are integers from 1 to 10, and the values are their cubes.
# Write a dictionary comprehension to return the cubes of numbers from 1 to 10.

# d = {x:x**3 for x in range(1,11)}
# print(d)

# Combined (Set & Dictionary) Practice
# 11. Create a dictionary where the keys are integers from 1 to 5, and the values are sets of factors of each key.
# For example, for 1, the set would be {1}, for 2, it would be {1, 2}, for 3, {1, 3}, and so on.
# d = {x:{i for i in range(1,x+1) if x%i==0} for x in range(1,6)}
# print(d)

# 12. Create a set of keys from a dictionary where the values are greater than 50.
# Given the dictionary data = {"a": 40, "b": 60, "c": 100, "d": 30}, 
# write a set comprehension to find all keys where the value is greater than 50.

# data = {"a": 40, "b": 60, "c": 100, "d": 30}
# s = {k for k,v in data.items() if v> 50}
# print(s)

# Extra Challenge
# 13. Create a set of unique letters from a given list of words.
# Given the list words = ["apple", "banana", "cherry", "date"] 
# write a set comprehension to generate a set of unique letters found in all the words.

# words = ["apple", "banana", "cherry", "date"]
# s = {letter for word in words for letter in word}
# print(s)

# 14. Create a dictionary that stores the words as keys and their reversed versions as values.
# Given the list words = ["apple", "banana", "grape"], 
# write a dictionary comprehension to reverse each word and store it as a value in the dictionary, with the original word as the key.
# words = ["apple", "banana", "grape"]
# d = {x:x[::-1] for x in words}
# print(d)





# d = {x:x**2 for x in range(1,11)}
# print(d)

# d = {x:x**2 for x in range(1,11) if x%2==0}
# print(d)

# f = ['apple','banana','cherry']
# d = {x:len(x) for x in f}
# print(d)

# o = {'a':1,'b':2,'c':3}
# d = {v:k for k,v in o.items()}
# print(d)

# keys = ['name','age','gender']
# d ={k:None for k in keys}
# print(d)

# d = {x:'even' if x%2==0 else 'odd' for x in range(1,11)}
# print(d)

# keys = ['name','age','gender']
# values = ['Alice',25,'female']
# d = {k:v for k,v in zip(keys,values)}
# print(d)

# d = {chr(x):x for x in range(65,91)}
# print(d)

# nes = {'a':{'b':1,'c':2},'d':{'e':3,'f':4}}
# d = {x:y for x in nes for y in nes}
# print(d) 

# s = "hello world"
# d = {char: s.count(char) for char in s}  
# print(d)


# Generate squares of numbers from 0 to 9:


# squares = (x**2 for x in range(10))
# print(list(squares))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2. Filtering with if
# Generate even numbers from a range:

# evens = (x for x in range(20) if x % 2 == 0)
# print(list(evens))  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 3. Conditional Expression (if-else)
# Double even numbers and halve odd numbers:


# transformed = (x * 2 if x % 2 == 0 else x / 2 for x in range(10))
# print(list(transformed))  # Output: [0.5, 2, 1.5, 6, 2.5, 10, 3.5, 14, 4.5, 18]

# 4. Nested Loops
# Generate Cartesian product of two ranges:


# cartesian_product = ((x, y) for x in range(3) for y in range(3))
# print(list(cartesian_product))  
# # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 5. Infinite Sequence
# Generate an infinite sequence of squares:


# import itertools
# infinite_squares = (x**2 for x in itertools.count())
# print(next(infinite_squares))  # Output: 0
# print(next(infinite_squares))  # Output: 1
# print(next(infinite_squares))  # Output: 4

# 6. Real-World Example: File Processing
# Read a file and generate lines with specific content:


# lines_with_keyword = (line for line in open('example.txt') if 'keyword' in line)
# for line in lines_with_keyword:
#     print(line.strip())

# 7. Combining with Built-in Functions
# Sum of all squares of even numbers:


# result = sum(x**2 for x in range(10) if x % 2 == 0)
# print(result)  # Output: 120

# 8. Generating Factorials
# Compute factorials lazily:


# import math
# factorials = (math.factorial(x) for x in range(10))
# print(list(factorials))  
# # Output: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# 9. Transforming Data
# Convert a list of strings to uppercase lazily:

# names = ["alice", "bob", "charlie"]
# uppercase_names = (name.upper() for name in names)
# print(list(uppercase_names))  # Output: ['ALICE', 'BOB', 'CHARLIE']

# 10. Combining Multiple Generator Expressions
# Chain generators for more complex transformations:

# numbers = range(10)
# squared_evens = (x**2 for x in (x for x in numbers if x % 2 == 0))
# print(list(squared_evens))  # Output: [0, 4, 16, 36, 64]



# output-> lo=[6, 8, 1, 4, 8, 9, 2] 
# l1=[4,5,6,7,0,0,0]
# l2=[2,3,5,6,7,9,2]

# l = [x for x in zip(l1,l2) for x in x]

# l3 = [l[i] + l[i+1] for i in range(0,len(l)-1,2)]
# #print(l3)
# for i in range(len(l3)-1):
#     if l3[i] > 10:
#         l3[i] = l3[i]-10
#         l3[i+1] = l3[i+1] + 1
# print(l3)
