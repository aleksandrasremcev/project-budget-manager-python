#adding pandas library
import pandas as pd
import os
print("Project budget App")

# Check weather the CSV file exists and read it 
def load_projects():
   if os.path.exists("projects.csv"):
        df=pd.read_csv("projects.csv")
        print("Projects loaded successfully.")
        projects = df.to_dict(orient="records")
   else:
        print("The file does not exist")  
        projects = []
   return projects
  
projects = load_projects()

 #Adding menu 
def add_project():
        print("\nAdd project selected")

        # Project information
        project_name = input("What is the project name?")

        # Approved budget
        approved_personnel_costs = float(input("Please insert approved personnel costs: "))
        approved_travel_costs = float(input("Please insert approved travel costs: "))
        approved_equipment_costs = float(input("Please insert approved equipment costs: "))
        approved_supplies_costs = float(input("Please insert approved supplies costs: "))
        approved_subcontracting_costs = float(input("Please insert approved subcontracting costs: "))
        approved_other_costs = float(input("Please insert approved other costs: "))

        # Actual costs
        actual_personnel_costs = float(input("Please insert actual personnel costs: "))
        actual_travel_costs = float(input("Please insert actual travel costs: "))
        actual_equipment_costs = float(input("Please insert actual equipment costs: "))
        actual_supplies_costs = float(input("Please insert actual supplies costs: "))
        actual_subcontracting_costs = float(input("Please insert actual subcontracting costs: "))
        actual_other_costs = float(input("Please insert actual other costs: "))

        # Dictionary
        project = {
            "project_name": project_name,
            "approved_personnel_costs": approved_personnel_costs,
            "approved_travel_costs": approved_travel_costs,
            "approved_equipment_costs": approved_equipment_costs,
            "approved_supplies_costs": approved_supplies_costs,
            "approved_subcontracting_costs": approved_subcontracting_costs,
            "approved_other_costs": approved_other_costs,
            "actual_personnel_costs": actual_personnel_costs,
            "actual_travel_costs": actual_travel_costs,
            "actual_equipment_costs": actual_equipment_costs,
            "actual_supplies_costs": actual_supplies_costs,
            "actual_subcontracting_costs": actual_subcontracting_costs,
            "actual_other_costs": actual_other_costs
        }

        projects.append(project)
        print(f"\nProject '{project_name}' added successfully!")
        # process part - This is where Python made calculation

        total_approved_budget = approved_personnel_costs + approved_travel_costs + approved_equipment_costs + approved_supplies_costs + approved_subcontracting_costs + approved_other_costs
        total_actual_costs = actual_personnel_costs + actual_travel_costs + actual_equipment_costs +actual_supplies_costs + actual_subcontracting_costs + actual_other_costs
        remaining_costs = total_approved_budget - total_actual_costs
        exceeded_budget = total_actual_costs > total_approved_budget
        # Output for each project

        # output -  This is what user should see 

        print("Project Name", project_name)
        print("Approved Personnel Costs", approved_personnel_costs)
        print("Approved Travel Costs", approved_travel_costs)
        print("Approved Equipment cost" , approved_equipment_costs)
        print("Approved Supplies Costs" , approved_supplies_costs)
        print("Approved Subcontracting Costs", approved_subcontracting_costs)
        print("Approved Other Costs" , approved_other_costs)

        print("Actual personnel costs" , actual_personnel_costs)
        print("Actual travel costs" , actual_travel_costs)
        print("Actual travel costs" , actual_travel_costs)
        print("Actual equipment costs", actual_equipment_costs)
        print("Actual supplies costs" , actual_supplies_costs)
        print("Actual subcontracting costs" , actual_subcontracting_costs)
        print("Actual other costs" , actual_other_costs)

        print("Total approved budget" , total_approved_budget)
        print("Total actual costs" , total_actual_costs)
        print("Remaining costs" , remaining_costs)
        print("Exceeded budget" , exceeded_budget)
        print("\nPROJECT BUDGET REPORT")
        print("Project Name:", project_name)
        print("Total Approved Budget:", total_approved_budget)
        print("Total Actual Costs:", total_actual_costs)
        print("Remaining Costs:", remaining_costs)
        if exceeded_budget:
           print("The costs exceeded the approved budget")
        else:
            print("The costs are within approved budget")

def view_projects():
    print("\nALL PROJECTS")

    if projects:
        for project in projects:
            print(project)
    else:
        print("No projects available.")
def search_project():
    print("\nSearch project selected")
    found = False

    search_name = input("Please insert the project name: ")

    for project in projects:
        if project["project_name"] == search_name:
            found = True
            print("\nProject found:")
            print(project)

    if found == False:
        print("The project was not found.")
def update_project():
    print("\nUpdate project selected")

    found = False
    update_project = input("Which project do you want to update? ")

    for project in projects:
        if project["project_name"] == update_project:
            found = True

            available_fields = [
                "project_name",
                "approved_personnel_costs",
                "approved_travel_costs",
                "approved_equipment_costs",
                "approved_supplies_costs",
                "approved_subcontracting_costs",
                "approved_other_costs",
                "actual_personnel_costs",
                "actual_travel_costs",
                "actual_equipment_costs",
                "actual_supplies_costs",
                "actual_subcontracting_costs",
                "actual_other_costs"
            ]

            print("\nYou can update the following fields:")

            for field in available_fields:
                print(field)

            change = input("\nWhich field do you want to update? ")
            if change not in available_fields:
               print("Invalid field.")
               break

            if change == "project_name":
                new_value = input("Please enter the new value: ")
            else:
                new_value = float(input("Please enter the new value: "))

            project[change] = new_value
            print("Project updated successfully.")
            break

    if not found:
        print("The project was not found.")          
def save_projects():
    if projects:
        df = pd.DataFrame(projects)
        df.to_csv("projects.csv", index=False)
        print("Projects saved successfully.")
    else:
        print("No projects to save.")

def delete_project():
    print("\nDelete project selected")

    found = False

    delete_project = input("Which project do you want to delete? ")

    for project in projects:
        if project["project_name"] == delete_project:
            found = True

            projects.remove(project)

            print("Project deleted successfully.")
            break

    if not found:
        print("Project not found.")


while True:
    print("\n===== PROJECT BUDGET APP MENU =====")
    print("1. Add project")
    print("2. View projects")
    print("3. Search project")
    print("4. Update project")
    print("5. Delete project")
    print("6. Save and Exit")
   
    choice = input("Choose an option: ")

    if choice == "1":
        add_project()
            
    elif choice == "2":
        view_projects()
    
    elif choice == "3":
        search_project()

    elif choice == "4":
        update_project()

    elif choice == "5":
        delete_project ()   

    elif choice == "6":
        save_projects()
        print("\nExiting Project Budget App...")
        break

    else:
        print("\nInvalid option. Please choose a number between 1 and 6.")
     
 
     


   