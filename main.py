print("Добро пожаловать!")
contact_phone = {
    
}

def add_contact():
    name = input("Введите имя: ").strip().title()
    number =input("Введите номер: ").strip()
    
    if not name or not number:
            print("Имя и номер не могут быть пустыми")
            return
    
    clear_number = number.replace("+", "").replace("-", "").replace(" ", "")
    if not clear_number.isdigit() or not 10 <= len(clear_number) <= 15:
        print("Номер должен содержать цифры от 0 до 9 с длиной от 10 до 15 символов")
        return
    
    if name.lower() in [key.lower() for key in contact_phone.keys()]:
            print(f"Kонтакт {name} уже существует")
            return
            
    if clear_number in contact_phone.values():
            print(f"{number} уже записан")
            return

    contact_phone[name] = clear_number
    print("Контакт добавлен")
    
def show_contact():
    for name, number in contact_phone.items():
        print(f"{name} - {number}")
        
def search_contact():
    names = input("Введите имя контакта: ").title().strip()
    print("Номер: ", contact_phone.get(names, "Такого контакта не существует"))

def edit_contact():
    name = input("Введите име контакта: ").title().strip()
    new_number = input("Введите новый номер: ")
    
    if name in contact_phone and not new_number in contact_phone.values():
        contact_phone[name] = new_number
        print(f"Для контакта {name} установлен номер: {new_number}")
    else:
        print(f"Ошибка: {name} не существует или номер уже занят")

def delete_contact():
    del_contact = input("Введите имя контакта: ").title().strip()
    
    if del_contact in contact_phone: 
        contact_phone.pop(del_contact)
        print(f"Контакт {del_contact} удален")
        
    else:
        print(f"Ошибка: {del_contact} контакта не существует")


def main():
    while True:
        
        print("Меню: ")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Найти контак")
        print("4. Изменить контакт")
        print("5. Удалить контак")
        print("6. Выход")
        
        try:
            choice = int(input("Выберите действие: ")) 
        except ValueError:
            print("Ошибка: Введите число от 1 до 6")
            continue 
        
        if choice == 1:
            add_contact()
            
        elif choice == 2:
            show_contact()
                
        elif choice == 3: 
            search_contact()
        
        elif choice == 4:
            edit_contact()
            
        elif choice == 5:
            delete_contact()
            
        elif choice == 6:
            break 
        
        else:
            print("Error: the command is not defined")

main()



