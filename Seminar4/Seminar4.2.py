# Задача №27. Решение в группах Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

str_split = input("Enter some text: ").lower().split()
str_cnt = set(str_split)
print(f"Number of words in the text is: {len(str_cnt)}")