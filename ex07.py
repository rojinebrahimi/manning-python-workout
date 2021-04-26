def ubbi_dubbi(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    ubbi_word = []

    for char in word:
        if char in vowels:
            ubbi_word.append("ub" + char)
        
        else:
            ubbi_word.append(char)

    return "".join(ubbi_word)


print(ubbi_dubbi('manning_book'))