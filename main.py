import pathlib

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        book_string = f.read()
    return book_string
    

def count_words_in_book(book_text):
    return len(book_text.split())

def count_characters_in_book(book_text):
    character_count = {}

    for character in book_text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def convert_dict_to_list_of_dicts(dictionary):
    return [{"character":k, "count":v} for k,v in dictionary.items()]



def main():
    root_dir = pathlib.Path().cwd()
    file_path = root_dir / "frankenstein.txt"
    frankenstein_book = get_book_text(book_file_path=file_path)
    num_words = count_words_in_book(book_text=frankenstein_book)
    character_count = count_characters_in_book(book_text=frankenstein_book)
    sorted_character_count_records = convert_dict_to_list_of_dicts(dictionary=character_count)
    sorted_character_count_records.sort(reverse=True, key=lambda d: d["count"])

    
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document\n")
    for record in sorted_character_count_records:
        if record["character"].isalpha():
            print(f"The {record["character"]} chracter was found {record["count"]} times")


if __name__ == "__main__":
    main()