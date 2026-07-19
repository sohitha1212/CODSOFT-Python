# Contact Book in Python

contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")

def search_contact(name):
    if name in contacts:
        print(f"\nName: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print("Contact not found.")

def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]["Phone"] = phone
        if email:
            contacts[name]["Email"] = email
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

# Menu-driven program
while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "4":
        name = input("Enter name to update: ")
        phone = input("Enter new phone (leave blank to skip): ")
        email = input("Enter new email (leave blank to skip): ")
        update_contact(name, phone if phone else None, email if email else None)
    elif choice == "5":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
