import json
file_name = 'contacts_book.json'
def load_contacts():
    try:
        with open(file_name,'r') as cf:
            all_contacts = json.load(cf)
    except FileNotFoundError:
        all_contacts = {}
    return all_contacts

def save_contact(contacts):
    with open(file_name, 'w') as cf:
        json.dump(contacts, cf, indent=4)

def add_contact(contacts):
    name = input("Enter Name: ")
    mobile = input("Enter Mobile number: ")
    email = input("Enter email (optional): ")
    address = input("Enter address (optional): ")
    contacts[name] = {
        "mobile": mobile,
        "email": email,
        "address": address
    }
    print(f"Contact {name} successfully added!")

def search_contact(contacts):
    user_input = input("Enter the contact name: ").lower()
    found = False
    for name, info in contacts.items():
        if user_input in name.lower():
            print(f"-------{name}-----")
            print(f"Mobile: {info['mobile']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("--------------------")
            found = True
    if not found:
        print(f"No Contact Found with {user_input}")


def delete_contact(contacts):
    delete_name = input("Enter Contact Name to Delete:")
    if delete_name in contacts:
        del contacts[delete_name]
        save_contact(contacts)
        print(f"Contact {delete_name} successfully deleted!")
    else:
        print(f"No contact found with {delete_name}")


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
            print('------------Add New contacts---------')
            add_contact(contacts)
            save_contact(contacts)
            print('--------------------------------------')
        elif choise == 3:
            print('search')
            search_contact(contacts)
        elif choise == 4:
            print('delete')
            delete_contact(contacts)
        elif choise == 5:
            print('---------------Bye Bye-----------------')
            break
        else:
            print('Invalid Input')

if __name__ == '__main__':
    hamara_func()

