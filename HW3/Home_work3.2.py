'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5'''

import random
amount_of_elements = int(input('Введите количество элементов: '))
desired_value = int(input('Введите искомый элемент: '))

my_list = [random.randint(0,100) for i in range(amount_of_elements)]
print(my_list)
min_difference = 100

i = 0
while i < len(my_list):
    if my_list[i] >= desired_value: difference = my_list[i] - desired_value
    else: difference = desired_value - my_list[i]
    if min_difference > difference:
        min_difference = difference
        nearest_index = i
    i += 1
print(my_list[nearest_index])