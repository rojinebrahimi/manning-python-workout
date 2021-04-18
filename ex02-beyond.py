def mysum(*numbers, extra=0):
    result = 0
    
    for item in numbers:
        result += item
        
    return result + extra


def average(*numbers):
    return mysum(*numbers) / len(numbers)


print(mysum(1, 6, 219.42, .7, 9, 17, 0), 10)
print(mysum(*[1, 6, 219.42, .7, 9, 17.89, 0.9], 10))
print(average(1, 6, 219.42, .7, 9, 17, 0))