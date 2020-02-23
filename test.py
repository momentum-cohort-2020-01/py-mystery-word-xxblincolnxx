
with open('words.txt', 'r') as file:
    open_file = file.readlines()
    possible_words = [word.replace('\n','').upper() for word in open_file if len(word) == 7]
    print(len(possible_words))