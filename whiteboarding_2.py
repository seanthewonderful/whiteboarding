""" Write a function that takes in a list of strings. Return the longest string in the list."""

def longest_string(strings):

    # Initial questions = Can list of strings be empty?
    # How shall I return a result if multiple strings have the same length in the list? 
    
    # Set empty string to represent current longest string
    longest = ""
    # Loop through strings, if longer than 'longest' then reset 'longest' to that string
    for string in strings:
        if len(string) > len(longest):
            longest = string
    # Once loop is complete, we have the longest string set to 'longest' and return it
    return longest
  
string_list = ["apple", "cat", "pear", "super duper", "pumpkin"]

"""Write a function that takes in an item and a list. Return the number of times the given item appears in the list."""

def item_times_in_list(item, list1):

  # Initial questions = Could the list be empty?

  # Create a counter to increment
  count = 0

  # Loop through list. If item == list element, increase counter
  for i in list1:
    if i == item:
      count += 1

  return count


"""Write a function that takes in a list of numbers. It should find all even numbers and return a list of their indices. For example

[2, 4, 1] => [0, 1]
[] => []
[1] => []"""

def find_even_num_indices(nums):
  # Set empty list to append indices
  indices = []
  # Loop through each number
  for num in nums:
    # If number % 2 == 0 then it is even
    if num % 2 == 0:
      indices.append(nums.index(num))

  return indices

l_nums = [2, 4, 1, 8, 10, 2, 7, 2000] # [0, 1, 3, 4, 5, 7]

"""Write a function that takes in a string and returns a string with all vowels replaced with *"""

def replace_vowels(string):
  # Set vowels so they are known
  vowels = "aeiou"
  # Set new empty string to append values or *
  new_string = ""
  # Loop through string and find vowel matches
  for i in string:
    if i in vowels:
      new_string += "*"
    else:
      new_string += i

  return new_string
  # Replace vowels with * by using their index? --> TypeError: 'str' object does not support item assignment


"""Write a function that takes in a string and returns all unique characters in the string"""

def unique_chars(string):
  # Initial questions = 
  # Should the return be a particular data type?
  # Find characters that only appear once? Or find one version of all characters in the string?

  return set(string)


"""Write a function that takes in a string and returns a character count dictionary. For example,

"catty" => {"c": 1, "a": 1, "t": 2, "y": 1}"""

def character_counts(string):
  # Set empty dictionary to house characters and their counts
  counts = {}

  # Iterate and insert keys to dictionary. If exist, increment value
  for char in string:
    counts[char] = counts.get(char, 0) + 1
  
  return counts



"""Write a function that takes in a string and returns True if it is a palindrome and False otherwise. A palindrome is a word that is spelled the same backwards and forwards.

You cannot use the reverse or reversed functions.

"noon" => True
"racecar" => True
"a" => True
"math" => False
"" => True
Treat spaces and uppercase letters normally:

"Racecar" => False"""

def is_palindrome(string):

  for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:
      return False

  return True


list_of_strings = ["sean", "natalie", "carlos", "tio", "bazooka joe"]