# f =open("demo.txt",'w')
# f.write("Woops! I have deleted the content!")
# f.close()

# f = open("demo.txt",'r')
# print(f.read(10))

# f = open("myfile.txt",'w')
# f.write("File handling in Python is an essential skill for reading, \n writing, and managing files. \n Here's a comprehensive guide to file handling, \nstarting from the basics and moving to advanced concepts, along with example problems.")
# f.close()

# with open("myfile.txt",'r') as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     f.close()

# with open("myfile.txt",'w') as f:
#     f.write("""
#             File handling in Python is an essential skill for reading, 
#             writing, and managing files. 
#             Here's a comprehensive guide to file handling, 
#             starting from the basics and moving to advanced concepts, along with example problems.
#             I am learning file handling
#             """)
#     f.close()

# with open("Myfile.txt",'r') as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     f.close()

# with open("myfile.txt",'r') as f:
#     for x in f:
#         print(x)

# import os 
# if os.path.exists("dummy"):
#     os.remove("dummy")
# else:
#     print("File not found")

# with open("output.bin", "wb") as file:
#     file.write(b"Binary data")

# f = open("output.bin",'r')
# print(f.read())

#import csv
# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age"])
#     writer.writerow(["Alice", 25])

# f = open("data.csv",'r')
# x = csv.reader(f)
# for row in x:
#     print(row)


# import json
# with open("data.json", "w") as file:
#     json.dump({"name": "Alice", "age": 25}, file)

# with open("data.json",'r') as file:
#     data = json.load(file)
#     print(data)

#Write a program to count the number of words in a file.
# def word_count(filename):
#     try:
#         with open("myfile.txt",'r') as f:
#             text = f.read()
#             words = text.split()
#             return (len(words))
#     except FileNotFoundError as e:
#         print(f"{e}")
# f = "myfile.txt"
# print("no of words:",word_count(f))

#Append a new line to an existing file without overwriting its content.
# def append_newline(filename,line):
#     try:
#         with open("demo.txt",'a') as file:
#             file.write( '\n' + line)
#     except FileNotFoundError:
#         print("File not found")
# f = 'demo.txt'
# append_newline(f,"This is a new line.")
# print("appended successfully")

#Reverse File Content
# f = open("myfile.txt",'r')
# x = f.read()

# file = open("newfile.txt",'w')
# file.write(x[::-1])

# file = open("newfile.txt",'r')
# print(file.read())

#Count Lines, Words, and Characters
# line_count = 0
# word_count = 0
# char_count = 0
# f = open("demo.txt",'r')
# for x in f:
#     line_count += 1
#     words = x.split()
#     word_count += len(words)
#     char_count += len(x)
# print("line count:" ,line_count,"Word count: ",word_count,"char count: ",char_count)

#Merge Two Files
# f = open("demo.txt",'r')
# c1 = f.read()
# f2 = open("myfile.txt",'r')
# c2 = f2.read()

# n = open("merged.txt",'w')
# n.write(c1 + c2)
# x = open("merged.txt",'r')
# print(x.read())

#Find and Replace
# serach_word = "line"
# new_word = "text"
# f = open("demo.txt",'r')
# c = f.read()

# updated_text = c.replace(serach_word,new_word)
# with open("example_updated.txt", "w") as updated_file:
#     updated_file.write(updated_text)

# with open("example_updated.txt", "r") as updated_file:
#     print(updated_file.read())

#Detect and Remove Blank Lines
# with open("demo.txt",'r') as inline , open("new.txt",'w') as out:
#     for x in inline:
#         if x.strip():
#             out.write(x)

# with open("new.txt",'r') as file:
#     print(file.read())