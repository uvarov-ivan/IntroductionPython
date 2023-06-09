# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# # 123456 -> no

ticketNum = input("Введите номер билета: ")
if len(ticketNum) == 6:
    sumLeft = 0
    sumRight = 0
    i = 0
    while i < 3:
        sumLeft += int(ticketNum[i])
        sumRight += int(ticketNum[5-i])
        i += 1
    if sumLeft == sumRight:
        print("Ваш билет счастливый!")
    else:
        print("Ваш билет несчастливый, срочно выбросите его!")
else:
    print("Вы ввели неправильный номер билета!")
