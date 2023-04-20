# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random

number_of_trees = int(input('Введите количество деревьев: '))
max_num_of_berries_on_one_tree = int(input('Введите максимальное количество ягод на одном дереве: '))

bed_of_trees = [random.randint(0, max_num_of_berries_on_one_tree) for _ in range(number_of_trees)]
print(bed_of_trees)

max_num_of_berries_on_three_trees = 0

i = -1
while i < len(bed_of_trees)-1:
    num_of_berries_on_three_trees = bed_of_trees[i-1] + bed_of_trees[i] + bed_of_trees[i+1]
    if max_num_of_berries_on_three_trees < num_of_berries_on_three_trees:
        max_num_of_berries_on_three_trees = num_of_berries_on_three_trees
        if i < 0:max_tree = len(bed_of_trees)
        else:max_tree = i + 1
    i += 1
print(f'За один заход собирающий модуль может собрать максимум {max_num_of_berries_on_three_trees} ягод, находясь перед деревом № {max_tree}')