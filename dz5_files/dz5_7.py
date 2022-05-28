import json
count = 0
firm_dic = {}
profit = 0
firm_list = []
with open("text7.txt", 'r', encoding='utf-8') as f:
    for line in f:
        firm_data = line.split(" ")
        if len(firm_data) == 4:
            benefit = int(firm_data[2]) - int(firm_data[3])
            if benefit > 0:
                profit += benefit
            count += 1
            firm_dic[firm_data[0]] = benefit
firm_list.append(firm_dic)
firm_list.append({"average_profit": round(profit/count,2)})
with open("text7_result.txt", 'w+', encoding='utf-8') as f:
    json.dump(firm_list, f)
    f.seek(0)
    print(f.read())

