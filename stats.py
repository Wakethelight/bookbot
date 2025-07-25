#takes the content from the book, and counts the words
def get_count_words(book_text):
    book_words = book_text.split()
    return len(book_words)


#takes text from book and counts number of times each character (including symbol and space) appear in string
def get_character_count(book_text):
    character_count = {}
    book_text = book_text.lower()
    for character in book_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

#this will take my disctionary and return a sorted list of the dictionary
def sort_character(characters):
    return characters["num"]

def character_dict_to_sorted_list(num_chars_dict):
    sorted_character_list = []
    for ch in num_chars_dict:
        sorted_character_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_character_list.sort(reverse=True, key=sort_character)
    return sorted_character_list





