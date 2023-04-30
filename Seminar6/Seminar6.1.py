# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
# что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
import random

print(my_list := [random.randint(0, 10) for _ in range(int(input('Введите длину списка-> ')))])

# my_set = {i for i in my_list}

# res = 0
# for i in set(my_list):
#     res += (my_list.count(i) - 1) * my_list.count(i) // 2

print(f'В данном списке образуется {sum((my_list.count(i) - 1) * my_list.count(i) // 2 for i in set(my_list))} пар равных чисел.')