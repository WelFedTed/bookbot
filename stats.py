def get_num_words(book_text):
    return len(book_text.split())

def get_char_list(book_text):
    text = book_text.lower()
    char_list = {}
    for char in text:
        if char not in char_list:
            char_list[char] = 1
            continue
        char_list[char] += 1
    return char_list
