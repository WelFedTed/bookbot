from stats import get_num_words
from stats import get_char_list
from stats import sort_char_list

def get_book_text(book):
    file = open(book)
    return file.read()

def main():
    print("============ BOOKBOT ============")
    book = get_book_text("books/frankenstein.txt")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_list = get_char_list(book)
    char_list = sort_char_list(char_list)
    for i in char_list:
        if i.isalpha():
            print(f"{i}: {char_list[i]}")
    print("============= END ===============")

main()
