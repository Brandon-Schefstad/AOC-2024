import os
import sys
from numpy import sort

file_to_open = open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"))

list_1 = []
list_2 = []

for line in file_to_open.readlines():
    lists = line.split("   ")
    list_1.append(int(lists[0]))
    list_2.append(int(lists[1].replace("\n", "")))

assert len(list_1) == len(list_2)

total = 0

for num in list_1:
    try:
        assert num in list_2
        multiplier = list_2.count(num)
        total += multiplier * num
    except:
        pass

print(total)
