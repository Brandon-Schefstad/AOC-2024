import os
import sys
from numpy import sort

file_to_open = open(os.path.join(os.path.dirname(sys.argv[0]), "input.txt"))


def check_line_increase(report):
    for index in range(0, len(report)):
        if index != 0:
            if 1 <= report[index] - report[index - 1] <= 3:
                pass
            else:
                return report[index] if report[index] != 1 else 0
    return True


def check_line_decrease(report):
    for index in range(0, len(report)):
        if index != 0:
            if 1 <= report[index - 1] - report[index] <= 3:
                pass
            else:
                return report[index] if report[index] != 1 else 0
    return True


safe_count = 0

for entry in file_to_open.readlines():
    report = entry.split(" ")
    report[-1] = report[-1].replace("\n", "")
    for num in report:
        report[report.index(num)] = int(num)

    passes_increase = check_line_increase(report) == True
    passes_decrease = False

    if not passes_increase or type(passes_increase) == int:
        passes_decrease = check_line_decrease(report) == True

    print(
        f"""{report}
        Increase? {passes_increase}
        Decrease? {passes_decrease}"""
    )

    if passes_increase:
        safe_count += 1
    elif passes_decrease:
        safe_count += 1
    else:
        print(f"""failure for report: {report}""")
    # if passes_decrease == True:
    #     safe_count += 1

    # print("MODIFYING REPORT", report)
    # report = report.remove(safety_check)
    # safe_bool = check_line_increase(report)

    # safe_count += safe_bool

print(safe_count)
