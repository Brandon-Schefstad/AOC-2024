import os
import sys
from numpy import sort
import re

file_to_open = open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"))


def use_regex(input_text):

    if pattern.match(input_text):
        return True


sum = 0
pattern = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
for entry in file_to_open.readlines():

    splitted = entry.split("don't()")
    for line in splitted:
        x: list[str] = re.findall(pattern, line.split("do()")[0])
        for mult in x:
            mult_2 = mult.replace("mul(", "").replace(")", "")
            print(mult_2)
            [num_1, num_2] = [int(num) for num in mult_2.split(",")]
            sum += num_1 * num_2

print(sum)
