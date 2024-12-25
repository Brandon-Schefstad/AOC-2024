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

list_1 = sort(list_1)
list_2 = sort(list_2)

total = 0
for index in range(0, len(list_1)):
    if index != 0:
        try:
            assert list_1[index] >= list_1[index - 1]
            assert list_2[index] >= list_2[index - 1]
            assert list_2[index] - list_1[index] >= 0
        except:
            print("---ERROR---")
            print(
                f"{list_2[index]} - {list_1[index]} = {list_2[index] - list_1[index]}"
            )

    difference = list_2[index] - list_1[index]
    total += abs(difference)

print(total)
print(sum(list_2) + sum(list_1))
