from stats import get_num_words, get_num_chars, get_sorted_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    string_of_words = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(string_of_words)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars_dict = get_num_chars(string_of_words)
    sorted_list_of_chars = get_sorted_chars(chars_dict)
    for dict_pair in sorted_list_of_chars:
        print(f"{dict_pair['char']}: {dict_pair['num']}")
    print("============= END ===============")
    
main()