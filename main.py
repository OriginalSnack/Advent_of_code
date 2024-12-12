data = """
"""


def function_change(unsafe, j):
    if j >= len(unsafe):
        return False
    temp_list = unsafe.copy()
    temp_list.pop(j)
    if element_check_safe(temp_list):
        return True
    else:
        return function_change(unsafe, j + 1)


def element_check_safe(element):
    is_descending = all(element[i] > element[i + 1] for i in range(len(element) - 1))
    is_increasing = all(element[i] < element[i + 1] for i in range(len(element) - 1))
    is_different = all(1 <= abs(element[i] - element[i + 1]) <= 3 for i in range(len(element) - 1))
    if is_different and is_increasing != is_descending:
        return True
    else:
        return False

def function_check(dat):
    count = 0
    list_unsafe = []
    data_list = [[int(num) for num in row.split()] for row in dat.splitlines()]
    for i in range(len(data_list)):
        if element_check_safe(data_list[i]):
            count += 1
        else:
            list_unsafe.append(data_list[i])
    return list_unsafe,count

light_list,count = function_check(data)
for i in range(len(light_list)):
    if function_change(light_list[i],0):
        count+=1
print(count)

