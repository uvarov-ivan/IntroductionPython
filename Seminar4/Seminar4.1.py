# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

my_string = 'a a a b c a a d c d d'
my_list = my_string.split()
print(my_list)

for i in my_list:
    j = 0
    count = 0
    while j < len(my_list):

        if my_list[j] == i: count += 1
        if my_list[j] == i and count != 0: my_list[j] += '_' + str(count)
        j += 1
print(my_list)