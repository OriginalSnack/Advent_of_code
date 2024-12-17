import re


def mul(a, b):
    return a * b


count = 0

with open("data", "r", encoding="utf-8") as file:
    content = file.read()

position = re.findall(r'mul\((-?\d+),\s*(-?\d+)\)', content)
print(f"Found {len(position)} matches: {position}")
print(type(position[0]))

list_functions = []
for i in range(len(position)):
    list_functions.append(list(position[i]))

for i in range(len(list_functions)):
    list_functions[i][0] = int(list_functions[i][0])
    list_functions[i][1] = int(list_functions[i][1])

for i in range(len(list_functions)):
    count += mul(list_functions[i][0], list_functions[i][1])

print(count)
