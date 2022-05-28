def fact(number):
    start_from = 1
    number = int(number)
    for elem in range(1, number + 1):
        start_from = start_from * elem
        yield start_from


n = input("Enter number: ")
for el in fact(n):
    print(el)
