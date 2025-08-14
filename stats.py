def count_words(file_content):
    words = file_content.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters
        