def is_paired(input_string):
    opposites = {")": "(", "}": "{", "]":"["}
    seen = []
    for symbol in input_string:
        if symbol in opposites.values():
            seen.append(symbol)

        elif symbol in opposites.keys():
        
            if not seen or (seen.pop() != opposites.get(symbol, None)):
                return False

    return True if not seen else False

