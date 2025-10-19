from stats import get_num_words, char_count_sort, get_book_text
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File not found at path '{book_path}'")
        sys.exit(1)

    count_words = get_num_words(book_text)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(count_words)
    print("--------- Character Count -------")
    char_count_sort(book_text)
    print("============= END ===============")


main()
