# Version 1 (inputs)

# Project Budget App

## Problem

Project managers need a simple tool to compare approved project budgets with actual expenditures and monitor project spending by category.

## User

- Project Manager
- Finance Manager
- NGO Staff

## Inputs

### Project Information

- Project Name

### Approved Budget

- Approved Personnel Budget
- Approved Travel Budget
- Approved Equipment Budget
- Approved Supplies Budget
- Approved Subcontracting Budget
- Approved Other Budget

### Actual Costs

- Personnel Costs
- Travel Costs
- Equipment Costs
- Supplies Costs
- Subcontracting Costs
- Other Costs

## Process

### Category-Level Calculations

For each category:

Remaining Budget = Approved Budget - Actual Costs

### Project-Level Calculations

- Calculate Total Approved Budget
- Calculate Total Actual Costs
- Calculate Total Remaining Budget

### Budget Status Check

- Check whether any category exceeds the approved budget
- Check whether total actual costs exceed total approved budget

## Outputs

### Project Summary

- Project Name
- Total Approved Budget
- Total Actual Costs
- Total Remaining Budget

### Category Summary

Personnel
- Approved Budget
- Actual Costs
- Remaining Budget

Travel
- Approved Budget
- Actual Costs
- Remaining Budget

Equipment
- Approved Budget
- Actual Costs
- Remaining Budget

Supplies
- Approved Budget
- Actual Costs
- Remaining Budget

Subcontracting
- Approved Budget
- Actual Costs
- Remaining Budget

Other
- Approved Budget
- Actual Costs
- Remaining Budget

### Budget Status

- Within Budget
- Budget Exceeded

## Workflow

START

Enter Project Name

Enter Approved Budget Categories

Enter Actual Cost Categories

Calculate Remaining Budget by Category

Calculate Total Approved Budget

Calculate Total Actual Costs

Calculate Total Remaining Budget

Check Budget Status

Display Project Budget Summary

END

## Coding Plan - Version 1

Task 1: Show app title

Task 2: Ask user to enter project name

Task 3: Ask user to enter approved budget categories

Task 4: Ask user to enter actual costs categories

Task 5: Calculate remaining budget for each category

Task 6: Calculate total approved budget

Task 7: Calculate total actual costs

Task 8: Calculate total remaining budget

Task 9: Check budget status

Task 10: Display project budget summary

END


## Version 2 - Store Multiple Projects

## Goal
The app should allow the user to enter more than one project.

## User Flow
START

Ask how many projects the user wants to enter

For each project:
- Enter project name
- Enter approved budget categories
- Enter actual costs
- Calculate total approved budget
- Calculate total actual costs
- Calculate remaining budget
- Check budget status

Display summary for each project

END

# Version 3 Save project to CSV using Pandas


# Version 4: Load/read projects from CSV

# Version 5: Simple menu
- Add project
- View projects
- Search project
- Save
- Exit

# Version 6: Implement search functionality

# Version 7: Update a project

# Version 8: Delete a project

# Version 9: Streamlit web app

# Version 10: AI Budget Assistant