def mysum(*numbers):
    result = 0
    
    for item in numbers:
        result += item
        
    return result


print(mysum(1, 6, 219.42, .7, 9, 17, 0))
