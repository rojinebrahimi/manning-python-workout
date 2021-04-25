from os import path

# Creates a sentence based on the first character of each line
def creat_sentence():
    file = input("File address: ")

    if path.exists(file):
        try:
            sentence = []
            with open(file, 'r+') as f:
                lines = f.readlines()
                
                for line in lines:
                    sentence.append(line.split(" ")[0])
        
        except Exception as e:
            print(e)

    return " ".join(sentence)

# Creates Pig Latin of the given sentence
def pl_sentence(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split(" ")
    pig_latin_words = []

    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(f"{word}way")
        
        elif word[0] not in vowels and word != '\n':
            pig_latin_words.append(f"{word[1:]}{word[0]}ay")

    return pig_latin_words

print(" ".join([ element for element in pl_sentence(creat_sentence()) ]))