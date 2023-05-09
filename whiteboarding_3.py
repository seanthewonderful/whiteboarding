""" #1
Write a function that takes in two arguments: a list of numbers and a number. It should return the largest number in the list that is smaller than the given number. For example:

[1, 300, 3, 5, 70], 100 => 70
"""

def largest_smaller(nums, n):
  result = None

  for num in nums:
    if num < n:
      if not result or result < num:
        result = num

  return result

def largest_smaller2(nums, n):
  largest = 0
  for num in nums:
    if (num < n and num > largest):
      largest = num

  return largest

def largest_smaller3(nums, n):
  new_nums = []
# start a loop through the nums list
  for num in nums:
    #check that num 
    if num < n:
      new_nums.append(num)

  return max(new_nums)

""" #2
Write a function that takes in a list of numbers. It should return True if any two numbers in the list add to 0.
"""

def add_to_zero(nums):
    nums_set = set(nums)

    for n in nums:
        if -n in nums_set:
            return True

    return False
  
def pair_adding_to_zero(numbers):
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers[i+1:], i+1):
            if num1 + num2 == 0:
                return True
    return False


""" #3
A string is a pangram if it contains every letter in the alphabet at least once. For example, this sentence is a pangram:

The quick brown fox jumps over the lazy dog.

Write a function that takes in a string and returns True if the string is a pangram.
"""

def is_pangram(s):
    letters = set()

    lowercased = s.lower()
    for c in lowercased:
        if c.isalpha():
            letters.add(c)

    return len(letters) == 26

def is_pangram2(s):
  alphabet = "abcdefghijklmnopqrstuvwxyz"

  s_lower = s.lower()

  for letter in alphabet:
    if letter not in s_lower:
      return False
    
    # if letter in s_lower:
    #   continue
    # else:
    #   return False

  return True


""" #4
Write a function that takes in a number. Return a number with the digits of the given number, but in reverse order. For example:

123 => 321

Hint:
One way to do this is to (ab)use the fact that you can typecast an integer into a string.
"""

def reverse_digits(num):
  
    rev_digits = reversed(str(num))

    return int("".join(rev_digits))

def reverse_digits2(num):
  
    num_string = str(num)
    reverse_num_str = ""

    for i in range(len(num_string)-1, -1, -1):
      reverse_num_str += num_string[i]

    return int(reverse_num_str)
    
def reverse_digits3(num):

    reversed_str = str(num)[::-1]
    reversed_str = int(reversed_str)

    return reversed_str
    # return int(str(num)[::-1])

def reverse_digits4(num):
  
  rev_list = []
  new_num = list(str(num))
  
  while new_num:
    rev_list.append(new_num.pop())
    
  return int("".join(rev_list))

def reverse_digits5(num):
  
  letters = list(str(num))
  
  r = reversed(letters)
  
  return int("".join(r))
  
  
""" #5
Write a function that takes in a string. It should return a string where consecutive repeating characters have been truncated. For example:

"aaaabbbbbbcccc" => "abc"
"caaaat" => "cat"
"""

def truncate_repeats(string):
    new_str = ""
    
    for i, c in enumerate(string):
        if i == 0 or c != string[i - 1]:
            new_str += c
    
    return new_str

def v_truncate(string):
    new_str = ""
    
    for i in range(1, len(str)):
        if (string[i] == 100):
            pass
        
def truncate_string(string):
    chars_to_keep = [string[0]]

    i = 0
    for i in range(len(string) - 1):
      if string[i] == string[i+1]:
         i += 1
      elif string[i] != string[i+1]:
         chars_to_keep.append(string[i+1])
         i += 1

    truncated_string = "".join(chars_to_keep)
   
    return truncated_string
  
# def truncate(string):
#   if not string:
#     return string
#   result = string[0]
#   for i in range(1, len(string)):
#     if s[i] != s[I-1]:
#       result += s[i]
#   return result