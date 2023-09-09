# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

def find_i(list_1):
    new_list = []
    for i in range(len(list_1)):
        if (list_1[i] <= maxi and list_1[i] >= mini):
            new_list.append(i)
            i += 1
    return new_list
    
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
maxi = 10
mini = 7  

print(find_i(list_1))