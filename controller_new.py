import view_new
import text_fields_new as txt
from classes_new import Contact, Phonebook


def start():
    phonebook = Phonebook('sample.txt')
    while True:
        choice = view_new.main_menu()
        match choice:
            case 1:
                phonebook.open()
                view_new.print_message(txt.successful_open)
            case 2:
                phonebook.save()
                view_new.print_message(txt.successful_save)
            case 3:
                pb = phonebook.get()
                view_new.show_contacts(pb, txt.empty_list_or_not_open_file)
            case 4:
                new_contact = view_new.new_contact()
                phonebook.add(new_contact)
                view_new.print_message(txt.contact_saved(new_contact.name))
            case 5:
                word = view_new.enter_keyword()
                result = phonebook.find(word)
                view_new.show_contacts(result, txt.not_found(word))
            case 6:
                pb = phonebook.get()
                view_new.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    edited_contact = view_new.edit_contact(pb, txt.input_index)
                    phonebook.edit_contact(edited_contact)
                    view_new.print_message(txt.successful_edited(edited_contact[1].name))
            case 7:
                pb = phonebook.get()
                view_new.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    index = view_new.input_index(pb, txt.input_delete_index)
                    if view_new.confirm(txt.confirm_delete(pb[index - 1].name)):
                        view_new.print_message(txt.delete_contact(Phonebook.remove(index)))
            case 8:
                if phonebook.save_on_exit():
                    if view_new.confirm(txt.no_saved_book):
                        phonebook.save()
                view_new.print_message(txt.goodbye)
                exit()