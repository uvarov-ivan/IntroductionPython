import text
import view
import model


def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                if model.phone_book:
                    view.print_message(text.pb_is_open)
                else:
                    model.open_pb()
                    view.print_message(text.load_seccessful)
            case 2:
                model.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb = model.get_pb()
                view.print_all_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_seccessful(name))
            case 5:
                key_word = view.input_search(text.input_search)
                result = model.search_contact(key_word)
                view.print_all_contacts(result,text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_search)
                result = model.search_contact(key_word)
                if result:
                    if len(result) != 1:
                        view.print_all_contacts(result, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    action = view.input_search(text.are_you_sure_change(model.action(current_id)))
                    if action == 'y':
                        new_contact = view.input_contact(text.change_contact)
                        name = model.change_contact(new_contact, current_id)
                        view.print_message(text.change_seccessful(name))
                    elif action == 'n':
                        view.print_message(text.cancel_change(model.action(current_id)))
                    else:
                        view.print_message(text.error_input)
                else:
                    view.print_message(text.empty_search(key_word))
            case 7:
                key_word = view.input_search(text.input_delete)
                result = model.search_contact(key_word)
                if result:
                    if len(result) != 1:
                        view.print_all_contacts(result, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    action = view.input_search(text.are_you_sure_del(model.action(current_id)))
                    if action == 'y':
                        name = model.deleting_contact(current_id)
                        view.print_message(text.delete_seccessful(name))
                    elif action == 'n':
                        view.print_message(text.cancel_deletion(model.action(current_id)))
                    else:
                        view.print_message(text.error_input)
                else:
                    view.print_message(text.empty_search(key_word))
            case 8:
                break
            case 9:
                pass