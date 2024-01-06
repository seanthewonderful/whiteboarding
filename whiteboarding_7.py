""" 
Challenge 1:
Write a function that returns the length of a list using recursion

Hint: 
What’s your base case? How do you make progress towards the base case?
"""

def recurse_length(lst):
    
    #base case
    if len(lst) == 1:
        return 1
    else:
        lst.pop()
        return recurse_length(lst) + 1
    
    # Hackbright Solution:
    
    # if not lst:
    #     return 0

    # return 1 + recurse_length(lst[1:])

def recur(lst):
    
    if not lst:
        return 0
    else:
        lst.pop()
        
    return 1 + recur(lst)
    
    
l1 = [1,2,3,4,5,6]
# print(f"Recursion to print list length: {recurse_length(l1)}")
print(recur(l1))

""" 
Challenge 2:
Write a recursive function that prints the numbers 1 through 5

Hint: 
What’s a good base case for this function?
"""

def recurse_printnums(max_num, i=0):

    # Base case
    if i == max_num:
        return i
    
    i += 1
    print(i)
    recurse_printnums(max_num, i)
    
# Hackbright Solution:
def print_nums(n=1):
    
    if n > 5:
        return
    
    print(n)
    print_nums(n + 1)
    
# def vin(lst):
#     if not lst:
#         return
#     for item in lst:
#         print(item)
#         recurse_length(lst[1:])

# print("Recursion to print 1 - 5:")
# recurse_printnums(5)
# print_nums()


""" 
Challenge 3: 
Write a recursive function that takes a list of numbers and returns the largest number in the list.

Hint 1: 
You’ll need some way to keep a hold of the greatest number. How do you carry data from one function call to the next?
Hint 2: 
One way to persist data across function calls is to add an additional parameter to your function signature. That way, we can pass the current highest number into the next recursive call.
Hint 3:
def max_num(nums, max_n=None):
    pass
"""

def largest_num(lst, l=0):
    # General idea: update l to the current greatest number and once entire list has been traversed, l must be the greatest number of all and return it
    # Recursion process:
    # 1. Break problem down into a problem 1 step simpler -- idk how to do that in this scenario
    # 2. Assume that my function will work to solve the simpler problem. What is the simpler problem compared to the complex? 
    #. Since I know that can be solved, how can I solve the more complex one?
    
    # Base case = list is empty so return l
    if not lst:
        return l
    
    # else:
    i = lst.pop()
    if i > l:
        l = i

    return largest_num(lst, l)

# Hackbright Solution:
def max_num(nums, largest=None):
    if not nums:
        return largest

    if largest is None or nums[0] > largest:
        largest = nums[0]

    return max_num(nums[1:], largest)

l2 = [5,4,7,1,9,4,7,2]
# print("Return largest number:")
# print(largest_num(l2))


""" 
Challenge 4:
Write a recursive function that takes a list of numbers and returns a list where all numbers are doubled.

Hint 1: 
You can solve this by modifying the list in-place or by creating a new list (out-of-place).
"""

def double_list_nums(lst, lst2=[]):
    # Base idea: for idx, num in enumerate(lst): lst[idx] = num * 2
    
    # Base Case:
    if not lst:
        return lst2
    # Using a new list (out-of-place)
    lst2.append(lst[0] * 2)
    
    return double_list_nums(lst[1:], lst2=lst2)

def double_list_inplace(lst, idx=0):
    
    if idx == len(lst):
        return lst
    
    lst[idx] *= 2
    
    return double_list_inplace(lst, idx=idx+1)

# Hackbright Solution:
def double_nums(nums):
    if not nums:
        return []

    first_num_doubled = nums[0] * 2

    return [first_num_doubled] + double_nums(nums[1:])

# print(double_list_nums(l1))
# print(double_list_inplace(l1))


""" 
Challenge 5:
Write a recursive funtion that takes in a string and reverses it. Return the reversed string.

Hint 1:
Can you use the call stack to your advantage?
Hint 2:
Hint 3:
"""

def reverse_string(string, string2=""):
    # Recursive thought process:
    # 1-step simpler: return all letters reversed + string[0]
    # Believe the function will handle the first part
    # How to solve the last part? return reverse_string(string) + string[0]
    
    # Base Case
    if not string:
        return string2
    
    string2 += string[-1]
    
    return reverse_string(string[:-1], string2=string2)

# Hackbright Solution:
def reverse_str(s):
    if not s:
        return s

    return reverse_str(s[1:]) + s[0]

# print(reverse_string("sean is cool"))


""" 
Challenge 6:
Write a recursive function that takes in a list and flattens it. For example:

in: [1, 2, 3]
out: [1, 2, 3]

in: [1, [1, 2], 2, [3]]
out: [1, 1, 2, 2, 3]

Hint 1:
You’ll need to use a for-loop somewhere. (Not really though)
"""

def flatten_list(lst, lst2=[]):
    # Base idea: at each element, if the element is a list unpack it and append it. Need a new list for this?
    # Recursion thought process:
    # 1-step smaller: return the list - list[-1]
    # Believe the rest will work
    # How to solve the more complex one: return list + flattened(list[-1])
    
    if not lst:
        return lst2
        
    if type(lst[0]) == list:
        flatten_list(lst[0], lst2=lst2)
    else:
        lst2.append(lst[0])
    
    return flatten_list(lst[1:], lst2=lst2)

# Hackbright Solution:
def flatten(lst, result=None):
    result = result or []

    for el in lst:
        if type(el) is list:
            flatten(el, result)
        else:
            result.append(el)

    return result

def flatten_no_loop(lst):
    if not lst:
        return []

    if isinstance(lst[0], list):
        return flatten_no_loop(lst[0]) + flatten_no_loop(lst[1:])

    return [lst[0]] + flatten_no_loop(lst[1:])

fl = [1, 2, [3, 4, 5], 6, [7, 8, [8, 7]], 9]
# print(flatten_list(fl))

