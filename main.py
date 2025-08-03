def get_book_text(book):
    # while open(book) as f:
    #     file_contents = f.read()
    #     return file_contents
    file = open(book)
    return file.read()


def main():
    print(get_book_text("books/frankenstein.txt"))

main()
