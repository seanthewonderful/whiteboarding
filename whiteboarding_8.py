""" #1
Write a function that takes in a list and returns the sum of all numbers in the list using recursion.
"""

def sum_nums_recursive(lst):
    if not lst:
        return 0

    return lst[0] + sum_nums_recursive(lst[1:])
###
def recursive_sum(nums, count=0):
    # 1 step simpler, believe rest, solve complex
    
    if not nums:
        return count
    
    count += nums[0]
    return recursive_sum(nums[1:], count=count)

nums_1 = [1,2,3,4,5,6,7]
# print(recursive_sum(nums_1))

""" #2
Write a function that computes the factorial of a number using recursion. The factorial of a number n is defined as the product of all numbers from 1 to n. For example, 4! = 4 x 3 x 2 x 1 = 24.
"""

def factorial_recursive(n):
    if n == 0:
        return

    return n * factorial_recursive(n - 1)
###
def recurse_factorial(num, count=1):
    
    if num == 1:
        return count
    
    count = count * num
    num -= 1
    return recurse_factorial(num=num, count=count)

# print(recurse_factorial(8))

""" #3
Imagine a list of numbers from 1 to max_num, inclusive – except that one of these numbers will be missing from the list. Write a function that takes this list of numbers, as well as the max_num, and returns the missing number. If no numbers are missing, return 0.

For example, given a list of numbers, in random order, of 1..10, 8 was removed. Your function would be given the list and the max_num (10), and it should find 8:

>>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
8
>>> missing_number([4,3,2,1], 4)
0
>>> missing_number([5,4,7,3,6,2], 7)
1
The function should run in O(n) time.

Hint:
Create a new list/set/dictionary.
Note: why does it not work to sort the list? What is the runtime of sorting a list?
"""

def find_missing_num(nums, max_num):
    # Create a set and use range to check if numbers
    # in the range are in the set.

    num_set = set(nums)
    for i in range(1, max_num + 1):
        # still O(n) because "in set" is O(1). O(n) * O(1) = O(n)
        if i not in num_set:
            return i
    return 0

def find_missing_num_sum(nums, max_num):
    
    lst_sum = sum(nums)
    max_sum = int((max_num ** 2 + max_num) / 2)

    return max_sum - lst_sum

# use new data types
# consider runtimes



# Not sure if this works yet
# def find_missing_num_dict(nums, max_num):
#     num_dict = {}
    
#     for num in nums:
#         num_dict[num] = True
        
#     for i in range(max_num + 1):
#         if i not in num_dict:
#             return i
        
#     return 0
    
nums_2 = [1,2,3,5,6,7,8,4,9]
# print(find_missing_num(nums_2, 9))

""" #4
Write a function that takes in a string and returns True or False depending on whether the string’s opening and closing brackets are balanced. Account for the following bracket types:

Parentheses ()

Square Brackets []

Curly Braces {}

If an open bracket appears, the pair should also be closed correctly. Examples:

"([ok])" => True
"{[[This has too many open square brackets]}" => False
")(Closing bracket before opening bracket" => False
"[{Wrong order]}" => False
"No brackets!" => True

Hint1:
One particular data structure will be very helpful here.
Hint2:
"""

def has_balanced_brackets(phrase):
    closers_to_openers = {")": "(", "]": "[", "}": "{"}

    # Set of all opener characters; used to match openers quickly.
    openers = set(closers_to_openers.values())

    # Create an empty list to use as a stack.
    openers_seen = []

    for char in phrase:

        # Push open brackets onto the stack.
        if char in openers:
            openers_seen.append(char)

        # For closers:
        # - if nothing is open; fail fast
        # - if we are the twin of the most recent opener, pop & continue
        # - else we're the twin to a different opener; fail fast
        elif char in closers_to_openers:

            if openers_seen == []:
                return False

            if openers_seen[-1] == closers_to_openers.get(char):
                openers_seen.pop()

            else:
                return False

    # An empty stack means the brackets are balanced.
    return openers_seen == []

