def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    punctuations = [',', '.', ';', ':']
    p = ''
    all_chars = [ ch for ch in word if ch in vowels]

    if word[-1] in punctuations:
        p = word[-1]
        word = word.rstrip(word[-1])
    
    if len(set(all_chars)) >= 2:
        return word + 'way' + p

    return word[1:] + word[0] + 'ay' + p


print(pig_latin('wine,'))