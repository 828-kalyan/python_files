#nested func
# def outer():
#     x = 5  #enclosing var
#     def inner():
#         return x 
#     return inner #returing fun reference 

# a = outer()
# print(a)  #prints the adress of fun 
# print(a.__name__) #name of fun which it is refering. o/p: inner

# def outer():
#     x = 5  #enclosing var
#     def inner():
#         return x 
#     return inner() #returing fun

# a = outer()
# print(a)  #prints value of fun 

#func can take fun as a parameter
# def fun1():
#     print("i am fun1")

# def fun2(func):
#     print("i am fun2")
#     func()

# fun2(fun1)

#decorators

# def decorator(func):
#     def inner():
#         s = func()
#         return s.upper()
#     return inner

# def greet():
#     return "Good morning"

# print(greet())
# d =decorator(greet)
# print(d())

# def decorator(func):
#     def inner():
#         s = func()
#         return s.upper()
#     return inner

# @decorator
# def greet():
#     return "good morning"

# print(greet())

# def decorator(fun):
#     def inner(x,y):
#         if y == 0:
#             return "give proper input"
#         return fun(x,y)
#     return inner 
# @decorator
# def div(a,b):
#     return a//b

# print(div(6,2))

#mutiple decorators
# def upper_d(func):
#     def inner():
#         s = func()
#         return s.upper()
#     return inner

# def split_d(func):
#     def wrapper():
#         s1 = func()
#         return s1.split()
#     return wrapper
# @split_d
# @upper_d
# def greet():
#     return "good morning"

# print(greet())

# def outer(expres):
#     def dec(fun):
#         def inner():
#             return fun()  + expres
#         return inner
#     return dec

# @outer('kalyan')
# def greet():
#     return "Good morining "

# print(greet())


# def dec(func):
#     def inner(*args):
#         l1 = []
#         l1 = args[1:]
#         for i in l1:
#             if i == 0:
#                 return "give proper input"
#         return func(*args)
#     return inner

# @dec
# def div(a,b):
#     return a/b
# @dec 
# def div1(a,b,c):
#     return a/b/c

# print(div(4,2))

# print(div1(8,4,2))

#decorators to methods

# def dec(method):
#     def inner(name_ref):
#         if name_ref.name == "kalyan":
#             return "hey both names are same"
#         else:
#             method(name_ref)
#     return inner
    
# class greet:
#     def __init__(self,name):
#         self.name = name 
#     @dec
#     def print_greet(self):
#         print("entered name:",self.name)

# p = greet("kalyan")
# print(p.print_greet())
        
# p1 = greet("Ram")
# p1.print_greet()

#class decorators

# class dec:
#     def __init__(self,fun):
#         self.fun = fun
#     def __call__(self):
#         s = self.fun()
#         return s.upper()
# @dec   
# def greet():
#     return "good morning"

# print(greet())