""" 
Challenge 1:

This is a graph Node class:
"""

class Node:
  #A graph node.#

  def __init__(self, data, adjacent=None):
    self.data = data
    self.adjacent = adjacent or set()
        
class Graph:
    
  def __init__(self):
    self.nodes = set()
     
  def add_node(self, node):
    self.nodes.add(node)
  
  def connect_nodes(self, node1, node2):
    self.add_node(node1)
    self.add_node(node2)
    node1.adjacent.add(node2)
    node2.adjacent.add(node1)
        
"""
Create a Graph class. Graph instances should store all nodes in a graph. It should also have an instance method that adds a Node to the graph and a method that connects two existing Node instances together.

Hint 1: 
You can store all the nodes of a graph in an instance attribute. What would be a good data structure to use in this situation?
Hint 2:
The method that adds a Node to the graph should take in a Node instance.
The method that connects nodes should take in two Node instances. Also, be sure that both nodes have been added to the graph.
"""


""" 
Challenge 2:

Write a function that takes in a Node object and prints all connected nodes.

Bonus: try implementing this recursively.

Hint 1:
The solution is very similar to traversing a tree. The difference is that nodes in a graph can have circular connections.
Hint 2:
You can avoid backtracking by keep track of the nodes you’ve already seen.
"""

def print_nodes(node):
  
  seen = set()
  to_see = [node]
  # to_see = set()
  
  while to_see:
    
    current = to_see.pop(0)
    
    print(current)
    seen.add(current)
    
    for element in current.adjacent:
      
      if element not in seen:
        to_see.append(element)
      
  return 
""" 
Challenge 3:
Write a function that takes in two Node objects and returns True if the nodes are connected to one another.
Bonus: try implementing this recursively.
"""

def connected(node1, node2):
  if node1 in node2.adjacent:
    return True

  checked = set()
  not_checked = [node1]
  
  while not_checked:
    current = not_checked.pop(0)
    if current == node2:
      return True
    
    else:
      checked.add(current)
    
      for element in current.adjacent:
        if element not in checked:
          not_checked.append(element)

  return

""" 
Challenge 4:

An edge is a connection between two nodes. For example, this graph 

      A
    /   \
   B --- C
   
has the following edges:

Edges
<Node A>, <Node B>
<Node A>, <Node C>,
<Node B>, <Node A>,
<Node B>, <Node C>,
<Node C>, <Node B>,
<Node C>, <Node A>

[(Node A, Node B), (Node B, Node C), (Node C, Node A)]

Write a function that takes in a Node and returns a list of edges.
"""
def connected(node1):

  checked = set()
  not_checked = [node1]
  edges = []
  
  while not_checked:
    current = not_checked.pop(0)
    checked.add(current)
    
    for element in current.adjacent:
      edges.append((current, element))
      
      if element not in checked:
        not_checked.append(element)

  return edges