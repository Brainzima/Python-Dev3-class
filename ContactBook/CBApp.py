import json
file_name = 'contacts_book.json'
def load_contacts():
    try:
        with open(file_name,'r') as cf:
            all_contacts = json.load(cf)
    except FileNotFoundError:
        all_contacts = {}
    return all_contacts


def view_all(contacts):
    for name, info in contacts.items():
        print(f"Name: {name} , Mobile: {info['mobile']}")


def hamara_func():
    contacts = load_contacts()
    while True:
        print("----------------Contact Book Choice List------------")
        print("1. View All Contacts")
        print("2. Add New Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("----------------Choose desired option------------")
        choise = int(input("Enter the Choise Number: "))

        if choise == 1:
            print('------------view all contacts---------')
            view_all(contacts)
            print('--------------------------------------')
        elif choise == 2:
            print('add')
            add_contact()
        elif choise == 3:
            print('search')
            search_contact()
        elif choise == 4:
            print('delete')
            delete_contact()
        elif choise == 5:
            print('---------------Bye Bye-----------------')
            break
        else:
            print('Invalid Input')

if __name__ == '__main__':
    hamara_func()

