from stats import get_book_text
from stats import get_num_of_words
from stats import get_num_of_characters
from stats import dict_sort
import sys

def main():
    try:
        sys.argv[1] == True
        book_filepath = sys.argv[1]
        word_count = get_num_of_words(get_book_text(f"{book_filepath}"))
        sorted_list = dict_sort(get_num_of_characters(get_book_text(f"{book_filepath}")))
        readable_list = []
        for i in sorted_list:
            if i["char"].isalpha():
                readable_list.append({i["char"]: i["num"]})
        print(f"============ BOOKBOT ============\nAnalyzing book found at {book_filepath}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
        for i in readable_list:
            print('\n'.join("{}: {}".format(k, v) for k, v in i.items()))
        print("============= END ===============")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()