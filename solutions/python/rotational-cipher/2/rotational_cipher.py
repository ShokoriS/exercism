def rotate(text, key):
     
    cipher = lambda char, alpha: (chr(((ord(char) - ord(alpha) + key ) % 26) + ord(alpha)))


    return "".join(cipher(char, "a") if char.isalpha() and char.islower() 
                    else cipher(char, "A") if char.isalpha() and char.isupper()
                   else char 
                    for char in text) 
    

