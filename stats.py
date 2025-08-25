def get_num_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def get_char_count(text):
    letters = ("abcdefghijklmnopqrstuvwxyz")
    counts = {letter: 0 for letter in letters}
    for char in text:
        for letter in letters:
            if char == letter or char.lower() == letter:
                counts[letter] += 1
    return counts

def sort_on(items):
    return items["num"]

