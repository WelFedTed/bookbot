from stats import get_num_words
from stats import get_char_list

def get_book_text(book):
    file = open(book)
    return file.read()

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    print(f"{num_words} words found in the document")
    char_list = get_char_list(book)
    print(char_list)

main()
