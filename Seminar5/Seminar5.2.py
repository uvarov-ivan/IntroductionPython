# 35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def prime_num(num):
    divider = num // 2 + 1
    while divider > 2:
        divider -= 1
        if num % divider == 0: return (f'Число {num} не является простым!')
    return (f'Число {num} является простым!')

my_num = int(input('Введите число для проверки -> '))

print(prime_num(my_num))