def get_num_words(book_string):
    words = book_string.split()
    return len(words)

def char_times(book_string):
    dict = {}
    for l in book_string.lower():
        if l not in dict:
            dict[l] = 1
        else:
            dict[l] += 1

    return dict

def format_dict(char_dict):
    new_list = [{"char": char, "count": count} for char, count in char_dict.items()]

    new_list.sort(reverse=True, key=lambda x: x["count"])

    return new_list

