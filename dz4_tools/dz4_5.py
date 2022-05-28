from functools import reduce

init_list = list(range(100, 1001, 2))
print(init_list)
print(reduce(lambda prev, current: prev * current, init_list))
