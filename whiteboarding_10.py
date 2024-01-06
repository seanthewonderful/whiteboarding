""" #1
This is a staircase of size n = 4:
   #
  ##
 ###
####

Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a function that takes in a parameter n and prints a staircase of size n.
"""
    # 1st n-1 " " plus 1 "#"
    # 2nd: n-2 " " plus 2 "#"
    # 3rd: n-3 " " plus 3 "#"
    # 4th: n-4 " " plus 4 "#"
    # while-loop and reassign n for each loop?   

def print_staircase(n):
    
    count = 1
    
    while n > 0:
        
        print((" " * (n - 1)) + ("#" * count))

        n -= 1
        count += 1


def staircase(n):
    
    i = 1
    
    while i <= n:
        
        space = " " * (n - i)
        if space is not None:
            print(space + ("#" * i))
        
        i += 1
        
        
def staircase_hb(n):
    
    for i in range(1, n + 1):
        row = []

        for j in range(n - i):
            row.append(" ")

        for j in range(i):
            row.append("#")

        print("".join(row))
        
def build_staircase(n):
    
    for i in range(1, n+1):
        
        print(" "*(n-i) + "#"*i)

# staircase(7)
# staircase_hb(7)

""" # 2

Given a 2-dimensional array of numbers (i.e. a list of lists), write a function that returns the sum of all numbers that are low points. A low point is any number that is smaller than its neighbors above, below, and to the left and right. Example:

[9, 8, 6, 5, 4]
[7, 4, 7, 7, 2]
[6, 5, 0, 5, 6]
[3, 1, 8, 5, 8]

[[9, 8, 6, 5, 4], [7, 4, 7, 7, 2], [6, 5, 0, 5, 6], [3, 1, 8, 5, 8]]

The red numbers are low points, so the function should return 4 + 2 + 0 + 1 = 7.


Hint 1:
To iterate through a 2-dimensional array, you can use the following syntax:
num_rows = len(grid)
num_cols = len(grid[0])
for row in range(num_rows):
    for col in range(num_cols):
        current = grid[row][col]

Hint 2:
The trick to this problem is making sure indices do not go out of bounds.
"""
def sum_low_points(grid):
    low_points = []
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row in range(num_rows):
        for col in range(num_cols):
            current = grid[row][col]

            if row > 0 and current >= grid[row - 1][col]:
                continue
            elif col > 0 and current >= grid[row][col - 1]:
                continue
            elif row < num_rows - 1 and current >= grid[row + 1][col]:
                continue
            elif col < num_cols - 1 and current >= grid[row][col + 1]:
                continue
            else:
                low_points.append(current)

    return sum(low_points)


def low_point_sum(grid):
    
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    low_points = 0
    
    for row in range(num_rows):
        for col in range(num_cols):
            
            current = grid[row][col]
            
            if row == 0:
                # in top row, cannot be a top value
                if col == 0:
                    # if col == 0, cannot be a left value (plus no top value) --> this is the first number (top left)
                    if current < grid[row + 1][col] and current < grid[row][col + 1]:
                        low_points += current
                
                elif col == num_cols - 1:
                    # if col == num_cols - 1, cannot be a right value (plus no top value) --> this is the last number in the top row (top right)
                    if current < grid[row + 1][col] and current < grid[row][col - 1]:
                        low_points += current
                
                else:
                    # in top row, not on right or left side --> only don't check "top" number
                    if current < grid[row + 1][col] and current < grid[row][col - 1] and current < grid[row][col + 1]:
                        low_points += current
                        
            elif row == num_rows - 1:
                # working in bottom row --> don't check bottom number
                if col == 0:
                    # bottom left number --> don't check left or bottom
                    if current < grid[row - 1][col] and current < grid[row][col + 1]:
                        low_points += current
                        
                elif col == num_cols -1:
                    # bottom right number --> don't check right or bottom
                    if current < grid[row - 1][col] and current < grid[row][col - 1]:
                        low_points += current
                
                else: 
                    # bottom row, not right or left --> don't check bottom
                    if current < grid[row - 1][col] and current < grid[row][col - 1] and current < grid[row][col + 1]:
                        low_points += current
                        
            else:
                # not in top or middle row
                if col == 0:
                    # on left side, don't check left value
                    if current < grid[row - 1][col] and current < grid[row + 1][col] and current < grid[row][col + 1]:
                        low_points += current
                        
                elif col == num_cols - 1:
                    # on right side, don't check right value
                    if current < grid[row - 1][col] and current < grid[row + 1][col] and current < grid[row][col - 1]:
                        low_points += current
                
                else:
                    # not on an edge - can check against all
                    if current < grid[row - 1][col] and current < grid[row + 1][col] and current < grid[row][col - 1] and current < grid[row][col + 1]:
                        low_points += current
                        
    return low_points

            
            # normal condition: 
                # top = grid[row-1][col]
                # bottom = grid[row+1][col]
                # left = grid[row][col-1]
                # right = grid[row][col+1]

""" #3
Given a Node class for a binary search tree below:

Write a method that takes in a new node, and inserts the node in its proper position in the binary search tree rooted at self. You can assume there are no duplicate values in the tree.
"""

class BinarySearchNode:
    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right

    def insert_node(self, new_node):
        
        current = self
        
        while current: 
            if new_node.data >= current.data:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left


    def insert_recursive(self, new_node):
        """Insert new node with `new_data` to BST tree rooted here."""

        if new_node.data >= self.data:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert_recursive(new_node)
        else:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert_recursive(new_node)
                

""" #4
Given the following Node class:
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
"""    
Write a function that takes in the head of a singly-linked list. It should return the head of a linked list with the nodes in reversed order.

