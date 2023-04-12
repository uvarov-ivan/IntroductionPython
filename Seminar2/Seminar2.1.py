'''Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6'''

a = int(input())

first = 0
second = 1
count = 2

while a > second:
    first, second = second, first + second
    count += 1

if a == second:
    print(count)
else:
    print(-1)
