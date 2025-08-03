from stats import get_num_words

def get_book_text(book):
    file = open(book)
    return file.read()

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()
