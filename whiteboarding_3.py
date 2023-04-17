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
  new_nums = []
# start a loop through the nums list
  for num in nums:
    #check that num 
    if num < n:
      new_nums.append(num)

  return max(new_nums)


def largest_smaller3(nums, n):
  largest = 0
  for num in nums:
    if (num < n and num > largest):
      largest = num

  return largest

""" #2
Write a function that takes in a list of numbers. It should return True if any two numbers in the list add to 0.
"""

def add_to_zero(nums):
    nums_set = set(nums)

    for n in nums:
        if -n in nums_set:
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

def reverse_digits(n):
    rev_digits = reversed(str(n))

    return int("".join(rev_digits))

    # n_string = str(n)
    # reverse_n_str = ""

    # for i in range(len(n_string)-1, -1, -1):
    #   reverse_n_str += n_string[i]

    # return int(reverse_n_str)

    # return int(str(n)[::-1])
    
def reverse_order(num):

    # reversed_str = str(num)[::-1]
    # reversed_str = int(reversed_str)

    # return reversed_str
  return int(str(num)[::-1])

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
            return True
        