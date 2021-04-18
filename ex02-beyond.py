def mysum(*numbers, extra=0):
    result = 0
    
    for item in numbers:
        result += item
        
    return result + extra

def average(*numbers):
    return mysum(*numbers) / len(numbers)

def word_length(*words):
    w = [ len(w) for w in words ]
    return (max(w), int((max(w) + min(w)) / len(words)), min(w))
 

print(mysum(1, 6, 219.42, .7, 9, 17, 0))
print(mysum(*[1, 6, 219.42, .7, 9, 17.89, 0.9]))
print(average(1, 6, 219.42, .7, 9, 17, 0))
print(word_length("Love", "Coding", "This", "Way", "!"))
