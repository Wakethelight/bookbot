filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
    return file_content

def main(get_book_text, filepath):
    book_text = get_book_text(filepath)
    print(book_text)

if __name__ == "__main__":
    main(get_book_text, filepath)
# This code reads the content of a book file and prints it to the console.