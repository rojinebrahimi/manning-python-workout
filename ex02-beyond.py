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
 
def sum_objects(*objects):
    object_tup = objects
    result = []
    for item in object_tup:
        if type(item) == int or type(item) == float or (type(item) == str and not item.isalpha()):
            result.append(float(item))
    mysum(*result)

print(mysum(1, 6, 219.42, .7, 9, 17, 0))
print(mysum(*[1, 6, 219.42, .7, 9, 17.89, 0.9]))
print(average(1, 6, 219.42, .7, 9, 17, 0))
print(word_length("Love", "Coding", "This", "Way", "!"))
print(sum_objects(.1, 6, "219.42", "test", 9, 17, 0.00000, "#"))
