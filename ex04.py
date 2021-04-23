def hex_output(hex_number):
    convert = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    length = int(len(str(hex_number)))
    decimal = 0
    
    for d in str(hex_number):
        if d in convert.keys():
            d = convert[d]
        decimal += (16 ** (length - 1)) * int(d)
        length -= 1

    return decimal


print(hex_output("C9"))