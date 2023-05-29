import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choise = input(text.input_choice)
        if choise.isdigit() and 0 < int(choise) < 9:
            return int(choise)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_all_contacts(book: list[dict[str, str]], error: str):
    if book:
        print('\n' + '=' * 71)
        for contact in book:
            print(
                f'{contact.get("id"):>3}) {contact.get("name"):<20} | {contact.get("phone"):<20} | {contact.get("comment"):<20}')
        print('=' * 71 + '\n')
    else:
        print(error)


def input_contact(message) -> dict[str, str]:
    new = {}
    print(message)
    for key, txt in text.new_contact.items():
        value = input(txt)
        if value:
            new[key] = value
    return new


def input_search(message) -> str:
    return input(message)
