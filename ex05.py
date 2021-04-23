def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if word[0] in vowels:
        return word + 'way'

    return word[1:] + word[0] + 'ay'


print(pig_latin('rojin'))