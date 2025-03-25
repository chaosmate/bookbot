from stats import get_num_words, get_num_chars, get_sorted_chars
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_book):
    string_of_words = get_book_text(path_to_book)
    num_words = get_num_words(string_of_words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars_dict = get_num_chars(string_of_words)
    sorted_list_of_chars = get_sorted_chars(chars_dict)
    for dict_pair in sorted_list_of_chars:
        print(f"{dict_pair['char']}: {dict_pair['num']}")
    print("============= END ===============")
    
main(sys.argv[1])