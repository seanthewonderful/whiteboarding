"""
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

l1 = [1,2,3,4,5,6,7]
# print(recursive_sum(l1))

""" 
Write a function that computes the factorial of a number using recursion. The factorial of a number n is defined as the product of all numbers from 1 to n. For example, 4! = 4 x 3 x 2 x 1 = 24.
"""

def factorial_recursive(n):
    if n == 1:
        return 1

    return n * factorial_recursive(n - 1)
###
def recurse_factorial(num, count=1):
    
    if num == 1:
        return count
    
    count = count * num
    num -= 1
    return recurse_factorial(num=num, count=count)

# print(recurse_factorial(8))

""" 
Imagine a list of numbers from 1 to max_num, inclusive – except that one of these numbers will be missing from the list. Write a function that takes this list of numbers, as well as the max_num, and returns the missing number. If no numbers are missing, return 0.

For example, given a list of numbers, in random order, of 1..10, 8 was removed. Your function would be given the list and the max_num (10), and it should find 8:

>>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
8
The function should run in O(n) time.

Hint:
Create a new list/set/dictionary.
Note: why does it not work to sort the list? What is the runtime of sorting a list?
"""

def find_missing_num(nums, max_num):
    # Create a set and use range to check if numbers
    # in the range are in the set.

    # num_set = set(nums)
    # for i in range(1, max_num + 1):
    #     if i not in num_set:
    #         return i
    # return 0

    lst_sum = sum(nums)
    max_sum = int((max_num**2 + max_num) / 2)

    return max_sum - lst_sum
    
l2 = [1,2,3,5,6,7,8,4,9]
print(find_missing_num(l2, 9))

""" 
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
    l = []
    for i in phrase:
        if i in '({[':
            l.append(')}]'['({['.index(i)])
        elif l and l[-1] == i:
            l.pop()

    return len(l) == 0

# print(balanced_brackets("[{wrong{]"))

""" 
Write a function that takes in two sorted lists. Merge them into one sorted list. For example:

[1, 3], [2, 8, 10]
=> [1, 2, 3, 8, 10]
The function should run in O(n) time.

Hint1:
Why does it not work to sort the list? What is the runtime of sorting a list?
Hint2:
You can use the fact that the lists are already sorted. Compare the first number in each list and add the lower one to the new list. Then, increment the index in whichever list that number came from.
"""

def merge_sorted_lists(l1, l2):
    
    merged_list = []
    i = j = 0
    
    while i < len(l1) and j < len(l2):
        
        if l1[i] <= l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1
    
    merged_list += l1[i:] + l2[j:]
    return merged_list

l3 = [1,3,5]
l4 = [2,3,7]
# print(merge_sorted_lists(l3, l4))

""" 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

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


""" 
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
    
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None 
        

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