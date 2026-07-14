import streamlit as st
import pandas as pd
import os

def load_projects():
   if os.path.exists("projects.csv"):
        df=pd.read_csv("projects.csv")
        print("Projects loaded successfully.")
        projects = df.to_dict(orient="records")
   else:
        print("The file does not exist")  
        projects = []
   return projects

def save_projects():
    if projects:
        df = pd.DataFrame(projects)
        df.to_csv("projects.csv", index=False)
        print("Projects saved successfully.")
    else:
        print("No projects to save.")
            
projects = load_projects()

st.title("📊 Project Budget Manager")

with st.form("project_form"):

    st.subheader("Add New Project")

    project_name = st.text_input("Project Name")

    # Approved costs

    approved_personnel_costs = st.number_input(
        "Approved Personnel Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

    approved_travel_costs = st.number_input(
        "Approved Travel Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )
    approved_equipment_costs = st.number_input(
        "Approved Equipment Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )
    approved_supplies_costs = st.number_input(
        "Approved Supplies Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )
    approved_subcontracting_costs = st.number_input(
        "Approved Subcontracting Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )
    approved_other_costs = st.number_input(
        "Approved Other Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

    # Actual costs
    actual_personnel_costs = st.number_input(
        "Actual Personnel Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )    
    actual_travel_costs = st.number_input(
        "Actual Travel Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )
    actual_equipment_costs = st.number_input(
        "Actual Equipment Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )
    actual_supplies_costs = st.number_input(
        "Actual Supplies Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )
    actual_subcontracting_costs = st.number_input(
        "Actual Subcontracting Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )
    actual_other_costs = st.number_input(
        "Actual Other Costs",
        min_value=0.0,
        value=0.0,
        step=100.0
    )
    
    submit = st.form_submit_button("Add Project")

if submit:
    if not project_name:
        st.error("Please enter the project name.")
    else:
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
        save_projects()
        st.success(f"Project '{project_name}' added successfully!")
st.subheader("All Projects")

df = pd.DataFrame(projects)

st.dataframe(df)