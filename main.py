def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import count_words
from stats import count_letters

    


def main():
    path_to_file = "./books/frankenstein.txt"
    print(f"{count_words(get_book_text(path_to_file))} words found in the document")
    print(f"{count_letters(get_book_text(path_to_file))}")

main()