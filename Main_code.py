# Simple Gym Management System

members = {}


def add_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    age = input("Enter Age: ")
    plan = input("Enter Membership Plan: ")

    members[member_id] = {
        "Name": name,
        "Age": age,
        "Plan": plan
    }

    print("Member added successfully!\n")



def view_members():
    if not members:
        print("No members found.\n")
        return

    print("\nGym Members List:")
    for member_id, details in members.items():
        print(f"""
Member ID: {member_id}
Name: {details['Name']}
Age: {details['Age']}
Plan: {details['Plan']}
------------------------
""")



def remove_member():
    member_id = input("Enter Member ID to remove: ")

    if member_id in members:
        del members[member_id]
        print("Member removed successfully!\n")
    else:
        print("Member not found.\n")


while True:
    print("===== Gym Management System =====")
    print("1. Add Member")
    print("2. View Members")
    print("3. Remove Member")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_member()
    elif choice == "2":
        view_members()
    elif choice == "3":
        remove_member()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
