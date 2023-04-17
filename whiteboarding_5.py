""" #1
Define a Queue class and implement the following methods: __init__, enqueue, dequeue, and is_empty. Specify the runtime of all methods except __init__.

Bonus: How can we implement the queue so that all three runtimes are O(1)?
"""
from collections import deque

class Queue:

  def __init__(self):
    self.items = deque()
    # self.items = []

  def enqueue(self, data):
    self.items.appendleft(data)
    # self.items.append(data)
    # runtime = O(1)

    # self.items.insert(0, data)
    #runtime = O(n)

  def dequeue(self):
    if self.is_empty():
      return None
    
    self.items.popleft()
    # runtime O(1)

    # return self.items.pop(0)
    # runtime = O(n)

  def is_empty(self):
    return self.items == []
    # runtime = O(1)
    
    # if d:
    #   return False
    # else:
    #   return True


""" #2
Part 1: Define a class for a linked list node.

Part 2: Write a function that takes in the head node of a linked list and prints the data of every node in the list.
"""
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def __repr__(self):
    return f"Node object. Data: {self.data}. Next node = {self.next}"


def print_linked_list(head):
  current = head
  while current is not None:
    print(current.data)
    current = current.next

class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def append_node(self, node):
    if self.head == None:
      self.head = node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = node

  def print_nodes(self):
    if self.head == None:
      return "Empty list"
      
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next

  def __repr__(self):
    return f"Linked List object. Head node: {self.head}"


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c

new_ll = LinkedList()
new_ll.append_node(a)
new_ll.append_node(b)
new_ll.append_node(c)


""" #3
Here’s a snippet from a linked list class:

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Write a method called print_odd_nodes that prints the nodes with odd-numbered indices (1, 3, 5, …, etc.)

Hint 1:
Linked lists don’t have indices by default. You’ll have to come up with another way to detect if a node is odd-numbered or not.
Hint 2:
Can you use a counter variable to do this?
"""

def print_odd_nodes(self):
  i = 0
  curr = self.head

  while curr is not None:
    if i % 2 != 0:
        print(curr.data)

    curr = curr.next
    i += 1


""" #4
Write a method for this class called append. It should take in a node instance and add it to the end of the linked list.

Remember to account for appending to an empty list.
"""

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, node):
      # is list empty? --self.tail = None
      
      if self.tail is not None:
        self.tail.next = self.tail = node
        # self.tail.next = node
        # self.tail = node

      else:

        self.head = self.tail = node
        
        
""" #5
Here’s a snippet from a linked list class:

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Write a method for this class called append. It should take in a node instance and add it to the end of the linked list.

Remember to account for appending to an empty list.

Hint 1:
Your linked list has a pointer to its tail.
Hint 2:
Have you tried drawing a diagram of a linked list?
Hint 3:
If self.tail is None, that means the list is empty. In this case, you should update self.tail and self.head so they point to the node you want to append.

Otherwise, self.tail.next should point to the node you want to append. Then, update self.tail so it points to the correct node.
"""

def append(self, node):
  
  if not self.head:
    self.head = node
    self.tail = node
    
  else:
    self.tail.next = node
    self.tail = node
    

def append2(self, node):
  
  if self.tail is None:
    self.tail = self.head = node
    
  else:
    self.tail.next = node
    self.tail = node