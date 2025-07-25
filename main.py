#import needed modules from other files
from stats import (
    get_count_words,
    get_character_count,
    character_dict_to_sorted_list
)


# this is the main function that calls get_book_text and prints the book text
def main():
    #filepath to the book
    filepath = "books/frankenstein.txt"
    #get the book text as string from book file
    book_text = get_book_text(filepath)
    #get word count from book text
    book_word_count = get_count_words(book_text)
    #get the book character count as dictionary
    book_character_dict = get_character_count(book_text)
    book_character_sorted_list = character_dict_to_sorted_list(book_character_dict)
    print_report(filepath, book_word_count, book_character_sorted_list)



def print_report(filepath, book_word_count, book_character_sorted_list):
    #print report
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}...')
    print("----------- Word Count ----------")
    print(f'Found {book_word_count} total words')
    print("--------- Character Count -------")
    for character in book_character_sorted_list:
        if not character["char"].isalpha():
            continue
        print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

# this gets the book text from a given file in "filepath" variable and returns the contents
def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
    return file_content





if __name__ == "__main__":
    main()
# This code reads the content of a book file and prints it to the console.