print('hello world...')
"""
[12:44 PM] Arjun Shome

Problem Statement: Implement a Queue using Stacks


You are required to implement a Queue data structure using two Stacks:


 Your task is to -


 

Create your own Stack classes with it's required methods and attributes

push
pop
peek
is_empty()
size
__str__
implement the Queue class with the following methods:

enqueue(item): Add an element to the end of the queue.
dequeue(): Remove and return the element from the front of the queue. If the queue is empty, return None.

is_empty():  Check if the queue is empty
Please use proper exception handling to handle edge cases.
"""

# class Stack:
#
#
#     def __init__(self,val):
#         self.value = val
#         self.values = []
#
#     def push(self,val):
#         self.values.append(val)
#
#
#     def pop(self):
#         self.values.pop()
#
#     def peek(self):
#         pass
#
#     def is_empty(self):
#         leng = len(self.values)
#         if leng==0:
#             print('list is empty')
#
#     def size(self):
#         temp = self.values
#         leng = len(temp)
#         return leng
#
#     def __str__(self):
#         return str(self.values)
#
# class Queue():
#
#     def __init__(self.val):
#
#     def enqueue(self,val):
#         self.push(val)
#
#     def dequeue(self):
#
#         self.pop()
#         print('we are removing values')
#
#     def is_empty(self):
#         if self.size() ==0:
#             print('queue is empty..')
#         else:
#             print('queue is not empty')
#
#
#
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
#
# queue.dequeue()
# queue.dequeue()
#
# queue.is_empty()



class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class QueueUsingStacks:
    def __init__(self):
        self.stack1 = Stack()  # for enqueue operation
        self.stack2 = Stack()  # for dequeue operation

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            if self.stack1.is_empty():
                return None
            else:
                while not self.stack1.is_empty():
                    self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()


# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued item:", queue.dequeue())  # Output: 1
print("Dequeued item:", queue.dequeue())  # Output: 2

queue.enqueue(4)
print("Is Queue empty?", queue.is_empty())  # Output: False
print("Dequeued item:", queue.dequeue())  # Output: 3
print("Dequeued item:", queue.dequeue())  # Output: 4
print("Is Queue empty?", queue.is_empty())  # Output: True
