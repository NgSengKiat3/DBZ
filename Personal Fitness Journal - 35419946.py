import csv

data_file = "fitness_journal.csv"



#activity list
activities = []

# Main Page
def main():
    load_data()
    while True:
        print("\nPersonal Fitness Journal")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")
        print("4. Details")
        print("5. Search")
        print("6. Exit")
        
        # Carry out different functions based on the input
        choice = input("Enter your choice: ")

        if choice == '1':
            add()
        elif choice == '2':
            edit()
        elif choice == '3':
            delete()
        elif choice == '4':
            details()
        elif choice == '5':
            search()
        elif choice == '6':
            save_data()
            print("Exiting the program. Your data has been saved.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")
     
     
# Load data from the CSV file
def load_data():
    global activities
    try:
        with open(data_file, mode='r') as file:
            reader = csv.DictReader(file)
            activities = list(reader)
    except FileNotFoundError:
        print(f"{data_file} not found. Starting with an empty journal.")

# Save data to the CSV file
def save_data():
    global activities
    with open(data_file, mode='w', newline='') as file:
        fieldnames = ["Activity", "Type", "Duration", "Distance", "Calorie", "Date", "Notes"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(activities)

#add activity
def add():
 activity = input("Enter the name of the activity: ")
 Type = input("Enter the type of activity ")
 duration = float(input("Enter the duration of the activity: "))
 distance = float(input("Enter the distance: "))
 calorie = float(input("Enter the calorie burned during the activity: "))
 date = input("Enter the date: ")
 notes = input("Enter any additional note: ")

 activities.append(activity)
 print("New activity added")
    
        
#edit infomation in chosen activity
def edit():
    for activity in activities:
        new_data = input("Please enter the name of the activity:")
        new_type = input("Please enter the type of the activity:")
        new_duration = float(input("Please enter the duration:"))
        new_distance = float(input("Enter the distance: "))
        new_calorie = float(input("Enter the distance: "))
        new_date = input("Please enter the date")
        new_notes = input("Please enter any additional notes(if there's any):")
    
# Delete an activity
def delete():
    list_activities()
    index = int(input("Enter the number of the activity to delete: ")) - 1
    if 0 <= index < len(activities):
        removed = activities.pop(index)
        print(f"Activity '{removed['Activity']}' has been deleted.")
    else:
        print("Invalid activity number.")


# Outline the details of all activities
def details():
    if not activities:
        print("No activities to display.")
        return
    print("\nActivity Details:")
    for activity in activities:
        print(f"""
        Activity: {activity['Activity']}
        Type: {activity['Type']}
        Duration: {activity['Duration']} minutes
        Distance: {activity['Distance']} km
        Calorie: {activity['Calorie']}
        Date: {activity['Date']}
        Notes: {activity['Notes']}
        """)
    print("End of details.")

# Search the activities based on the input
def search():
    search_term = input("Enter a keyword to search (e.g., activity name, type, or date): ").lower()
    results = [activity for activity in activities if search_term in activity['Activity'].lower() or
               search_term in activity['Type'].lower() or search_term in activity['Date']]
    if results:
        print("\nSearch Results:")
        for activity in results:
            print(f"""
            Activity: {activity['Activity']}
            Type: {activity['Type']}
            Duration: {activity['Duration']} minutes
            Distance: {activity['Distance']} km
            Calorie: {activity['Calorie']}
            Date: {activity['Date']}
            Notes: {activity['Notes']}
            """)
    else:
        print("No matching activities found.")


#run program 
if __name__ == "__main__":
     main()
