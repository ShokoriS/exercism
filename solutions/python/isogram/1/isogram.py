def is_isogram(word):
    seen = set()
    word = word.lower()
    for letter in word:
        if letter.isalpha():
            if letter in seen:
                return False
            seen.add(letter)
    return True 


