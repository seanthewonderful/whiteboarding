""" #1
Python programmers write variable names in snake case, where each word is lowercase and joined by underscores. For example, if you were to write “very hungry caterpillar” in snake case, you’d write very_hungry_caterpillar.

JavaScript programmers write variable names in camel case, where the initial word is lowercase and other words are capitalized. For example, if you were to write “very hungry caterpillar” in camel case you’d write veryHungryCaterpillar.

Write a function that converts a string in snake case to a string in camel case.
"""

def snake_cc(phrase):
    
    new_str = ""
    x = 0
    
    for i, char in enumerate(phrase):
        if i == 0:
            new_str += char
        else:
            if x == 1:
                new_str += char.upper()
                x = 0
            else:
                if char == "_":
                    x = 1
                else:
                    new_str += char
                    
    return new_str         

def snake_to_camel(string):
    
    camelStr = ""
    split_str = string.split("_")
    
    for i, word in enumerate(split_str):
        if i == 0:
            camelStr += word
        else:
            camelStr += word.title()
    
    return camelStr
            
def june_to_camel(phrase):
    
    snake_list = phrase.split('_')
    camel = snake_list[0]
    
    for i in range(1, (len(snake_list))):
        camel += snake_list[i].title()
        
    return camel
    

""" #2
Write a function that takes in a phrase and returns a dictionary that can be used to lookup words by word lengths.

For example, the phrase "cute cats chase funny rats" should return a dictionary like so:

{
    4: {"cute", "cats", "rats"},
    5: {"chase", "funny"}
}
Notice that the keys of the dictionary above are integers and its values are sets that contain strings.
"""

def letter_count_dict(phrase):
    
    letter_counts = {}
    
    for word in phrase.split(" "):
        
        if len(word) not in letter_counts:
            
            letter_counts[len(word)] = set()
        
        letter_counts[len(word)].add(word)
        
    return letter_counts


def erin_letter_dict(phrase):
    
    split_phrase = phrase.split()
    words_by_length = {}
    
    for word in split_phrase:
        words_by_length[len(word)] = (words_by_length.get(len(word), set())).add(word)
    
    return words_by_length


def make_word_length_dict(dict_str):
    words_by_length = {}

    word_list = dict_str.split()

    for word in word_list:
        word_length = len(word)

        if words_by_length.get(word_length):
            words_by_length[word_length].add(word)
        else:
            words_by_length[word_length] = {word, }

    return words_by_length


""" #5
Write a function that takes in a list and reverses it in-place (without creating a new list).

Hint:
To swap two values, you can use this syntax:
a, b = b, a
"""

def reverse_list(lst):
    
    for i in range(len(lst) // 2):
        lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]

    return lst


def rev_list_in_place(lst):
    for idx in range(len(lst) // 2):
        # We want to swap lst[0] with lst[-1], lst[1] with
        # lst[-2], etc.
        idx1, idx2 = idx, -(idx + 1)

        # Make the swap
        lst[idx1], lst[idx2] = lst[idx2], lst[idx1]


""" #4
Write a function that takes in two strings and returns True if the strings are anagrams of one another. For example,

"moon", "noom" => True
"bat", "snack" => False
"secure", "rescue" => True

"", "" => True
"""

def is_anagram(s1, s2):
    counts1 = {}
    counts2 = {}

    for char in s1:
        counts1[char] = counts1.get(char, 0) + 1

    for char in s2:
        counts2[char] = counts2.get(char, 0) + 1

    return counts1 == counts2
# Alternate solution that requires less effort:

def is_anagram_alt(s1, s2):
    return sorted(s1) == sorted(s2)

def alexgram(s1, s2):
    
    for char in s2:
        if char not in s1:
            return False
        
    return True


""" #5
Write a function that prints an encrypted message.

Using this method, the message HOT SAUCE would look like this:

HTAC
OSUE
It’s a pretty simplistic method of encryption. All you do is split the letters of the initial message and alternate them over two rows of text, skipping any spaces. For example, the first letter goes in the first row, the second letter goes in the second row, the third letter goes in the first row, and so on…

Write a function that takes in a phrase and prints an encrypted version of that phrase using the method described above.

The phrase is guaranteed to only contain uppercase, alphabetic characters and spaces.
"""

def print_coded_msg(msg):
    row1 = []
    row2 = []

    # Filter out non-alphabetic characters
    only_chars = []
    for char in msg:
        if char.isalpha():
            only_chars.append(char)

    # Even indexed characters go in row1, odd ones
    # in row 2.
    for idx, char in enumerate(only_chars):
        if idx % 2 == 0:
            row1.append(char)
        else:
            row2.append(char)

    print("".join(row1))
    print("".join(row2))