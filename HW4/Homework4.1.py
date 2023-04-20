# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

set_length1 = int(input('Введите количество элементов первого множества: '))
set_length2 = int(input('Введите количество элементов второго множества: '))
max_num = int(input('Введите максимальный предел элемента: '))

my_list1 = [random.randint(0, max_num) for _ in range(set_length1)]
my_list2 = [random.randint(0, max_num) for _ in range(set_length2)]

print(my_list1)
print(my_list2)

my_set1 = set()
my_set2 = set()

for i in my_list1:
    my_set1.add(i)

for i in my_list2:
    my_set2.add(i)

for i in my_set1.intersection(my_set2):
    print(i, end=', ')