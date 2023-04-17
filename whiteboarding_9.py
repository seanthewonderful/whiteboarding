""" 
Challenge 1:

This is a graph Node class:
"""

class Node:
  #A graph node.#

  def __init__(self, data, adjacent=None):
    self.data = data
    self.adjacent = adjacent or set()


"""Here is an example of how to create a graph to test your code"""

d = Node("D", {})
c = Node("C", {})
b = Node("B", {c, d})
a = Node("A", {c, b})
d.adjacent.add(b)
c.adjacent = {a, b}
        
"""
Create a Graph class. Graph instances should store all nodes in a graph. It should also have an instance method that adds a Node to the graph and a method that connects two existing Node instances together.

Hint 1: 
You can store all the nodes of a graph in an instance attribute. What would be a good data structure to use in this situation?
Hint 2:
The method that adds a Node to the graph should take in a Node instance.
The method that connects nodes should take in two Node instances. Also, be sure that both nodes have been added to the graph.
"""
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
  
  while to_see:
    
    current = to_see.pop(0)
    
    print(current)
    seen.add(current)
    
    for element in current.adjacent:
      
      if element not in seen:
        to_see.append(element)
      
  return 

def print_nodes_2(node):
    seen = set([node])
    to_visit = [node]

    while to_visit:
        current = to_visit.pop()
        print(current)

        for node in current.adjacent - seen:
            to_visit.append(node)
            seen.add(node)

""" 
Challenge 3:
Write a function that takes in two Node objects and returns True if the nodes are connected to one another.
Bonus: try implementing this recursively.
"""

def connected(node1, node2):
  
  if node1 in node2.adjacent:
    return True
  
  from collections import deque

  checked = set()
  not_checked = deque(node1)
  
  while not_checked:
    current = not_checked.popleft()
    if current == node2:
      return True
    
    else:
      checked.add(current)
    
      for element in current.adjacent:
        if element not in checked:
          not_checked.append(element)

  return

def has_connection(node1, node2):
    seen = set([node1])
    to_visit = [node1]

    while to_visit:
        current = to_visit.pop()
        if current is node2:
            return True
        else:
            for node in current.adjacent - seen:
                to_visit.append(node)
                seen.add(node)

    return False

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

Write a function that takes in a Node and returns a list of edges.
"""

def get_edges(node):
    seen = set()
    to_visit = [node]
    edges = []

    while to_visit:
        parent_node = to_visit.pop()

        if parent_node not in seen:
            seen.add(parent_node)

            for node in parent_node.adjacent:
                edges.append((parent_node, node))
                to_visit.append(node)
                
    return edges


""" 
Challenge 5:

A path is a list of nodes that represent a path from one node to another node.

      A - D
     / \ / \
    B   C   E
     \     /
      \   /
        F

In the graph above, a simple path from A to E is [<Node A>, <Node D>, <Node E>] because it doesn’t contain any repeating nodes.

Another path is [<Node A>, <Node B>, <Node C>, <Node A>, <Node D>, <Node E>]. However, it’s not a simple path because Node A appears twice.

Write a function that takes in two Node objects and returns a list of all possible simple paths between both nodes.
"""

def find_all_paths(start, end, path=None):
  
    path = path or []
    path = path + [start]

    if start is end:
        return [path]

    all_paths = []
    for node in start.adjacent:
        if node not in set(path):
            paths = find_all_paths(node, end, path)
            all_paths.extend(paths)

    return all_paths