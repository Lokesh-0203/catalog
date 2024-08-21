import datetime

# ... (Existing code for Child, Vaccination, record_vaccination, etc.)

def find_child_by_name(children, name):
    """Searches for a child in the list by name.

    Args:
        children: The list of Child objects.
        name: The name of the child to search for.

    Returns:
        The Child object if found, otherwise None.
    """
    for child in children:
        if child.name.lower() == name.lower():
            return child
    return None

def edit_child_record(child):
    """Allows editing of a child's information (except vaccination records).

    Args:
        child: The Child object to edit.
    """
    print(f"\nEditing record for {child.name}:")
    print(f"1. Edit Parent Name (current: {child.parent_name})")
    print(f"2. Edit Date of Birth (current: {child.dob.strftime('%Y-%m-%d')})")
    print("3. Back")

    choice = input("Enter your choice: ")
    if choice == '1':
        new_parent_name = input("Enter new parent name: ")
        child.parent_name = new_parent_name
        print("Parent name updated successfully!")
    elif choice == '2':
        new_dob_str = input("Enter new date of birth (YYYY-MM-DD): ")
        try:
            new_dob = datetime.datetime.strptime(new_dob_str, '%Y-%m-%d').date()
            child.dob = new_dob
            print("Date of birth updated successfully!")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    elif choice == '3':
        return
    else:
        print("Invalid choice.")

def delete_child_record(children, name):
    """Deletes a child's record from the system.

    Args:
        children: The list of Child objects.
        name: The name of the child to delete.
    """
    child = find_child_by_name(children, name)
    if child:
        confirm = input(f"Are you sure you want to delete {child.name}'s record? (y/n): ")
        if confirm.lower() == 'y':
            children.remove(child)
            print(f"{child.name}'s record deleted successfully.")
    else:
        print("Child not found.")

def view_overdue_vaccinations(children):
    """Displays a list of children with overdue vaccinations.

    Args:
        children: The list of Child objects.
    """
    overdue = False
    today = datetime.date.today()
    print("\nOverdue Vaccinations:")
    for child in children:
        for record in child.vaccination_records:
            if record['date_administered'] is None and record['vaccine'].due_date < today:
                overdue = True
                print(f"- {child.name}: {record['vaccine']}, Overdue since: {record['vaccine'].due_date.strftime('%Y-%m-%d')}")
    if not overdue:
        print("- No overdue vaccinations found.")

def main():
    children = []

    while True:
        if choice == '8':  # Add a new option for editing records
            name = input("Enter child's name: ")
            child = find_child_by_name(children, name)
            if child:
                edit_child_record(child)
            else:
                print("Child not found.")
        elif choice == '9':  # Add a new option for deleting records
            name = input("Enter child's name: ")
            delete_child_record(children, name) 

        elif choice == '10': 
            view_overdue_vaccinations(children)
if __name__ == "__main__":
    main()