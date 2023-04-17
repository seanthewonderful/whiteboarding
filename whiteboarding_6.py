"""For all non-binary Tree problems below, assume any Node class to be defined as follows:"""

class Node:
  """Node in a tree."""

  def __init__(self, data, children=None):
      self.data = data
      self.children = children or []
      
      
"""For all Binary Tree problems below, assume the Node class to be defined as follows:"""

class BinarySearchNode:
  """Binary tree node."""

  def __init__(self, data, left=None, right=None):
      self.data = data

      self.left = left
      self.right = right
      
"""Example of how to create a tree to test your code"""
d = Node("D", [])
b2 = Node("B", [])
e = Node("E", [])
b1 = Node("B", [d])
c = Node("C", [b2, e])
root = Node('A', [b1, b2])
      


""" #1
Given a tree Node class, write a method that returns the number of nodes in the tree. (self is the root of the tree).
"""

"""BFS Solution"""
def count_nodes_iterative_bfs(self):
    """Return the number of nodes in the tree using iterative
    breadth first traversal.
    """
    from collections import deque

    count = 0

    to_visit = deque()
    to_visit.append(self)

    while to_visit:
        current = to_visit.popleft()
        count += 1
        for child in current.children:
            to_visit.append(child)

    return count

"""DFS Solution"""
def count_nodes_iterative_dfs(self):
    """Return the number of nodes in the tree using iterative
    depth first traversal.
    """
    count = 0
    to_visit = [self]

    while to_visit:
        current = to_visit.pop()
        count += 1
        to_visit.extend(current.children)

    return count

"""Recursive Solution"""
def count_nodes_recursive(self):
    """Return the number of nodes in the tree using recursion."""

    return 1 + sum([n.count_nodes_recursive() for n in self.children])




""" #2
Given a tree Node class, write a method that takes an item as its only parameter and returns True if the data for any node in the tree matches the given item. Otherwise, it should return False.
"""

"""BFS Solution"""
def tree_contains_iterative_bfs(self, item):
    """Return True if any node's data in the tree matches item."""

    from collections import deque

    to_visit = deque()
    to_visit.append(self)

    while to_visit:
        current = to_visit.popleft()
        if current.data == item:
            return True
        for child in current.children:
            to_visit.append(child)

    return False
    
"""DFS Solution"""
def tree_contains_iterative_dfs(self, item):
    """Return True if any node's data in the tree matches item."""

    to_visit = [self]

    while to_visit:
        current = to_visit.pop()
        if current.data == item:
            return True

        to_visit.extend(current.children)

    return False

"""Recursive Solution"""
def tree_contains_recursive(self, item):
    """Return True if any node's data in the tree matches item."""

    if self.data == item:
        return True
    elif self.children:
        return any([n.tree_contains_recursive(item) for n in self.children])
    else:
        return False
    
    
    
    
""" #3
Given a tree Node class, write a method that takes an item as its only parameter and returns the highest ranking node whose data matches the given item. (If there are no matching nodes, it should return None).
"""

def find_highest_ranking(self, item):
    """Find the highest ranking matching node in the tree."""

    from collections import deque

    to_visit = deque()
    to_visit.append(self)

    while to_visit:
        current = to_visit.popleft()
        if current.data == item:
            return current
        for child in current.children:
            to_visit.append(child)

    return None



""" #4
Given a BinarySearchNode class, write a method that takes an item as its only parameter and returns the node in the BST whose data matches the given parameter. Be sure to discuss the runtime complexity of your solution.
"""

"""Non-recursive"""
def find_iterative(self, data_to_find):
    """Return node with this data. Return None if not found."""

    current = self

    while current:
        if current.data == data_to_find:
            return current

        elif data_to_find < current.data:
            current = current.left

        elif data_to_find > current.data:
            current = current.right

    return None
    
"""Recursive"""
def find_recursive(self, data_to_find):
    """Return node with this data. Return None if not found."""

    if self.data == data_to_find:
        return self
    elif data_to_find < self.data and self.left is not None:
        return self.left.find_recursive(data_to_find)
    elif data_to_find > self.data and self.right is not None:
        return self.right.find_recursive(data_to_find)
    else:
        return None
        
        

""" #5
Given a tree Node class, write a method that takes an item and a node as its two parameters, and adds the new node as a child of the first node in the tree whose data matches the given item.

(You may assume that there are no nodes with duplicate data in the tree, or you may decide to define “first node” using breadth-first or depth-first search, or your interviewer may decide for you).
"""

def insert_new_node(self, item, new_node):
    """Insert the given node as a child of the first node whose data
    matches item. Return True if successful, False otherwise."""

    from collections import deque

    to_visit = deque()
    to_visit.append(self)

    while to_visit:
        current = to_visit.popleft()
        if current.data == item:
            current.children.append(new_node)
            return True
        for child in current.children:
            to_visit.append(child)

    return False


""" #6
Given a BinarySearchNode class, write a method that returns the total number of nodes in the tree.
"""

"""Non-recursive"""
def count_total_nodes_iterative(self):
    """Count the overall number of nodes."""

    # This code is essentially an iterative BFS traversal, but we have to
    # do a slightly more complex version of to_visit.extend()
    if self is None:
        return 0

    count = 0

    to_visit = [self]

    while to_visit:
        current = to_visit.pop()
        count += 1
        if current.left is not None:
            to_visit.append(current.left)
        if current.right is not None:
            to_visit.append(current.right)

    return count        


"""Recursive"""
def count_total_nodes_recursive(self):
    """Count the overall number of nodes."""

    # Count nodes in left subtree:
    if self.left is None:
        left_total = 0
    else:
        left_total = self.left.count_total_nodes_recursive()

    # Count nodes in right subtree:
    if self.right is None:
        right_total = 0
    else:
        right_total = self.right.count_total_nodes_recursive()

    # Total number of nodes in tree is current node plus sizes of left
    # and right subtrees
    return 1 + left_total + right_total



""" #7
Given a tree Node class, write a method that takes an item as its only parameter and returns the lowest ranking node whose data matches the given item.
"""

def find_lowest_ranking(self, item):
    """Find the lowest ranking matching node in the tree."""

    from collections import deque

    to_visit = deque()
    to_visit.append(self)

    found = None

    while to_visit:
        current = to_visit.popleft()
        if current.data == item:
            found = current
        for child in current.children:
            to_visit.append(child)

    return found


""" #8
Given a tree Node class, write a method that takes an item as its only parameter and removes any nodes in the tree whose data matches the given item. Question: what happens to the deleted node’s children?
"""

"""Non-destructive"""
def remove_nodes_non_destructive(self, item):
    """Remove any nodes in the tree whose data matches the given item."""

    from collections import deque

    to_visit = deque()
    to_visit.append(self)

    while to_visit:
        current = to_visit.popleft()
        for child in current.children:
            if child.data == item:
                current.children.remove(child)
                current.children.extend(child.children)
        for child in current.children:
            to_visit.append(child)


"""Destructive"""
def remove_nodes_destructive(self, item):
    """Remove any nodes in the tree whose data matches the given item."""

    from collections import deque

    to_visit = deque()
    to_visit.append(self)

    while to_visit:
        current = to_visit.popleft()
        for child in current.children:
            if child.data == item:
                current.children.remove(child)
        for child in current.children:
            to_visit.append(child)