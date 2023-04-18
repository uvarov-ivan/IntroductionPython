'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1'''

import random
number_of_signs = int(input('Введите количество элементов: '))
desired_number = int(input('Введите искомое число: '))
count = 0

my_list = [random.randint (0, 10) for i in range(number_of_signs)]
print(my_list)
for i in my_list:
    if i == desired_number: count += 1

print(count)
