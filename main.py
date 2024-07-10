
def main():
    with open("/root/workspace/github.com/kimberlyseurai/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()

    book_path = "books/frankenstein.txt"
    num_words = count(file_contents)
    chars_dict = count_char(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)


    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def count(string):  
    words = string.split()

    return len(words)
   


def count_char(string):

    letter_dict = {}
    new_string = string.lower()

    for i in new_string:
        if i in letter_dict.keys():
            letter_dict[i] += 1
        else: 
            letter_dict[i] = 1
        
    return letter_dict


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []

    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
        
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(d):
    return d["num"]

if __name__ == "__main__":
    main()