f = open("text3.txt", 'r')
content = f.readlines()

sum_salary = 0
persons = []
print("Persons with salary less than 20000:")
for line in content:
    person_list = line.split(' ')
    person_dic = {"surname": person_list[0], "salary": float(person_list[1])}
    persons.append(person_dic)
    sum_salary += person_dic["salary"]
    if person_dic["salary"] < 20000:
        print(person_dic["surname"])
print("Average salary is: %.2f" % (sum_salary/len(persons)))
f.close()