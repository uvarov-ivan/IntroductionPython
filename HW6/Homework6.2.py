# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random


def search_index_in_range(basic_list: list, min: int, max: int) -> list:
    res_index_list = []
    for i in range(len(basic_list)):
        if min <= basic_list[i] <= max:
            res_index_list.append(i)
    return res_index_list


min_num = int(input('Задайте минимум-> '))
max_num = int(input('Задайте максимум-> '))

print(my_list := [random.randint(-100, 100) for _ in range(int(input('Введите длину списка-> ')))])
print(search_index_in_range(my_list, min_num, max_num))
