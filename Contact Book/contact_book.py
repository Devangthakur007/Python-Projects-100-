import sys

def display_contact(name: str, info: dict):
    """Prints formatted contact details."""
    print(f"\nName: {name.title()}")
    print(f"Phone: {info['phone']}")
    print(f"Email: {info['email']}")
    print(f"Address: {info['address']}")


def get_non_empty_input(prompt: str) -> str:
    """Helper to ensure the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value.lower() == 'exit':
            print("Goodbye!")
            sys.exit()
        if value:
            return value
        print("Field cannot be empty! Please try again.")


def contact_book_app():
    # Dictionary structure: {"name_lowercase": {"phone": "...", "email": "...", "address": "..."}}
    contacts = {}

    print("=== Python CLI Contact Book ===")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        print("\nMain Menu:")
        print("1. View All Contacts")
        print("2. Add New Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip().lower()

        if choice in ['6', 'exit']:
            print("Goodbye!")
            sys.exit()

        # 1. View All Contacts
        elif choice == '1':
            if not contacts:
                print("\nYour contact book is empty.")
            else:
                print(f"\n--- Contact List ({len(contacts)}) ---")
                for key, info in sorted(contacts.items()):
                    display_contact(key, info)
                print("-" * 35)

        # 2. Add New Contact
        elif choice == '2':
            name = get_non_empty_input("Enter contact name: ")
            key = name.lower()

            if key in contacts:
                print(f"A contact with the name '{name}' already exists!")
                continue

            phone = get_non_empty_input("Enter phone number: ")
            email = input("Enter email address (optional): ").strip() or "N/A"
            address = input("Enter home address (optional): ").strip() or "N/A"

            contacts[key] = {
                "display_name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            print(f"Contact '{name}' added successfully!")

        # 3. Search Contact
        elif choice == '3':
            if not contacts:
                print("\nYour contact book is empty.")
                continue

            search_query = input("Enter name to search: ").strip().lower()
            matches = [k for k in contacts if search_query in k]

            if not matches:
                print("No matching contacts found.")
            else:
                print(f"\nFound {len(matches)} matching contact(s):")
                for k in matches:
                    display_contact(contacts[k]["display_name"], contacts[k])

        # 4. Update Contact
        elif choice == '4':
            if not contacts:
                print("\nYour contact book is empty.")
                continue

            name = input("Enter the name of the contact to update: ").strip().lower()
            if name not in contacts:
                print("Contact not found.")
                continue

            print(f"\nUpdating '{contacts[name]['display_name']}'. Press Enter to keep existing details.")
            
            new_phone = input(f"New phone [{contacts[name]['phone']}]: ").strip()
            new_email = input(f"New email [{contacts[name]['email']}]: ").strip()
            new_address = input(f"New address [{contacts[name]['address']}]: ").strip()

            if new_phone:
                contacts[name]["phone"] = new_phone
            if new_email:
                contacts[name]["email"] = new_email
            if new_address:
                contacts[name]["address"] = new_address

            print("Contact updated successfully!")

        # 5. Delete Contact
        elif choice == '5':
            if not contacts:
                print("\nYour contact book is empty.")
                continue

            name = input("Enter the name of the contact to delete: ").strip().lower()
            if name in contacts:
                deleted = contacts.pop(name)
                print(f"Deleted contact: '{deleted['display_name']}'")
            else:
                print("Contact not found.")

        else:
            print("Invalid option! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    contact_book_app()