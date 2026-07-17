# 📊 Project Budget Manager

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A Python application for managing project budgets, tracking approved and actual project costs, and monitoring project spending. The repository includes both a Command-Line Interface (CLI) version and an interactive Streamlit web application built on the same business logic.

---

## 🚀 Features

- 📊 Interactive dashboard with key budget metrics
- ➕ Add new projects
- 🔍 Search projects
- ✏️ Update project information
- 🗑️ Delete projects
- 📈 Compare approved budgets with actual costs using interactive charts
- 📥 Export project data to Excel
- 💾 Store project data in CSV format
- ✅ Prevent duplicate project entries through input validation

---

## 🖼️ Application Preview

### Dashboard

![Dashboard](images/dashboard.png)

---

## 📌 Project Versions

This repository contains two implementations of the Project Budget Manager.

### 🖥️ CLI Version (`app.py`)

A command-line application implementing the core project budget management logic, including:

- Create, update and delete projects
- Budget tracking
- CSV data storage

### 🌐 Streamlit Web Version (`streamlit_app.py`)

A modern web application featuring:

- Interactive dashboard
- Budget visualization
- CRUD operations
- Excel export
- User-friendly interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- OpenPyXL
- Git
- GitHub

---

## 📂 Project Structure

```text
project-budget-manager-python/
│
├── images/
│   └── dashboard.png
├── app.py
├── streamlit_app.py
├── projects.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aleksandrasremcev/project-budget-manager-python.git
```

Navigate to the project folder:

```bash
cd project-budget-manager-python
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Streamlit Version

```bash
streamlit run streamlit_app.py
```

### CLI Version

```bash
python app.py
```

---

## 📊 Dashboard Overview

The Streamlit dashboard provides a quick overview of all projects, including:

- Total number of projects
- Total approved budget
- Total actual costs
- Remaining budget
- Budget comparison chart
- Complete project table

---

## 🎯 Key Skills Demonstrated

This project demonstrates practical experience with:

- Python programming
- Data structures (lists and dictionaries)
- CSV file handling
- Data analysis using Pandas
- Interactive web application development with Streamlit
- CRUD (Create, Read, Update, Delete) operations
- Data validation
- Dashboard creation and data visualization
- Excel export with OpenPyXL
- Version control using Git and GitHub

---

## 👩‍💻 Author

**Aleksandra Sremcev**

GitHub: https://github.com/aleksandrasremcev