Hint 1: 
You may want to consider using an additional data structure.
Hint 2:
You can store all the nodes in a stack. Then, you can re-create the list by popping nodes from the stack. Due to the nature of stacks, nodes will automatically be popped in reverse order.
Hint 3:
There’s also a way to do this without using any extra data structures.
"""

def reverse_ll(head):
    
    # Can iterate and make a stack, then pop from stack creating a new ll
    stack = []
    current = head
    
    while current:
        stack.append(current)
        current = current.next
    
    new_head = stack.pop()
    current = new_head
    
    while stack:
        current.next = stack.pop()
        current = current.next
        
    current.next = None
    
    return new_head
        
        
def reverse_llist_without_stack(head):
    new_head = None
    curr = head

    while curr:
        new_head = Node(curr.data, new_head)
        curr = curr.next

    return new_head


""" #5
Given a Node class for a binary search tree:
"""
class BinarySearchNode:
    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right
"""
Write a function that takes in the root of a binary search tree, and returns the max depth of the tree (the number of nodes in the longest path from the root to any leaf).

Hint 1:
Use recursion. If the max depth of the left subtree is 3, and the max depth of the right subtree is 2, what is the max depth of the tree? Why?
"""

def max_depth(root):
    
    # Base case
    if root is None:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    
    if left_depth > right_depth:
        return 1 + left_depth
    else:
        return 1 + right_depth


# HB - same thing basically
def max_tree_depth(root):
    if root is None:
        return 0
    
    left_height = max_tree_depth(root.left)
    right_height = max_tree_depth(root.right)
    
    return max(left_height, right_height) + 1


""" #6
Rate limiting refers to preventing the frequency of an operation from exceeding a defined limit. For example, a rate limiter for an API might limit the number of API requests that can happen in a certain period of time (e.g. 5 seconds).

Write a function that takes in two parameters: a list of numbers that represent timestamps (in seconds) of API requests, and the maximum number of requests allowed in any 5 second window. The function should return a list which is the same length as the input list, where each item is True or False depending on whether each request was allowed or rejected.

Example: .. code-block:: python

>>> allowed_requests(request_timestamps=[1, 2, 2, 2, 6, 12, 32, 33, 34, 37], max_requests=3)
[True, True, True, False, False, True, True, True, True, True]
The first three requests (t=1, t=2, t=2) are allowed, but the 4th request (t=2) is rejected because there were already three requests in the last two seconds. The 5th request (t=6) is also rejected, because there were three requests that happened 4 seconds ago at t=2, so no more requests are allowed until t=7. The rest of the requests are allowed.

Hint 1:
At each iteration, compile a list of all requests that happened less than 5 seconds ago. For example, if the timestamp of the current request is t=8, make a list of all requests with timestamps between 4 and 8 inclusive.
"""

# Need to keep track of timestamps up till 5, if more than x requests in sequence with sum <= 5, next is rejected until 5 more seconds have passed ?

def rate_limiter(timestamps, max_requests):
    pass
    


def allowed_requests(request_timestamps, max_requests):
    
    requests_in_window = [2, 2]
    results = [T, ]

    for timestamp in request_timestamps:

        # Make a list of all requests that happened less than 5 sec ago
        # For efficiency, you don't have to start at the beginning, you can
        # just look at the requests that were previously in the list and
        # filter those that are still less than 5 sec ago.
        updated_requests_in_window = []
        for request_time in requests_in_window:
            if request_time > timestamp - 5:
                updated_requests_in_window.append(request_time)
            requests_in_window = updated_requests_in_window

        # Append the current request to the list
        requests_in_window.append(timestamp)

        if len(requests_in_window) <= max_requests:
            results.append(True)
        else:
            results.append(False)

    return results


""" #7
Given a 2D grid which represents a map of “1”s (land) and “0”s (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Examples:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Hint 1: This is a graph problem, though it may not look like one. Each set of coordinates (row, col) in the grid is a node, and the adjacent nodes are the neighbors above, below, and to the left and right. See the hint for the Low Points problem for how to iterate through a 2D grid.

Hint 2: 
Use DFS or BFS to traverse each island, and keep a count of the number of islands.
"""

def get_neighbors(row, col):
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    
def num_islands(grid):
    visited_islands = set()
    island_count = 0
    for start_row in range(len(grid)):
        for start_col in range(len(grid[0])):
            if (
                grid[start_row][start_col] == "1"
                and (start_row, start_col) not in visited_islands
            ):
                island_count += 1
                to_visit = [(start_row, start_col)]

                while to_visit:
                    current_row, current_col = to_visit.pop()
                
                    for row, col in get_neighbors(current_row, current_col):
                        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                            continue  # out of bounds!
                        if grid[row][col] == "1" and (row, col) not in visited_islands:
                            to_visit.append((row, col))
                            visited_islands.add((row, col))

    return island_count


# Recursive solution

def num_islands_recursive(grid):  # grid is a list of lists
    visited_islands = set()

    # By making this an inner function, we can also access the variables
    # grid and visited_islands.
    # We can make it a separate function, but then we'd have to pass in
    # grid and visited_islands as additional parameters.
    def visit_whole_island(row, col):
       
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return  # out of bounds!
        if (row, col) in visited_islands:
            return

        if grid[row][col] == "1":
            visited_islands.add((row, col))
            # Top
            visit_whole_island(row - 1, col)
            # Bottom
            visit_whole_island(row + 1, col)
            # Left
            visit_whole_island(row, col - 1)
            # Right
            visit_whole_island(row, col + 1)

    island_count = 0
    for start_row in range(len(grid)):
        for start_col in range(len(grid[0])):
            if (
                grid[start_row][start_col] == "1"
                and (start_row, start_col) not in visited_islands
            ):
                island_count += 1
                visit_whole_island(start_row, start_col)
    return island_count