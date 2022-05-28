f = open("text2.txt", 'r', encoding='utf-8')
content = f.readlines()

count = 0
for line in content:
    count += 1
    words = line.split(' ')
    words_number = len(words) if line.strip() != '' else 0
    print("Line{}, words {}: {}".format(count, words_number, line.strip()))
f.close()
