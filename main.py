import sys
from stats import count_words, count_character, sorted_characters_count


def get_book_text(path_to_file):
	with open(path_to_file, 'r', encoding='utf-8') as f:
		file_contents = f.read()
		return file_contents

def main():

	# If sys.argv doesn't have two entries:

    #Print a message explaining how to use the program: Usage: python3 main.py <path_to_book>
    #Exit the program with a status code of 1 using sys.exit(1)
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1] #"./books/frankenstein.txt"
	book = get_book_text(book_path)
	sorted_characters_counts = sorted_characters_count(count_character(book))
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {count_words(book)} total words")
	print("--------- Character Count -------")
	for character in sorted_characters_counts:
		if character.isalpha():
			print(f"{character}: {sorted_characters_counts[character]}")
	print("============= END ===============")
main()