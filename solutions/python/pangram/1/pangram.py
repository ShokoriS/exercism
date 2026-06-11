def is_pangram(text):
    text = text.lower() 
    seen = set()

    i = 0
    while i < len(text) and len(seen) < 26:
        char = text[i]
        if char.isalpha():
            seen.add(char)
        i += 1 

    
    return len(seen) == 26

