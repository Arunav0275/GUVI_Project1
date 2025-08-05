# GUVI_Project1: HR Data Cleaning for Analysis

📌 Problem Statement
Clean and prepare raw HR employee data by handling missing values, correcting data types, and standardizing formats.

## ✅ Expected Outcome:
- No missing values  
- Correct data types  
- Encoded categorical columns

## 🧾 Project Description
This project is designed to clean HR data entered manually by the user, allowing:
- Continuous entry of employee records
- Handling of missing values (None) for both numerical and categorical data
- Automatic imputation using:
  - Mean for numerical fields (Age, Salary, Experience)
  - Mode for categorical fields (Department, Attrition, Education, Gender)
- Data is saved in a CSV file which gets updated on every run

## 🛠 Technologies Used
- Python 3
- Pandas
- NumPy

## 📁 Input Fields
- EmployeeID (int)
- Age (int)
- Department (categorical)
- Attrition (Yes/No)
- Salary (float)
- Experience (float)
- Education Level (HighSchool/Bachelor/Master/PhD)
- Gender (Male/Female/Other)

## 🚀 How to Run This Project
1. Clone the repository:
    git clone https://github.com/Arunav0275/GUVI_Project1.git
    cd GUVI_Project1
2. Install dependencies:
     pip install pandas numpy
3. Run the script:
     python3 GUVI.py
4. Follow the prompts to input data.
5. The script will:
    .Save your data to a CSV file (new or existing)
    .Handle missing values
    .Clean and finalize the CSV

