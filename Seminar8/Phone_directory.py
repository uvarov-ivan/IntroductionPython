# 1. Открывать файл (режим txt) +
# 2. Сохранить файл +
# 3. Показать все контакты +
# 4. Добавить контакт +
# 5. Найти контакт +
# 6. Изменить контакт +
# 7. Удалить контакт
# 8. Выход

# 1; Фамилия Имя Отчество; +79123456789; Комментарий

def load_pd(my_file: str) -> dict[int, tuple[str, str, str]]:
    res = {}
    with open(my_file, 'r') as directory:
        for string in directory.read().splitlines():
            list_elements = string.split(';')
            res[int(list_elements[0])] = (list_elements[1], list_elements[2], list_elements[3])
    return res


def save_pd(phone_directory: dict[int, tuple[str, str, str]]) -> None:
    with open('phone_directory.txt', 'w') as file:
        i = 1
        for (k, v) in phone_directory.items():
            file.write(f'{i};{v[0]};{v[1]};{v[2]}\n')
            i += 1


def add_contact(phone_directory: dict[int, tuple[str, str, str]]) -> None:
    surname = input('Введите фамилию нового абонента -> ')
    name = input('Введите имя нового абонента -> ')
    middle_name = input('Введите отчество нового абонента -> ')
    phone_number = input('Введите номер телефона нового абонента -> ')
    comments = input('Введите комментарий о новом абоненте -> ')
    max_id = max(phone_directory.keys())
    phone_directory[max_id + 1] = (f'{surname} {name} {middle_name}', phone_number, comments)
    save_pd(phone_directory)


def show_pd(phone_directory: dict[int, tuple[str, str, str]]) -> None:
    print('=' * 100)
    for (k, v) in phone_directory.items():
        print(f'{k:>3}) ФИО: {v[0]:<30}| Тел.: {v[1]:<15}| Комментарий: {v[2]}')
    print('=' * 100)


def contact_search(phone_directory: dict[int, tuple[str, str, str]]):
    what_look = input('Выберите критерий поиска:\n Если по ФИО, введите - 1\n Если по номеру телефона - 2\n '
                      'Если по комментарию - 3\n-> ')
    res = set()
    match what_look:
        case '1':
            found = input('Введите фамилию, имя и отчество ->')
            for (k, v) in phone_directory.items():
                if found in v[0]:
                    res.add(k)

        case '2':
            found = input('Введите номер телефона без "8" ->')
            for (k, v) in phone_directory.items():
                if found in v[1]:
                    res.add(k)

        case '3':
            found = input('Введите часть или весь комментарий ->')
            for (k, v) in phone_directory.items():
                if found in v[2]:
                    res.add(k)

        case _:
            print('Вы ввели неправильную комбинацию!')
    if len(res) > 0:
        print(f'По вашему запросу найдено:')
        for i in res:
            print(
                f'{i}) ФИО: {phone_directory[i][0]}, Тел.: {phone_directory[i][1]}, Комментарий: {phone_directory[i][2]}')
    else:
        print("Искомое значение не найдено.")
    # return res


def changing_contact(phone_directory: dict[int, tuple[str, str, str]]) -> dict[int, tuple[str, str, str]]:
    print('Для начала, найдём контакт который хотим изменить:')
    contact_search(phone_directory)
    num_contact = int(input('Введите номер контакта -> '))
    change_contact = [num_contact, phone_directory[num_contact][0], phone_directory[num_contact][1],
                      phone_directory[num_contact][2]]
    del phone_directory[num_contact]
    what_change = int(input('Выберите критерий который хотите изменить:\n Если ФИО, введите - 1\n '
                            'Если номер телефона - 2\n Если комментарий - 3\n-> '))
    match what_change:
        case 1:
            text = 'Введите новые ФИО -> '
        case 2:
            text = 'Введите новый номер телефона -> '
        case 3:
            text = 'Введите новый комментарий -> '
    change_contact[what_change] = input(text)
    phone_directory[num_contact] = (change_contact[1], change_contact[2], change_contact[3])
    return phone_directory


def delliting_contact(phone_directory: dict[int, tuple[str, str, str]]) -> dict[int, tuple[str, str, str]]:
    print('Для начала, найдём контакт который хотим удалить:')
    contact_search(phone_directory)
    num_contact = int(input('Введите номер контакта который хотите удалить -> '))
    del phone_directory[num_contact]
    print("Выбранный контакт удалён")
    return phone_directory


if __name__ == '__main__':
    while True:
        my_dict = load_pd('phone_directory.txt')
        action = input('Выберите действие:\nДобавить новый контакт - 1\nПоиск контакта - 2\n'
                       'Показать весь справочник - 3\nИзменить контакт - 4\nУдалить контакт - 5\nСохранить книгу - 6\n'
                       'Выход - 7\n-> ')
        match action:
            case '1':
                add_contact(my_dict)
            case '2':
                contact_search(my_dict)
            case '3':
                show_pd(my_dict)
            case '4':
                my_dict = changing_contact(my_dict)
            case '5':
                my_dict = delliting_contact(my_dict)
            case '6':
                save_pd(my_dict)
            case '7':
                break


