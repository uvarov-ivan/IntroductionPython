
import random
def replacing_reting(reting_list):
    max_rating = max(reting_list)
    min_rating = min(reting_list)
    for i in range(len(reting_list)):
        if reting_list[i] == max_rating: reting_list[i] = min_rating
    return reting_list

numbers_of_ratings = int(input('Введите количесто оченок: '))
reting_list_orig = [random.randint(2,5) for _ in range(numbers_of_ratings)]
print(reting_list_orig)

print(replacing_reting(reting_list_orig))