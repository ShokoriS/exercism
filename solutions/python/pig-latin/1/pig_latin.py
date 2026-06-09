def find_split_index(word, characters):
    i = 0 
    while i < len(word) and word[i] not in characters:
        i += 1
    return i


def translate_word(word):
    vowels = {"a", "e", "i", "o", "u"}

    if word[0] in vowels or word.startswith(("xr", "yt")):
        return word + "ay"

    split_index = find_split_index(word, vowels)

    if word.startswith("qu") or word[split_index-1:].startswith("qu"):
        split_index += 1

    elif split_index == len(word):
        split_index = find_split_index(word, {"y"})

    return f"{word[split_index:]}{word[:split_index]}ay"

def translate(text):
    splited_text = text.split()
    return " ".join(translate_word(word) for word in splited_text)