import csv
import os

FILE_NAME = "contacts.csv"
contacts = {}

def load_contacts():
    """Load contacts from the CSV file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    name, phone, email = row
                    contacts[name] = {"phone": phone, "email": email}

def save_contacts():
    """Save contacts to the CSV file."""
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        for name, data in contacts.items():
            writer.writerow([name, data["phone"], data["email"]])
    print("\nContacts saved successfully.")

def display_contacts():
    """Display all contacts."""
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\nContact List:")
    print("{:<20} {:<15} {:<30}".format("Name", "Phone", "Email"))
    print("-" * 65)
    for name, data in contacts.items():
        print("{:<20} {:<15} {:<30}".format(name, data["phone"], data["email"]))
    print("-" * 65)

def add_contact():
    """Add a new contact."""
    name = input("\nEnter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()

    if not name or not phone or not email:
        print("All fields are required!")
        return

    if name in contacts:
        print("A contact with this name already exists!")
        return

    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")

def edit_contact():
    """Edit an existing contact."""
    name = input("\nEnter the name of the contact to edit: ").strip()

    if name not in contacts:
        print("No contact found with that name.")
        return

    print(f"Editing Contact: {name}")
    print(f"Current Phone: {contacts[name]['phone']}")
    print(f"Current Email: {contacts[name]['email']}")

    phone = input("Enter new Phone (leave blank to keep current): ").strip()
    email = input("Enter new Email (leave blank to keep current): ").strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email

    print("Contact updated successfully.")

def delete_contact():
    """Delete a contact."""
    name = input("\nEnter the name of the contact to delete: ").strip()

    if name not in contacts:
        print("No contact found with that name.")
        return

    del contacts[name]
    print("Contact deleted successfully.")

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\nContact Management System")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            display_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            save_contacts()
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main script execution
if __name__ == "__main__":
    load_contacts()
    main_menu()
    save_contacts()  # Ensure contacts are saved before exiting
