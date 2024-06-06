def main():
    print('--- Begin report of books / frankenstein.txt - --')
    print(f"{get_words()} words found in the document")
    print()

    for letter, count in letter_count_dict().items():
        print(f"The '{letter}' character was found {count} times")

    print('--- End report ---')


def letter_count_dict():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_count = {letter: 0 for letter in alphabet}

    # Convert all characters to lower case
    book_text = get_book().lower()

    # Count the occurrence of each letter
    for letter in book_text:
        if letter in letter_count:
            letter_count[letter] += 1
    return letter_count


def get_words():
    words = get_book().split()
    return len(words)


def get_book():
    file_path = '/Users/essienebong/workspace/github.com/essienjames/bookbot/books/frankenstein.txt'
    with open(file_path) as file:
        contents = file.read()
    return contents


main()
