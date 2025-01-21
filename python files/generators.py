# What is a Generator?
# A generator is a special kind of function that yields values one at a time, instead of returning them all at once. 
# This allows you to iterate over potentially large datasets without using a lot of memory.

# def fun():
#     yield 1
#     yield 2
#     yield 3

# gen = fun()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for i in fun():
#     print(i)

#we can use mix of next and for loop
# def fun():
#     yield 1
#     yield 2
#     yield 3
# gen = fun()
# print(next(gen)) #ouput: 1
# for i in gen:
#     print(i) #2 and 3

# def simple_generator():
#     for i in range(1,6):
#         yield i

# gen = simple_generator()
# for x in gen:
#     print(x)

# def infinete_generator():
#     n = 0
#     while True:
#         yield n 
#         n += 2 
# gen = infinete_generator()
# for _ in range(10):
#     print(next(gen)) 

# def large_nums():
#     for i in range(1,100000000000):
#         yield i 

# for x in large_nums():
#     print(x)
#     if x == 10:
#         break

# def fib_gen():
#     a,b = 0,1
#     while True:
#         yield a 
#         a,b = b, a+b 
# gen = fib_gen()
# for _ in range(10):
#     print(next(gen))

# Chaining Generators
# def numbers():
#     for i in range(1, 11):
#         yield i

# def squares(gen):
#     for num in gen:
#         yield num**2

# # Chaining generators
# for square in squares(numbers()):
#     print(square)

#Generator with State
# def fun(state):
#     while state > 0:
#         yield state
#         state -= 1
#     yield "done"

# for x in fun(5):
#     print(x)

# def fun():
#     total = 0
#     while True:
#         num = yield total
#         if num is None:
#             continue
#         total += num 

# gen = fun()
# print(next(gen))
# print(gen.send(10))
# print(gen.send(20))
# print(gen.send(100))

# def fib(num):
#   a,b = 0,1
#   for i in range(num):
#         print(a)
#         a,b = b, a+b

# fib(5)

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(5))

# for i in range(6):
#     print(fib(i),end=" ")
