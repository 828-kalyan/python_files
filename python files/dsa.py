# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class singleLinkedList:
#     def __init__(self):
#         self.head = None
        
#     def insert_at_beg(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
        
#     def insert_at_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
        
#     def insert_at_pos(self,prev_data,data):
#         currnt = self.head
#         while currnt and currnt.data != prev_data:
#             currnt = currnt.next
#         if not currnt:
#             print("element not found")
#             return
#         new_node = Node(data)
#         new_node.next = currnt.next
#         currnt.next = new_node
        
#     def delete(self,key):
#         currnt = self.head
#         if currnt and currnt.data == key:
#             self.head = currnt.next
#             currnt = None
#             return
        
#         prev = None
#         while currnt and currnt.data != key:
#             prev = currnt
#             currnt = currnt.next
#         if not currnt:
#             print(f"Node with data {key} not found.")
#             return
#         prev.next = currnt.next
#         currnt = None
        
#     def reverse(self):
#         prev = None
#         currnt = self.head
#         while currnt:
#             next_node = currnt.next
#             currnt.next = prev
#             prev = currnt
#             currnt = next_node
#         self.head = prev
    
#     def display(self):
#         currnt = self.head
#         elements = []
#         while currnt:
#             elements.append(currnt.data)
#             currnt = currnt.next
#         print("Linked list:",elements)
        
#     def length(self):
#         currnt = self.head
#         count = 0
#         while currnt:
#             count += 1
#             currnt = currnt.next
#         print(count)
        
#     def detect_cycle(self):
#         slow_ptr = fast_ptr = self.head
#         while fast_ptr and fast_ptr.next:
#             slow_ptr = slow_ptr.next
#             fast_ptr = fast_ptr.next.next
#         if slow_ptr == fast_ptr:
#             return True
#         else:
#             return False
    
#     def find_middle(self):
#         slow_ptr = fast_ptr = self.head
#         while fast_ptr and fast_ptr.next:
#             slow_ptr = slow_ptr.next
#             fast_ptr = fast_ptr.next.next
#         if slow_ptr:
#             return slow_ptr.data
#         else:
#             return False

            
# sll = singleLinkedList()
# sll.insert_at_end(1)
# sll.insert_at_end(2)
# sll.insert_at_end(3)
# sll.insert_at_beg(0)
# sll.insert_at_pos(1,4)
# sll.display()
# print("Length:", sll.length())  
# sll.delete(2)
# sll.display()         # Output: Linked List: [0, 1, 2, 3]
# sll.reverse()
# sll.display()
# x = sll.find_middle()
# print(x)

# if sll.detect_cycle():
#     print("Cycle detected")
# else:
#     print("No cycle detected")

#double linked list
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
# class doubleLinkedList:
#     def __init__(self):
#         self.head = None 
#     def insert_at_begin(self,data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node

#     def insert_at_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node
#             new_node.prev = temp

#     def delete(self,key):
#         temp = self.head
#         if temp is None:
#             return
#         if self.head == key:
#             if temp.next:
#                 temp.next.prev = None
#             self.head = temp.next
#             temp = None
#             return
        
#         while temp:
#             if temp.data == key:
#                 break
#             if temp is None:
#                 return
#         if temp.next:  
#             temp.next.prev = temp.prev  
#         if temp.prev:  
#             temp.prev.next = temp.next  
#         temp = None 
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end = " <--> ")
#             temp =  temp.next
#         print(None)
#     def reverse(self):
#         temp = self.head
#         if temp is None:
#             print("List is empty")
#         while temp.next:
#             temp = temp.next
#         while temp:
#             print(temp.data,end=" <--> ")
#             temp =temp.prev
#         print(None)

# dll = doubleLinkedList()
# dll.insert_at_begin(10)
# dll.insert_at_end(20)
# dll.insert_at_end(30)
# dll.insert_at_end(40)
# dll.insert_at_end(50)
# dll.display()

            
#Circular linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class CircularLinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_begin(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             new_node.next = self.head
#         else:
#             new_node.next = self.head
#             temp = self.head
#             while temp.next != self.head:
#                 temp = temp.next
#             temp.next = new_node
#             self.head = new_node
#     def insert_at_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             new_node.next = self
#         else:
#             temp = self.head
#             while temp.next != self.head:
#                 temp = temp.next
#             temp.next= new_node
#             new_node.next = self.head
#     def delete(self,key):
#         if self.head is None: 
#             return
#         temp = self.head
#         prev = None

