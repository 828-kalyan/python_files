#creating a thread
# from threading import Thread
# from time import sleep

# def print_num():
#     for i in range(5):
#         print(f"num: {i}")
#         sleep(1)
    
# t1 = Thread(target=print_num)

# t1.start()

# print("main thread continues")

#another method
# from threading import *
# from time import sleep

# class print_num(Thread):
#     def run(self):
#         for i in range(5):
#             print(f"num: {i}")
#             sleep(1)
# t1 = print_num()
# t1.start()

# print("Main thread continues")

#simple example to understand threads
# from threading import *
# from time import sleep
# class hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("HI")
#             sleep(1)
        
# class hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("HELLO")
#             sleep(1)

# t1 = hi()
# t2 = hello()

# t1.start()
# sleep(0.4)
# t2.start()


#Daemon thread
# import threading
# import time

# def background_task():
#     while True:
#         print("Daemon thread running...")
#         time.sleep(1)

# def main_task():
#     for i in range(5):
#         print("Main thread running...")
#         time.sleep(2)

# # Create a daemon thread
# daemon_thread = threading.Thread(target=background_task)
# daemon_thread.setDaemon(True)  # Mark the thread as daemon
# daemon_thread.start()

# # Main task
# main_task()

# # Once the main thread completes, the daemon thread will stop automatically.
# print("Main thread finished. Program exiting.")

#join()
# from threading import Thread
# from time import sleep

# class print_num(Thread):
#     def run(self):
#         for i in range(5):
#             print(f"number:{i}")
#             sleep(1)
# t1 = print_num()
# t1.start()
# t1.join()

# print("Main thred waits until t1 completes")

#daemon threads
# from threading import Thread
# from time import sleep

# def background_task():
#     while True:
#         print("Daemon thread executing.....")
#         sleep(1)

# t1 = Thread(target=background_task,daemon=True)
# t1.start()

# sleep(4)
# print("Main thread finished. Daemon thread stops automatically")

# from threading import Thread, Lock

# lock = Lock()
# counter = 0

# def increment():
#     global counter
#     for _ in range(1000):
#         with lock:  # Ensures only one thread modifies `counter` at a time
#             counter += 1

# t1 = Thread(target=increment)
# t2 = Thread(target=increment)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(f"Final counter value: {counter}")

# from threading import Thread
# from queue import Queue

# queue = Queue()

# def producer():
#     for i in range(5):
#         queue.put(i)
#         print(f"Produced: {i}")

# def consumer():
#     while not queue.empty():
#         item = queue.get()
#         print(f"Consumed: {item}")

# t1 = Thread(target=producer)
# t2 = Thread(target=consumer)

# t1.start()
# t1.join()

# t2.start()
# t2.join()

# def example(*args):
#     print(id(args)) 
#     print(id(args[0])) 
#     print(id(args[1])) 
#     print(id(args[2])) 

# example(1, 2, 3)  




