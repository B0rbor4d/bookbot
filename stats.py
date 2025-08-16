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

def sort_on(items):
    return items["Anzahl"]

def sort_list(letter_dict):
    letter_list = []
    for letter in letter_dict:
        count = letter_dict[letter]
        if letter.isalpha():
            letter_list.append({"Buchstabe": letter, "Anzahl": count})
    
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
    
        
    
    