#         if temp.data == key:
#             if temp.next == self.head:  # only one node in the list
#                 self.head = None
#             else:
#                 while temp.next != self.head:  # find the last node
#                     temp = temp.next
#                 temp.next = self.head.next  # last node points to the second node
#                 self.head = self.head.next  # head points to the next node
#             return

#         # search for the node to delete
#         while temp.next != self.head:
#             prev = temp
#             temp = temp.next
#             if temp.data == key:
#                 prev.next = temp.next  # previous node points to the next node
#                 return
        
#         # if key is not found
#         if temp.data == key:
#             prev.next = temp.next 
#     def reverse(self):
#         if self.head is None or self.head.next == None:
#             return
#         prev = None
#         current = self.head
#         next_node = None

#         while current.next != self.head:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node

#         current.next = prev
#         self.head.next = current
#         self.head = current 

#     def display(self):
#         if self.head == None:
#             print("List is empty")
#             return
        
#         temp = self.head
#         while temp:
#             print(temp.data, end = " --> ")
#             temp = temp.next
#             if temp == self.head:
#                 break
#         print()
    
# cll = CircularLinkedList()
# cll.insert_at_begin(1)
# cll.insert_at_end(2)
# cll.insert_at_end(3)
# cll.display()
# cll.reverse()
# cll.display()

#stack
# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         if self.is_empty():
#             print("stack is empty")
#         else:
#             return self.stack.pop()
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             raise IndexError ("peek from empty stack")
#     def display(self):
#         return self.stack
#     def size(self):
#         return len(self.stack)
#     def is_empty(self):
#         return len(self.stack) == 0
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.display()) 
# print(s.pop()) 
# print(s.size())

#stack using linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None 
# class stack:
#     def __init__(self):
#         self.top = None 
#     def push(self,data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node
#     def pop(self):
#         if self.is_empty():
#             print("Stack is empty")
#         else:
#             poped_ele =self.top.data
#             self.top = self.top.next
#             return poped_ele
#     def is_empty(self):
#         return self.top is None 
#     def peek(self):
#         if self.is_empty():
#             print("stack is empty")
#         else:
#             return self.top.data
#     def display(self):
#         arr = []
#         current= self.top
#         if self.is_empty():
#             print("No elements found")
#         else:
#             while current:
#                 arr.append(current.data)
#                 current = current.next
#             return arr 
#     def count(self):
#         c = 0
#         current = self.top
#         while current:
#             c += 1
#             current = current.next
#         return c 
# s = stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)

# print("Stack after pushing elements:", s.display())
# print("Top element:", s.peek())
# print("Popped element:", s.pop())
# print("Stack after popping:", s.display())

#queue using array
# class Queue:
#     def __init__(self):
#         self.queue = []
#     def is_empty(self):
#         return len(self.queue) == 0 
#     def enqueue(self,data):
#         self.queue.append(data)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         else:
#             raise IndexError("Queue is empty")
#     def front(self):
#         return self.queue[0]
#     def rear(self):
#         return self.queue[-1]
#     def display(self):
#         return self.queue
#     def size(self):
#         return len(self.queue)

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print("Eleents: ",q.display())
# print("Size: ",q.size())
# print("dequeue element: ",q.dequeue())
# print("After dequeue: ",q.display())

#queue using linked list
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None;
# class Queue:
#     def __init__(self):
#         self.front = None 
#         self.rear = None
#         self.size = 0   
#     def is_empty(self):
#         return self.size == 0
    
#     def enqueue(self,item):
#         new_node = Node(item)
#         if self.is_empty():
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#         self.size += 1

#     def dequeue(self):
#         if not self.is_empty():
#             pop_item = self.front.data
#             self.front = self.front.next
#             if self.front is None:
#                 self.rear = None
#                 return pop_item
#             self.size += 1
#         else:
#             raise IndexError("dequeue from empty queue")
        
