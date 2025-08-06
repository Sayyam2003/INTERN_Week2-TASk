#Phonebook App:
import json
import os

PHONEBOOK_FILE = 'phonebook.json'

# Load contacts from JSON file
def load_contacts():
    if os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save contacts to JSON file
def save_contacts(contacts):
    with open(PHONEBOOK_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# CREATE
def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added.")

# READ
def view_contacts(contacts):
    if not contacts:
        print("Phonebook is empty.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# UPDATE
def update_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print(f"Contact '{name}' updated.")
    else:
        print("Contact not found.")

# DELETE
def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

# Main loop
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(contacts, name, phone)

        elif choice == '2':
            view_contacts(contacts)

        elif choice == '3':
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            update_contact(contacts, name, new_phone)

        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)

        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()

