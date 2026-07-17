import os
from io import BytesIO

import pandas as pd
import streamlit as st


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Project Budget Manager",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# DATA FUNCTIONS
# ==========================================

def load_projects():
    if os.path.exists("projects.csv"):
        df = pd.read_csv("projects.csv")
        return df.to_dict(orient="records")

    return []


def save_projects():
    df = pd.DataFrame(projects)
    df.to_csv("projects.csv", index=False)


# ==========================================
# LOAD PROJECT DATA
# ==========================================

projects = load_projects()
df = pd.DataFrame(projects)


# ==========================================
# COLUMN DEFINITIONS
# ==========================================

approved_columns = [
    "approved_personnel_costs",
    "approved_travel_costs",
    "approved_equipment_costs",
    "approved_supplies_costs",
    "approved_subcontracting_costs",
    "approved_other_costs"
]

actual_columns = [
    "actual_personnel_costs",
    "actual_travel_costs",
    "actual_equipment_costs",
    "actual_supplies_costs",
    "actual_subcontracting_costs",
    "actual_other_costs"
]

available_fields = [
    "project_name",
    *approved_columns,
    *actual_columns
]

field_labels = {
    "project_name": "Project Name",
    "approved_personnel_costs": "Approved Personnel Costs",
    "approved_travel_costs": "Approved Travel Costs",
    "approved_equipment_costs": "Approved Equipment Costs",
    "approved_supplies_costs": "Approved Supplies Costs",
    "approved_subcontracting_costs": "Approved Subcontracting Costs",
    "approved_other_costs": "Approved Other Costs",
    "actual_personnel_costs": "Actual Personnel Costs",
    "actual_travel_costs": "Actual Travel Costs",
    "actual_equipment_costs": "Actual Equipment Costs",
    "actual_supplies_costs": "Actual Supplies Costs",
    "actual_subcontracting_costs": "Actual Subcontracting Costs",
    "actual_other_costs": "Actual Other Costs"
}


column_names = {
    "project_name": "Project Name",
    "approved_personnel_costs": "Approved Personnel",
    "approved_travel_costs": "Approved Travel",
    "approved_equipment_costs": "Approved Equipment",
    "approved_supplies_costs": "Approved Supplies",
    "approved_subcontracting_costs": "Approved Subcontracting",
    "approved_other_costs": "Approved Other",
    "actual_personnel_costs": "Actual Personnel",
    "actual_travel_costs": "Actual Travel",
    "actual_equipment_costs": "Actual Equipment",
    "actual_supplies_costs": "Actual Supplies",
    "actual_subcontracting_costs": "Actual Subcontracting",
    "actual_other_costs": "Actual Other"
}

# ==========================================
# APPLICATION TITLE
# ==========================================

st.title("📊 Project Budget Manager")

if "success_message" in st.session_state:
    st.success(st.session_state.success_message)
    del st.session_state.success_message

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "📊 Dashboard",
        "➕ Add Project",
        "🔍 Search",
        "✏️ Update",
        "🗑 Delete",
        "📥 Data Export"
    ]
)


# ==========================================
# TAB 1: DASHBOARD
# ==========================================

