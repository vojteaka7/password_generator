import json
import random

def generate(allowed): # allowed is string with representative characters
    f = open('words_dictionary.json', 'r')
    word_list = json.load(f)
    f.close()
    word_list = list(word_list.keys())

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special = ',?.:-_!()%=+'
    numbers = '0123456789'
    char_types_dict = {'a': lower, 'A': upper, '!': special, '0': numbers, 'w': word_list}

    password = ''
    chars = 0
    while chars < 8:
        char_type = random.choice(allowed)
        added_char = '123456'
        while len(added_char) > 5:
            added_char = random.choice(char_types_dict[char_type])
        password += added_char
        chars += len(added_char)

    return password

if __name__ == '__main__':
    while True:
        print(generate(input('Input the allowed characters: ')))
