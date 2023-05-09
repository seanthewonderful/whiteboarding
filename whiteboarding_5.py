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
    
    def __str__(self):
        return str(self.data)
      
    def __repr__(self):
        return f"<Node object. Data: {self.data}. Next node = {self.next}>"


def print_linked_list(head):
  current = head
  while current is not None:
    print(current.data)
    current = current.next



class LinkedListNoTail:
    """Create a new Linked List with a head"""
    
    def __init__(self, head=None):
        """Initialize a new Linked List"""
        
        self.head = head
    
    def print_list(self):
        """Print all items in the list"""
        # Want to keep track of current node, reset in loop
        current = self.head
        
        while current:
            print(current)
            current = current.next
            
    def find(self, value):
        """Return T/F whether a value exists in LL"""
        current = self.head
        
        while current:
            if current.data == value:
                return True
            current = current.next
            
        return False
            
    def append(self, data):
        """Append new node to end of list"""
        
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        
        else:
            current = self.head
            while current:
                
                if current.next == None:
                    current.next = new_node
                    return
                
                current = current.next
            
    # def append(self, data):
    #     """Append new node to end of list"""
        
    #     new_node = Node(data)
        
    #     current = self.head
        
    #     if not current:
    #         self.head = new_node
        
    #     else:
    #         while current.next:
                
    #             current = current.next
            
    #         current.next = new_node
    
    def remove_node(self, value):
        """Remove a specific node that matches value"""
        
        # Empty LL?
        if not self.head:
            return "List empty"
        
        # head == value?
        if self.head.data == value:
            self.head = self.head.next
            return
        
        # else, let's keep track of where we are
        current = self.head
        
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            
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

  while curr:
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
      
      if self.tail:
        # self.tail.next = self.tail = node
        self.tail.next = node
        self.tail = node

      else:
        self.head = node
        self.tail = node
        # self.head = self.tail = node
        
        
""" #5
Write a function that removes a node with a given value from a singly-linked list. It should return the head node. The function should take in two arguments:

head — the head of a linked list

value — a value that you want to remove

Hint 1:
Remember, head is a Node instance that is assumed to be the head of a linked list.

The nice thing about this is that you don’t have to worry about updating the head/tail of a LinkedList instance.
Hint 2:
Let’s say head.data is equivalent to value. How do we remove head from the linked list? You can remove it by returning head.next from your function.
"""

def remove_value(head, value):
    if head.data == value:
        return head.next

    curr = head
    while curr.next is not None:
        if curr.next.data == value:
            curr.next = curr.next.next
            break

        curr = curr.next

    return head

""" #6
Here’s a snippet from a doubly-linked list class:

class DblLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Write a method for this class called remove. It should take in a node instance and remove it from the list.

Hint 1:
Remember — you already have the node that needs to be removed, which means you can do this in O(1) time.
Hint 2:
You need to update two attributes on the node — node.prev and node.next.
Hint 3:
If node.prev is None, it means node is the head of the list. To remove it, we just need to reassign self.head to the next node.

Otherwise, reassign the previous node’s next attribute to node.next.

If node.next is None, it means node is the tail of the list. To remove it, reassign self.tail to the previous node.

Otherwise, reassign the next node’s next attribute to node.prev.
"""

def remove(self, node):
    if node.prev is None:
        # If node.prev is None, it means this node is the head of
        # the list. To remove it, just reassign self.head to the next
        # node
        self.head = node.next
    else:
        node.prev.next = node.next

    if node.next is None:
        # If node.next is None, it means this node is the tail of
        # the list. To remove it, reassign self.tail to the previous
        # node
        self.tail = node.prev
    else:
        node.next.prev = node.prev

""" #7
Write a function that takes in the head of a singly-linked list. It should return True if two nodes with the same data appear consecutively.

Example test cases:

in: 1 → 2 → 2
out: True

in: 1 → 2 → 1
out: False

Hint 1:
As you iterate through the list, you need to keep a reference to the node before the current one.
"""

def has_consecutive(head):
    if head is None:
        return False

    current = head

    while current.next is not None:
        if current.data == current.next.data:
            return True

        current = current.next
    return False