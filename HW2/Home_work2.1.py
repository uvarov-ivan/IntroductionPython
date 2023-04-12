'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все
монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть'''

import random
numbers = int(input('Введите количество монеток: '))

tails_count = 0
emblem_count = 0

for i in range(numbers):
    coin_side = random.randint(0,1)
    print(coin_side)
    if coin_side == 0: tails_count += 1
    else: emblem_count += 1
print()
if tails_count <= emblem_count: print(f"Нужно перевернуть минимум {tails_count} монеток")
else:print(f"Нужно перевернуть минимум {emblem_count} монеток")