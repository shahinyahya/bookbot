
#? Read the file contents function
def get_book_text(path):
    # path_input = input("Input your file path: ")

    with open(path, 'r') as f:
        return f.read()


#? Function to count number of words after reading the file.
def get_num_words(book_text):
    """ 
        Read the text file and count the words in the book.
    """
    
    book_arr = book_text.split()

    num_words = len(book_arr)

    return f"Found {num_words} total words"

#? Function to count total characters in the book.
def text_letter_count(book_text):
    """
        Count the number of letters appeared in times.
    """
    text = book_text.lower()

    char_count = {}

    for char in text:
        if char is None:
            continue
        if char == " ":
            continue
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

#? Function to sort the counted characters found in the book
def char_count_sort(book_text):
    letter_counts = text_letter_count(book_text)

    sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

    for k,v in sorted_counts:
        print(f"{k}: {v}")

    return