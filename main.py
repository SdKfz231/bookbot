import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_on

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)      
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_counts = get_char_count(text)
    list_of_counts = []
    for name, num in char_counts.items():
        list_of_counts.append((name, num))
    sorted_list = sorted(list_of_counts, reverse=True, key=lambda x: x[1])
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for item in sorted_list:
        print(f' {item[0]}: {item[1]}')
    print('============= END ===============')

main()
