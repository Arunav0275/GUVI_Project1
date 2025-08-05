import pandas as pd
import numpy as np


def get_input(prompt, dtype=str, allow_blank=True):
    while True:
        value = input(prompt).strip()
        if not value and allow_blank:
            return None
        try:
            return dtype(value)
        except ValueError:
            print(f"Invalid input. Expected a {dtype.__name__}.")

def get_categorical_input(prompt, valid_options, allow_blank = True):
    option_str = "/".join(valid_options)
    valid_map = {opt.lower(): opt for opt in valid_options}
    while True:
        value = input(f"{prompt} ({option_str}): ").strip().lower()
        if not value and allow_blank:
            return None
        if value in valid_map:
            return valid_map[value]
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")


def collect_employee_data():
    employees = []
    print(f"Enter employees data")

    departments = ['Sales', 'IT', 'HR', 'Finance', 'Operations']
    attrition_vals = ['Yes', 'No']
    edu_level = ['HighSchool', 'Bachelor', 'Master', 'PhD']
    genders = ['Male', 'Female', 'Other']

    while True:
        data = {}

        data['EmployeeID'] = get_input(f"Enter Employee ID: ", int)
        data['Age'] = get_input(f"Enter employee age: ", int)

        data['Department'] = get_categorical_input(f"Enter Department", departments)
        data['Attrition'] = get_categorical_input(f"Enter Attrition ", attrition_vals)
        data['Salary'] = get_input(f"Enter Salary: ", float)
        data['Experience'] = get_input(f"Enter Experience in years: ", float)
        data['Education'] = get_categorical_input(f"Enter Education Level: ", edu_level)
        data['Gender'] = get_categorical_input(f"Enter Gender", genders)

        employees.append(data)

        out = input('Do you want to enter another employee? (y/n): ').strip()
        if out != 'y':
            break
    
    return pd.DataFrame(employees)


df_new = collect_employee_data()
file_name = input("Enter csv file name in which you want to enter the data: ")
try:
    df_existing = pd.read_csv(f"{file_name}.csv")
except:
    df_existing = pd.DataFrame()

df_updated = pd.concat([df_existing, df_new], ignore_index=True)

for col in ['Age','Salary','Experience']:
    df_updated[col] = df_updated[col].fillna(df_updated[col].mean())

for col in ['Department','Attrition','Education','Gender']:
    mode_val = df_updated[col].mode(dropna=True)
    if not mode_val.empty:
        df_updated[col] = df_updated[col].fillna(mode_val[0])
    else:
        df_updated[col] = df_updated[col].fillna('Unknown')


df_updated.to_csv(f"{file_name}.csv", index = False)
print("Employee data updated in csv file!")



