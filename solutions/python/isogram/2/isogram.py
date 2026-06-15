"""This file will detect what the an isogram is"""


def is_isogram(word):
    """This function determines if a word is isogram or not"""
    
    seen = set()
    word = word.lower()
    for letter in word:
        if letter.isalpha():
            if letter in seen:
                return False
            seen.add(letter)
    return True 