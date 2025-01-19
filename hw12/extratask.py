# написати скрипт для видалення всіх файлів вказаної директорії
import os

# folder = "extratask"
#
# def delete_files_in_dir(dir_name):
#     if os.path.exists(dir_name):
#         files = os.listdir(dir_name)
#         for file in files:
#             os.remove(dir_name + "/" + file)
#
# delete_files_in_dir(folder)


# создать телефонную книгу с сохранением в файл txt
# добавление
# изменение контакта
# удаление
# поиск по имени

phonebook = "phonebook.txt"

def get_lines_in_file():
    with open(phonebook, "r", encoding='utf-8') as file:
        lines = file.readlines()
        return lines

def add_phone(name, phone):
    if len(name.strip()) and len(phone.strip()):
        with open(phonebook, "a", encoding='utf-8') as result:
            result.write(f"{name}: {phone}\n")
        print("Контакт добавлен")

add_phone("Ivan Ivanov", "12345678")
add_phone("Petr Petrov", "85296328")
add_phone("Maria Zakharova", "852741256")

def edit_phone(name, phone):
    if len(name.strip()) and len(phone.strip()):
        lines = get_lines_in_file()
        updated = False

        with open(phonebook, "w", encoding='utf-8') as file:
            for line in lines:
                if line.startswith(name):
                    file.write(f"{name}: {phone}\n")
                    updated = True
                else:
                    file.write(line)

            if updated:
                print("Контакт обновлен")
            else:
                print("Контакт не найден")

edit_phone("Petr Petrov", "55555555")

def delete_phone(name):
    if len(name.strip()):
        lines = get_lines_in_file()

        with open(phonebook, "w", encoding='utf-8') as file:
            for line in lines:
                if not line.startswith(name):
                    file.write(line)
                else:
                    print("Контакт удалён")

delete_phone("Ivan Ivanov")

def find_phone(name):
    if len(name.strip()):
        lines = get_lines_in_file()
        contact = ""

        for line in lines:
            if line.startswith(name):
                contact = line
        if len(contact):
            print(contact)
        else:
            print("Контакт не найден")

find_phone("Maria Zakharova")
find_phone("dsf")