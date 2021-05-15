def mysum(*items):
    if not items:
        return items
    else:
        result = items[0]
        for i in items[1:]:
            result += i
        return result
        
        
print(mysum(1, 2, 4))
print(mysum(*[1, 2, 4]))
print(mysum(*(1, 2, 4)))
print(mysum('Ro', 'jin'))
