contacts = {}

def add_contact():
    name = int(input("Enter name: "))
    phone = int(input("Enter phone number: "))
    contacts[name] = phone
    print("Contact added!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(name, ":", contacts[name])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        contacts[name] = input("Enter new phone number: ")
        print("Contact updated!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact not found.")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
    else:
        for name, phone in contacts.items():
            print(name, ":", phone)

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        view_contacts()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