#     def front_value(self):
#         if not self.is_empty():
#             return self.front.data
#         else:
#             raise IndexError ("Queue is empty")
#     def display(self):
#         if not self.is_empty():
#             current = self.front
#             queue_elements = []
#             while current:
#                 queue_elements.append(str(current.data))  
#                 current = current.next
#             print("Queue: " + " -> ".join(queue_elements))  
#         else:
#             print("Queue is empty.") 
#     def size(self):
#         return self.size

# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.display()  # Output: Queue: 10 -> 20 -> 30

# print(queue.dequeue())       # Output: 10
# queue.display()              # Output: Queue: 20 -> 30
# queue.enqueue(40)
# queue.display()        

#stack using queues
# from queue import Queue

# class StackUsingQueues:
#     def __init__(self):
#         self.q1 = Queue()  # First queue
#         self.q2 = Queue()  # Second queue

#     def push(self, x):
#         # Push element onto stack
#         self.q1.put(x)

#     def pop(self):
#         if self.q1.empty():
#             raise IndexError("pop from empty stack")

#         # Move all elements except the last one from q1 to q2
#         while self.q1.qsize() > 1:
#             self.q2.put(self.q1.get())

#         # The last element in q1 is the element to pop
#         popped_value = self.q1.get()

#         # Swap q1 and q2 so that q1 is ready for the next operations
#         self.q1, self.q2 = self.q2, self.q1

#         return popped_value

#     def top(self):
#         if self.q1.empty():
#             raise IndexError("top from empty stack")

#         # Move elements to q2, but keep the last element in q1 as the "top"
#         while self.q1.qsize() > 1:
#             self.q2.put(self.q1.get())

#         top_value = self.q1.get()

#         # Put it back into q1 since it's the top element
#         self.q2.put(top_value)

#         # Swap q1 and q2 to maintain the structure
#         self.q1, self.q2 = self.q2, self.q1

#         return top_value

#     def is_empty(self):
#         return self.q1.empty()

#     def size(self):
#         return self.q1.qsize()

# # Example Usage:
# stack = StackUsingQueues()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.pop())  # Output: 30
# print(stack.top())  # Output: 20
# print(stack.pop())  # Output: 20


#queue using stacks
# class QueueUsingStacks:
#     def __init__(self):
#         self.stack1 = []  # First stack for enqueue operation
#         self.stack2 = []  # Second stack for dequeue operation

#     def enqueue(self, x):
#         # Push element to the end of the queue (push onto stack1)
#         self.stack1.append(x)

#     def dequeue(self):
#         if not self.stack2:
#             if not self.stack1:
#                 raise IndexError("dequeue from empty queue")
            
#             # Move all elements from stack1 to stack2, reversing the order
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
        
#         # Pop the top element from stack2, which is the front of the queue
#         return self.stack2.pop()

#     def front(self):
#         if not self.stack2:
#             if not self.stack1:
#                 raise IndexError("front from empty queue")

#             # Move all elements from stack1 to stack2 to access the front element
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())

#         return self.stack2[-1]  # Return the front element

#     def is_empty(self):
#         return len(self.stack1) == 0 and len(self.stack2) == 0

#     def size(self):
#         return len(self.stack1) + len(self.stack2)

# # Example Usage:
# queue = QueueUsingStacks()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# print(queue.dequeue())  # Output: 10
# print(queue.front())    # Output: 20
# print(queue.dequeue())  # Output: 20

# #binary tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = TreeNode(data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def find(self, data):
        return self._find(self.root, data)

    def _find(self, node, data):
        if not node or node.data == data:
            return node
        if data < node.data:
            return self._find(node.left, data)
        return self._find(node.right, data)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# Example usage:
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(2)
bt.insert(7)

print("Inorder Traversal:", end=' ')
bt.inorder(bt.root)
print()

print("Preorder Traversal:", end=' ')
bt.preorder(bt.root)
print()

print("Postorder Traversal:", end=' ')
bt.postorder(bt.root)
print()

bt.delete(7)
print("After deleting 7, Inorder Traversal:", end=' ')
bt.inorder(bt.root)
print()




