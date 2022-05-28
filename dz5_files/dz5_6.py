subj = {}
with open("text6.txt", 'r', encoding='utf-8') as f:
    for line in f:
        subject = ""
        i = 0
        length = len(line)
        while i < len(line):
            symbol = line[i]
            i += 1
            if symbol != ':':
                subject += symbol
            else:
                break
        summary = 0
        number = ''
        while i < len(line):
            symbol = line[i]
            i += 1
            if symbol.isdigit():
                number += symbol
            elif len(number) > 0:
                summary += int(number)
                number = ''
        subj[subject] = summary
print(subj)
