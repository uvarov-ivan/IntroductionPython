phone_book: list[dict[str, str]] = []
patch = 'phones.txt'


def open_pb():
    global phone_book
    with open(patch, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        new = {'id': contact[3], 'name': contact[0], 'phone': contact[1], 'comment': contact[2]}
        phone_book.append(new)


def save_pb():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(patch, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_pb():
    global phone_book
    return phone_book


def add_contact(new: dict[str, str]) -> str:
    global phone_book
    if len(phone_book) > 0:
        new_id = int(phone_book[-1].get('id')) + 1
        new['id'] = str(new_id)
    else:
        new['id'] = '1'
    phone_book.append(new)
    return new.get('name')


def search_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    result: list[dict[str, str]] = []
    for contact in phone_book:
        for field in contact.values():
            if word.lower() in field.lower():
                result.append(contact)
                break
    return result


def change_contact(new: dict, index: str) -> str:
    global phone_book
    for contact in phone_book:
        if index == contact.get('id'):
            contact['name'] = new.get('name', contact.get('name'))
            contact['phone'] = new.get('phone', contact.get('phone'))
            contact['comment'] = new.get('comment', contact.get('comment'))
            return contact.get('name')


def deleting_contact(index: str) -> str:
    global phone_book
    for ind in enumerate(phone_book):
        if index == phone_book[ind[0]].get('id'):
            return phone_book.pop(ind[0]).get('name')

def compare(index: str) -> str:
    global phone_book
    for contact in phone_book:
        if index == contact.get('id'):
            return contact.get('name')
