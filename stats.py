def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_num_of_words(book_text):
    words = book_text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def get_num_of_characters(book_text):
    char_dict = {}
    lowercase_text = book_text.lower()
    for character in lowercase_text:
        if character not in char_dict:
            char_dict[f"{character}"] = 1
        else:
            char_dict[f"{character}"] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def dict_sort(num_of_chars):
    list_of_dicts = []
    for pair in num_of_chars:
        list_of_dicts.append({"char": f"{pair}", "num": num_of_chars[pair]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts