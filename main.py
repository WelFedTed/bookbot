from itertools import count
def get_book_text(book):
    file = open(book)
    return file.read()

def count_book_words(book_text):
    return len(book_text.split())

def main():
    num_words = count_book_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()
