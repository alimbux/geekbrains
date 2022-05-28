from sys import argv

script_name, working_hours, rate, bonus = argv


def salary(working_hours_, rate_, bonus_):
    return int(working_hours_) * float(rate_) + float(bonus_)


print(salary(working_hours, rate, bonus))
