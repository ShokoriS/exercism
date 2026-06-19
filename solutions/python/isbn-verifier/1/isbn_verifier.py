def is_valid(isbn):
    
    multi_by = 10 
    total = 0 

    for char in isbn.lower():
        if char == 'x' and multi_by == 1:
            total += 10 * multi_by
            multi_by -= 1
            print(char, multi_by)
        elif char.isdigit():
            total += int(char) * multi_by
            multi_by -= 1
        elif char.isalpha():
            return False
    return total % 11 == 0 and multi_by == 0 

