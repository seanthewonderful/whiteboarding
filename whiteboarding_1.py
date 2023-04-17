""" #1
Write a function that takes in a list of numbers and prints out each number that is less than 10.
"""

def print_less_than_10(nums):
    for num in nums:
        if num < 10:
            print(num)

""" #2 
Write a function that takes in a list of words. For each word, the function should print a tuple of (first_letter_of_word, word).
"""

def print_first_and_word(words):
    for word in words:
        print((word[0], word))

""" #3 
Write a function that takes in a list of numbers. It should print every other number, starting with the number at index 0.
"""

def print_every_other_number(nums):
    for i in range(len(nums)):
        if i % 2 == 0:
            print(nums[i])
            
    for i, num in enumerate(nums):
        if i % 2 == 0:
            print(num)
            
    for i in range(0, len(nums), 2):
        print(nums[i])
            
    for num in nums[::2]:
        print(num)
            

""" #4
Write a function that takes in a list and an item. It should return True if the list contains the item. Otherwise, return False.
"""

def find_item(lst, item):
    return item in set(lst)

    # for element in lst:
    #     if element == item:
    #         return True
        
    # return False

""" #5
Write a function that takes in a string and returns the length of that string. You cannot use the len function.
"""

def find_string_length(string):
    length = 0
    for letter in string:
        length += 1
        
    return length

""" #6 
Write a function that takes in a sentence as a string. The function should print the length of each word in the sentence.

Your sentence will not contain any punctuation.
"""

def print_word_lengths(sentence):
    sentence_list = sentence.split()
    for word in sentence_list:
        print(len(word))

""" #7
Write a function that takes in a list of numbers and returns the largest number in the list. You cannot use the max function.
"""

def largest_num(nums):
    if not nums:
        return

    max_n = nums[0]

    for num in nums:
        if num > max_n:
            max_n = num

    return max_n