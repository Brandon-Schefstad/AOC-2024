import os
import sys
from numpy import sort
import re

file_to_open = open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"))

entire_word_search_dict = dict()
opened_file = file_to_open.readlines()

count = 0
# Search in same row forwards
def search_X_MAS(row):
    xmas_count = 0
    for index in range(0, len(row)):

        if (
            index <= len(row) - 3
            and row[index] == "X"
            and row[index + 1] == "M"
            and row[index + 2] == "A"
            and row[index + 3] == "S"
        ):
            xmas_count += 1
            # print(f"XMAS found starting at position {index} in {row}")

        if (
            index >= 3
            and row[index] == "X"
            and row[index - 1] == "M"
            and row[index - 2] == "A"
            and row[index - 3] == "S"
        ):
            xmas_count += 1
            # print(f"XMAS backwards found starting at position{index} in {row}")
    return xmas_count

    


def search_XMAS_in_column(row_1, row_2, row_3, row_4):
    xmas_count = 0
    for index in range(0, len(row_1)):

        if (
            row_1[index] == "X"
            and row_2[index] == "M"
            and row_3[index] == "A"
            and row_4[index] == "S"
        or
            row_1[index] == "S"
            and row_2[index] == "A"
            and row_3[index] == "M"
            and row_4[index] == "X"

        ):
            xmas_count +=1
            # print(f"XMAS found in column starting at position{index} in {row_1}")
    return xmas_count


def search_XMAS_left_to_right_in_diagonal(row_1, row_2, row_3, row_4):
    xmas_count = 0
    for index in range(0, len(row_1) - 3):
        if (
            row_1[index] == "X"
            and row_2[index + 1] == "M"
            and row_3[index + 2] == "A"
            and row_4[index + 3] == "S"
        or 
        
            row_1[index] == "S"
            and row_2[index + 1] == "A"
            and row_3[index + 2] == "M"
            and row_4[index + 3] == "X"
        ):
            xmas_count+=1
            # print(f"XMAS found diagonal left to right starting at position{index} in {row_1}")
    return xmas_count

def search_XMAS_right_to_left_in_diagonal(row_1, row_2, row_3, row_4):
    xmas_count = 0
    for index in range(0, len(row_1)-4):
        if (
            row_1[index+3] == "X"
            and row_2[index+2] == "M"
            and row_3[index+1] == "A"
            and row_4[index] == "S"
        or
            row_1[index+3] == "S"
            and row_2[index+2] == "A"
            and row_3[index+1] == "M"
            and row_4[index] == "X"
        ):
            xmas_count+=1
            # print(f"XMAS found diagonal right to left but backwards starting at position {index+3} in {row_1}")
    return xmas_count


for index in range(0, len(opened_file)):
    entry = opened_file[index]
    letters_by_column = dict()
    split_row = [x for x in entry]
    for i in range(0, len(split_row)):
        letters_by_column[i] = split_row[i]

    entire_word_search_dict.__setitem__(f"{index}", letters_by_column)

# print(entire_word_search_dict)

for row in entire_word_search_dict:
    count += search_XMAS_in_row(entire_word_search_dict[row])

    int_row = int(row)
    if int_row <= len(entire_word_search_dict.keys()) - 4:
        count += search_XMAS_in_column(
            entire_word_search_dict[str(int_row)],
            entire_word_search_dict[str(int_row + 1)],
            entire_word_search_dict[str(int_row + 2)],
            entire_word_search_dict[str(int_row + 3)],
        )
        count += search_XMAS_left_to_right_in_diagonal(
            entire_word_search_dict[str(int_row)],
            entire_word_search_dict[str(int_row + 1)],
            entire_word_search_dict[str(int_row + 2)],
            entire_word_search_dict[str(int_row + 3)],
        )
        count += search_XMAS_right_to_left_in_diagonal(
            entire_word_search_dict[str(int_row)],
            entire_word_search_dict[str(int_row + 1)],
            entire_word_search_dict[str(int_row + 2)],
            entire_word_search_dict[str(int_row + 3)],
        )




print(count)

