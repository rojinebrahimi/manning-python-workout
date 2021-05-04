# applies on all sequences in Python
def indexed_sums(numbers):
    return sum(numbers[0::2]), sum(numbers[1::2])


print(indexed_sums([10, 20, 30, 40, 50, 60]))


