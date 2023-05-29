main_menu = '''\nГлавное меню:
    1. Открыть телефонную книгу
    2. Сохранить телефонную книгу
    3. Показать контакты
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход\n'''

input_choice = 'Выберите пункт меню\n-> '

pb_is_open = 'Телефонная книга уже открыта!'

load_seccessful = 'Телефонная книга успешно открыта!'

save_successful = 'Телефонная книга успешно сохранена!'

pb_empty = 'Телефонная книга пуста или не загружена!'

input_new_contact = 'Введите данные нового контакта: '

new_contact = {'name': 'Введите имя: ', 'phone': 'Введите номер телефона: ', 'comment': 'Введите комментарий: '}


def new_contact_seccessful(name: str):
    return f'Контакт -= {name} =- успешно добавлен!'


input_search = 'Что будем искать\n-> '

input_delete = 'Какой контакт хотите удалить?\n-> '


def empty_search(word: str) -> str:
    return f' Контакт содержащий "{word}" не найден!'


input_change = 'Какой контакт будем менять\n-> '

input_index = 'Введите индекс контакта\n-> '

change_contact = 'Введите новые данные или оставьте поле пустым чтобы оставить без изменений: '

def are_you_sure_del(name: str) -> str:
    return f'Вы уверены, что хотите удалить контакт "{name}" ?\n y/n -> '

def cancel_deletion(name:str) -> str:
    return f'Удаление контакта "{name}" отменено!'


def cancel_change(name:str) -> str:
    return f'Изменение контакта "{name}" отменено!'

def are_you_sure_change(name: str) -> str:
    return f'Вы уверены, что хотите изменить контакт "{name}" ?\n y/n -> '

def change_seccessful(name: str) -> str:
    return f'Контакт "{name}" успешно изменён!'


def delete_seccessful(name: str) -> str:
    return f'Контакт "{name}" успешно удалён!'

error_input = 'Вы ввели неверные данные!'