def count_words(book):
    num_words = len(book.split())
    return f"{num_words}"


def  count_character(text):
    # count each character and put into dictionary
    char_count = {}
    for ch in text:
        lower_ch = ch.lower()
        if lower_ch not in char_count:
            char_count[lower_ch] = 1
        else:
            char_count[lower_ch] += 1
    # print the dictionary
    return char_count


def sorted_characters_count(text):
    # sort dictionary by value
    return dict(sorted(text.items(), key=lambda item: item[1], reverse=True))