def save_contact(guide_file, new_contact):
    with open(guide_file, 'a') as file:
        file.write('\n{};{};{};{}'
                    .format(new_contact[0], new_contact[1],new_contact[2],new_contact[3]))
    print(f'Добавлен контакт: {new_contact}')

    # file.write(', '.join([name, surname, telephone, description]) + \n) - вариант записи в файл