a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

def add_nums(a, b):
    total = a + b
    return total

add_nums(a, b)

def subtract_nums(c, d):
    total = add_nums(a, b)
    difference = total - c - d
    print(difference)

subtract_nums(45, 5)

