from itertools import count
from itertools import cycle

counter = 0
for el in count(int(input('Enter init number:'))):
    counter += 1
    print(el)
    if counter >= 10:
        break

cycle_list = [1, 2, 3, 4]
counter = 0
cycle_counter = 0
for el in cycle(cycle_list):
    counter += 1
    print(el)
    if counter == len(cycle_list):
        counter = 0
        cycle_counter += 1
        print(f"Cycle number {cycle_counter} finished")
    if cycle_counter >= 10:
        break
