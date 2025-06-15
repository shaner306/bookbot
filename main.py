from stats import get_num_words, get_character_count
import sys

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] if len(sys.argv) > 1 else 'book.txt'
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at: {book_path}...')
    print('----------- Word Count ----------')
    with open(book_path, 'r') as file:  
        book_text = file.read()
    #count words
    word_count = get_num_words(book_text)
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    #count characters
    character_count = get_character_count(book_text)
    character_count = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    for char, count in character_count.items():
        print(f'{char}: {count}')
    
    print("============ END ============")