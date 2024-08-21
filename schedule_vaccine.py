import datetime

class Child:
    def __init__(self, name, parent_name, dob):
        self.name = name
        self.parent_name = parent_name
        self.dob = dob
        self.vaccination_records = []

    def __str__(self):
        return f"Child: {self.name}, Parent: {self.parent_name}, DOB: {self.dob}"

class Vaccination:
    def __init__(self, vaccine_name, due_date):
        self.vaccine_name = vaccine_name
        self.due_date = due_date

    def __str__(self):
        return f"Vaccine: {self.vaccine_name}, Due: {self.due_date.strftime('%Y-%m-%d')}"

def record_vaccination(child, vaccine):
    today = datetime.date.today()
    record = {"vaccine": vaccine, "date_administered": today}
    child.vaccination_records.append(record)
    print(f"\n{vaccine} administered to {child.name} on {today.strftime('%Y-%m-%d')}")

def view_child_records(child):
    print(f"\nVaccination Records for {child.name}:")
    if child.vaccination_records:
        for record in child.vaccination_records:
            print(f"- {record['vaccine']}, Administered: {record['date_administered'].strftime('%Y-%m-%d')}")
    else:
        print("- No vaccination records found.")

def schedule_vaccination(child, vaccine_name, due_date_str):
    due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
    vaccine = Vaccination(vaccine_name, due_date)
    child.vaccination_records.append({"vaccine": vaccine, "date_administered": None})
    print(f"\n{vaccine} scheduled for {child.name} on {due_date.strftime('%Y-%m-%d')}")

def view_upcoming_appointments(children):
    print("\nUpcoming Vaccination Appointments:")
    upcoming = False
    for child in children:
        for record in child.vaccination_records:
            if record['date_administered'] is None:
                upcoming = True
                print(f"- {child.name}: {record['vaccine']}, Scheduled: {record['vaccine'].due_date.strftime('%Y-%m-%d')}")
    if not upcoming:
        print("- No upcoming appointments found.")

def view_all_children(children):
    print("\nRegistered Children:")
    if children:
        for child in children:
            print(child)
    else:
        print("- No children registered yet.")

def main():
    children = []

    while True:
        print("\nVaccination Management System")
        print("1. Register Child")
        print("2. Schedule Vaccination")
        print("3. Record Vaccination")
        print("4. View Child's Records")
        print("5. View Upcoming Appointments")
        print("6. View All Children")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter child's name: ")
            parent_name = input("Enter parent's name: ")
            dob_str = input("Enter date of birth (YYYY-MM-DD): ")
            dob = datetime.datetime.strptime(dob_str, '%Y-%m-%d').date()
            child = Child(name, parent_name, dob)
            children.append(child)
            print(f"{child.name} registered successfully!")

        elif choice == '2':
            name = input("Enter child's name: ")
            child = next((c for c in children if c.name == name), None)
            if child:
                vaccine_name = input("Enter vaccine name: ")
                due_date_str = input("Enter due date (YYYY-MM-DD): ")
                schedule_vaccination(child, vaccine_name, due_date_str)
            else:
                print("Child not found.")

        elif choice == '3':
            name = input("Enter child's name: ")
            child = next((c for c in children if c.name == name), None)
            if child:
                vaccine_name = input("Enter vaccine name: ")
                vaccine = next((r['vaccine'] for r in child.vaccination_records if r['vaccine'].vaccine_name == vaccine_name), None)
                if vaccine:
                    record_vaccination(child, vaccine)
                else:
                    print("Vaccine not found in child's records.")
            else:
                print("Child not found.")

        elif choice == '4':
            name = input("Enter child's name: ")
            child = next((c for c in children if c.name == name), None)
            if child:
                view_child_records(child)
            else:
                print("Child not found.")

        elif choice == '5':
            view_upcoming_appointments(children)

        elif choice == '6':
            view_all_children(children)

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()