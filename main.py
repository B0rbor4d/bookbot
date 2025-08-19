import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import (count_words, count_letters, sort_list)
    


def main():
    if(len(sys.argv) < 2):
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print(f"----------- Word Count ----------")
        print(f"Found {count_words(get_book_text(path_to_file))} total words")
        print(f"--------- Character Count -------")
        #print(f"{sort_list(count_letters(get_book_text(path_to_file)))}")

        sorted_letters = sort_list(count_letters(get_book_text(path_to_file)))
        for letter in sorted_letters:
            print(f"{letter["Buchstabe"]}: {letter["Anzahl"]}")
        
        print(f"============= END ===============")
    

main()