# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponentiaton(number, degr, res=1):
    if degr == 0: return 1
    return number * exponentiaton(number, degr - 1, res)


num = int(input('Введите число-> '))
deg = int(input('Введите степень числа-> '))
print(exponentiaton(num, deg))
