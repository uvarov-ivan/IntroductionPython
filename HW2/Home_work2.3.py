#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

limit = int(input('Введите предел: '))
power_of_two = 1

while power_of_two <= limit:
    print(f"{power_of_two}")
    power_of_two *= 2