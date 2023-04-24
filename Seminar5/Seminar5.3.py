# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

def sequence_reversal(num, my_string = ""):
    if num == 0: return my_string
    return my_string + " " + str(num) + sequence_reversal(num - 1)



my_line = int(input('Введите длину последовательности -> '))

# my_line = my_line[0] + '5' + my_line[2:]
print(sequence_reversal(my_line))