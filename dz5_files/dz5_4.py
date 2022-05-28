numbers_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text4.txt", 'r', encoding='utf-8') as f1:
    content = f1.read()
    for key in numbers_dic.keys():
        content = content.replace(key, numbers_dic.get(key))
with open("text4_result.txt", 'w+', encoding='utf-8') as f2:
    f2.write(content)
    f2.seek(0)
    print(f2.read())