with tab1:
    st.header("Dashboard")

    if not df.empty:
        total_projects = len(df)

        total_approved_budget = (
            df[approved_columns]
            .sum()
            .sum()
        )

        total_actual_costs = (
            df[actual_columns]
            .sum()
            .sum()
        )

        total_remaining_budget = (
            total_approved_budget - total_actual_costs
        )


        col1, col2, col3, col4 = st.columns(4)
        
        col1.metric(
            "📁 Total Projects",
            total_projects
        )

        col2.metric(
            "💰 Approved Budget",
            f"{total_approved_budget:,.2f}"
        )

        col3.metric(
            "💸 Actual Costs",
            f"{total_actual_costs:,.2f}"
        )

        col4.metric(
            "✅ Remaining Budget",
            f"{total_remaining_budget:,.2f}"
        )

        # GRAPH GOES HERE

        # Calculate total approved and actual costs for each project
        chart_df = df.copy()

        chart_df["Approved Budget"] = chart_df[approved_columns].sum(axis=1)
        chart_df["Actual Costs"] = chart_df[actual_columns].sum(axis=1)

        # Keep only the columns needed for the chart
        chart_df = chart_df[
            [
                "project_name",
                "Approved Budget",
                "Actual Costs"
            ]
        ]

        # Rename the project column for display
        chart_df = chart_df.rename(
            columns={
                "project_name": "Project"
            }
        )

        # Set project names as the chart labels
        chart_df = chart_df.set_index("Project")

        st.subheader("Approved Budget vs Actual Costs")

        st.bar_chart(
            chart_df,
            width="stretch"
        )

        st.subheader("All Projects")
        display_df = df.rename(columns=column_names)
        st.dataframe(
            display_df,
            width="stretch",
            hide_index=True
        )
      
    else:
        st.info("No project data available for the dashboard.")


# ==========================================
# TAB 2: ADD PROJECT
# ==========================================

with tab2:
    st.header("Add New Project")

    with st.form("project_form"):

        project_name = st.text_input("Project Name")

        st.subheader("Approved Costs")

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

        st.subheader("Actual Costs")

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
        clean_project_name = project_name.strip()

        if not clean_project_name:
            st.error("Please enter the project name.")

        else:
            existing_names = [
                project["project_name"].strip().lower()
                for project in projects
            ]

            if clean_project_name.lower() in existing_names:
                st.error(
                    "A project with this name already exists."
                )

            else:
                project = {
                    "project_name": clean_project_name,
                    "approved_personnel_costs":
                        approved_personnel_costs,
                    "approved_travel_costs":
                        approved_travel_costs,
                    "approved_equipment_costs":
                        approved_equipment_costs,
                    "approved_supplies_costs":
                        approved_supplies_costs,
                    "approved_subcontracting_costs":
                        approved_subcontracting_costs,
                    "approved_other_costs":
                        approved_other_costs,
                    "actual_personnel_costs":
                        actual_personnel_costs,
                    "actual_travel_costs":
                        actual_travel_costs,
                    "actual_equipment_costs":
                        actual_equipment_costs,
                    "actual_supplies_costs":
                        actual_supplies_costs,
                    "actual_subcontracting_costs":
                        actual_subcontracting_costs,
                    "actual_other_costs":
                        actual_other_costs
                }

                projects.append(project)
                save_projects()
                st.session_state.success_message = (
                   f"Project '{clean_project_name}' added successfully!"
                )

                st.rerun()

# ==========================================
# TAB 3: SEARCH PROJECT
# ==========================================

with tab3:
    st.header("Search Project")

    with st.form("search_form"):
        search_name = st.text_input(
            "Enter project name"
        )

        search_submit = st.form_submit_button(
            "Search"
        )

    if search_submit:
        if not search_name.strip():
            st.warning("Please enter a project name.")

        else:
            found_project = None

            for project in projects:
                if (
                    project["project_name"].strip().lower()
                    == search_name.strip().lower()
                ):
                    found_project = project
                    break

            if found_project:
                st.success("Project found.")

                total_approved_budget = sum(
                    found_project[column]
                    for column in approved_columns
                )

                total_actual_costs = sum(
                    found_project[column]
                    for column in actual_columns
                )

                remaining_budget = (
                    total_approved_budget
                    - total_actual_costs
                )

                st.subheader(
                    found_project["project_name"]
                )

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Approved Budget",
                    f"{total_approved_budget:,.2f}"
                )

                col2.metric(
                    "Actual Costs",
                    f"{total_actual_costs:,.2f}"
                )

                col3.metric(
                    "Remaining Budget",
                    f"{remaining_budget:,.2f}"
                )

                if remaining_budget < 0:
                    st.error(
                        "This project has exceeded "
                        "its approved budget."
                    )

                elif remaining_budget == 0:
                    st.warning(
                        "This project has used the "
                        "entire approved budget."
                    )

                else:
                    st.success(
                        "This project is within "
                        "the approved budget."
                    )

                project_df = pd.DataFrame(
                    [found_project]
                )

                st.dataframe(
                    df,
                    width="stretch",
                    hide_index=True
                )
            else:
                st.error("Project not found.")

