def pl_sentence(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split(" ")
    pig_latin_words = []
    
    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(f"{word}way")
        
        pig_latin_words.append(f"{word[1:]}{word[0]}ay")
    
    return pig_latin_words

print(" ".join([ element for element in pl_sentence("hi this is rojin") ]))