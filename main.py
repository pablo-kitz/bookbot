from stats import get_num_words
from stats import char_times
from stats import format_dict
import sys

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print(book_path)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = char_times(text)
    formatted = format_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in formatted:
        if (entry["char"].isalpha()):
            print(f"{entry['char']}: {entry['count']}")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()

