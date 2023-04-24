# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# 2 2 -> 4

def sum_numbers(first, second):
    if second == 0: return first
    return 1 + sum_numbers(first, second - 1)


first_num = int(input('Введите первое слагаемое-> '))
second_num = int(input('Введите второе слагаемое-> '))
print(sum_numbers(first_num, second_num))