# ==========================================
# TAB 4: UPDATE PROJECT
# ==========================================

with tab4:
    st.header("Update Project")

    project_names = [
        project["project_name"]
        for project in projects
    ]

    if project_names:

        selected_project_name = st.selectbox(
            "Select a project",
            project_names,
            key="update_project_select"
        )

        selected_field = st.selectbox(
            "Select the field you want to update",
            available_fields,
            format_func=lambda field: field_labels[field],
            key="update_field_select"
        )

        with st.form("update_form"):

            if selected_field == "project_name":
                new_value = st.text_input(
                    "Enter the new project name"
                )

            else:
                new_value = st.number_input(
                    f"Enter new {field_labels[selected_field]}",
                    min_value=0.0,
                    value=0.0,
                    step=100.0
                )

            update_submit = st.form_submit_button(
                "Update Project"
            )

        if update_submit:

            if (
                selected_field == "project_name"
                and not new_value.strip()
            ):
                st.error(
                    "Please enter a new project name."
                )

            elif selected_field == "project_name":

                clean_new_name = new_value.strip()

                existing_names = [
                    project["project_name"].strip().lower()
                    for project in projects
                    if (
                        project["project_name"]
                        != selected_project_name
                    )
                ]

                if clean_new_name.lower() in existing_names:
                    st.error(
                        "A project with this name already exists."
                    )

                else:
                    for project in projects:
                        if (
                            project["project_name"]
                            == selected_project_name
                        ):
                            project["project_name"] = clean_new_name
                            save_projects()

                            st.session_state.success_message = (
                                f"Project '{selected_project_name}' "
                                "updated successfully."
                            )

                            st.rerun()

            else:
                for project in projects:
                    if (
                        project["project_name"]
                        == selected_project_name
                    ):
                        project[selected_field] = new_value
                        save_projects()

                        st.session_state.success_message = (
                            f"Project '{selected_project_name}' "
                            "updated successfully."
                        )

                        st.rerun()

    else:
        st.info("No projects available to update.")

# ==========================================
# TAB 5: DELETE PROJECT
# ==========================================

with tab5:
    st.header("Delete Project")

    project_names = [
        project["project_name"]
        for project in projects
    ]

    if project_names:

        with st.form("delete_form"):

            project_to_delete = st.selectbox(
                "Select a project to delete",
                project_names
            )

            confirm_delete = st.checkbox(
                "I confirm that I want to delete this project."
            )

            delete_submit = st.form_submit_button(
                "Delete Project"
            )

        if delete_submit:

            if not confirm_delete:
                st.warning(
                    "Please confirm that you want to delete this project."
                )

            else:

                for project in projects:

                    if project["project_name"] == project_to_delete:

                        projects.remove(project)

                        save_projects()

                        st.session_state.success_message = (
                            f"Project '{project_to_delete}' deleted successfully."
                        )

                        st.rerun()

    else:
        st.info("No projects available to delete.")

# ==========================================
# TAB 6: DATA EXPORT
# ==========================================

with tab6:
    st.header("Export Project Data")

    if not df.empty:
        display_df = df.rename(columns=column_names)
        
        st.dataframe(
           display_df,
            width="stretch",
            hide_index=True
        )
        excel_buffer = BytesIO()

        with pd.ExcelWriter(
            excel_buffer,
            engine="openpyxl"
        ) as writer:
            display_df.to_excel(
                writer,
                index=False,
                sheet_name="Projects"
            )

        excel_data = excel_buffer.getvalue()

        st.download_button(
            label="Download Projects as Excel",
            data=excel_data,
            file_name="project_budgets.xlsx",
            mime=(
                "application/vnd.openxmlformats-"
                "officedocument.spreadsheetml.sheet"
            )
        )

    else:
        st.info(
            "No project data available for export."
        )