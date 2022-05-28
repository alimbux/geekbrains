from random import randint
with open("text5.txt", 'w', encoding='utf-8') as f:
    for number in range(0, randint(0, 10)):
        f.write(f"{randint(0, randint(0, 10))} ")
summary = 0;
with open("text5.txt", 'r', encoding='utf-8') as f:
    number = ""
    while True:
        symbol = f.read(1)
        if symbol == ' ':
            summary += int(number)
            number = ''
        elif symbol == '':
            break
        else:
            number += symbol
print(f"sum={summary}")
