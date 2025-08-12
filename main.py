def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_content):
    words = file_content.split()
    return len(words)
    


def main():
    path_to_file = "./books/frankenstein.txt"
    print(f"{count_words(get_book_text(path_to_file))} words found in the document")

main()