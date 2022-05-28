f = open("text.txt", 'w+')
stop = False
prevLine = ''

while not stop:
    line = input(':')
    if line == '':
        stop = True
    f.write(line + '\n')
    prevLine = line.strip()
print("You input:")
f.seek(0)
print(f.read())
f.close()