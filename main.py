import re

with open("data", "r", encoding="utf-8") as file:
    memory = file.read()


def mul(a, b):
    return a * b


def find_mul(content):
    count = 0
    list_functions = []
    position = re.findall(r'mul\((-?\d+),\s*(-?\d+)\)', content)
    for i in range(len(position)):
        list_functions.append(list(position[i]))

    for i in range(len(list_functions)):
        list_functions[i][0] = int(list_functions[i][0])
        list_functions[i][1] = int(list_functions[i][1])

    for i in range(len(list_functions)):
        count += mul(list_functions[i][0], list_functions[i][1])

    return count
print(find_mul(memory))