def balanced_brackets(phrase):
    
    stack = []
    
    for i in phrase:
        
        if i in '({[':
            stack.append(')}]'['({['.index(i)])
            
        elif stack and stack[-1] == i:
            stack.pop()

    return len(stack) == 0

# print(balanced_brackets("[{wrong{]"))

def balanced_brackets3(phrase):
    '''
    Variation of the first function
    '''
    stack = []
    
    opening = set('([{')
    closing = set(')]}')
    pair = {')' : '(' , ']' : '[' , '}' : '{'}
    
    for char in phrase:
        
        if char in opening :
            stack.append(char)
            
        if char in closing :
            
            if not stack :
                return False
            elif stack.pop() != pair[char] :
                return False
            else :
                continue
            
    return stack == []

""" #5
Write a function that takes in two sorted lists. Merge them into one sorted list. For example:

[1, 3], [2, 8, 10]
=> [1, 2, 3, 8, 10]
The function should run in O(n) time.

Hint1:
Why does it not work to sort the list? What is the runtime of sorting a list?
Hint2:
You can use the fact that the lists are already sorted. Compare the first number in each list and add the lower one to the new list. Then, increment the index in whichever list that number came from.
"""

def merge_sorted_lists(nums_1, nums_2):
    
    merged_list = []
    i = j = 0
    
    while i < len(nums_1) and j < len(nums_2):
        
        if nums_1[i] <= nums_2[j]:
            merged_list.append(nums_1[i])
            i += 1
        else:
            merged_list.append(nums_2[j])
            j += 1
    
    merged_list += nums_1[i:] + nums_2[j:]
    
    return merged_list

l1 = [1,3]
l2 = [2,4,7]
l3 = [1,3,5]
l4 = [2,3,7]
# print(merge_sorted_lists(l3, l4))

def merge_sorted_joshuah(nums_1, nums_2):
    
    merged_list = []
    
    for i in range(len(nums_1)):
        for j in range(len(nums_2)):
            if nums_1[i] > nums_2[j]:
                merged_list.append(nums_2[j])

""" #6
You are given an array of prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

There is a fairly straightforward O(n^2) solution, but the best solution has a runtime of O(n).

Example 1:

Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]

Output: 0

Explanation: In this case, no transactions are done because the price always goes down, and the max profit = 0.

Hint1:
For the O(n) solution – as you loop through the list, keep track of two values: the lowest (best) buy price so far, and the max profit so far.
"""

def find_max_profit(prices):
    if not prices:
        return 0
    best_buy_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < best_buy_price:
            # found a new best buy price
            best_buy_price = price
        else:
            current_profit = price - best_buy_price
            max_profit = max(current_profit, max_profit)

    return max_profit

# Less efficient O(n^2) solution
def find_max_profit_n_squared(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            current_profit = prices[j] - prices[i]
            max_profit = max(current_profit, max_profit)
    return max_profit


""" #7
Given the following class definitions:

class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None
      self.tail = None
Write a method for the LinkedList class called remove. It should take in a value and remove the first node with that value from the linked list.

Hint1:
If you don’t want to worry about potentially updating the head and tail, there is an alternate solution that involves creating a new linked list.
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None 
        
class LinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def remove(self, value):
        # If list is empty, return
        if not self.head:
            return
        
        # If head is node to remove, reassign head to self.head.next
        if self.head.data == value:
            self.head = self.head.next
            # If new head is None, then LL only had 1 node. Update tail to None since list is empty
            if self.head == None:
                self.tail = None
            return
            
        current = self.head
        
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                # If node was the tail, current.next will be None. Update tail to current. 
                if not current.next:
                    self.tail = current
                return
            
    
    def remove_1(self, value):
        if not self.head:
            return

        new_list = LinkedList()
        curr = self.head
        while curr:
            if curr.data != value:
                # create new node and append to new_list
                new_node = Node(curr.data)
                if new_list.tail is None:
                    new_list.tail = new_list.head = new_node
                else:
                    new_list.tail.next = new_node
                    new_list.tail = new_node

            curr = curr.next

        self.head = new_list.head
        self.tail = new_list.tail