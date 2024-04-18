def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    words = len(text.split())
    char_dict = get_char_dict(text)
    char_dict_list = get_char_dict_list(char_dict)
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print("")
    
    for char in char_dict_list:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")


def get_char_dict_list(char_dict: dict):
    char_dict_list = []
    for char in char_dict:
        if char.isalpha():
            char_dict_list.append({"char": char, "count": char_dict[char]})
    char_dict_list.sort(key=lambda letter: letter["count"], reverse=True)
    
    return char_dict_list


def get_text(file: str):
    with open(file) as f:
        return f.read()


def get_char_dict(text: str):
    lower_case_text = text.lower()
    char_dict = {}
    
    for char in lower_case_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict


main()
