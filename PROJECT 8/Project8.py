import pandas as pd
dataset = {
    "Name" :['A','B','C','D'],
    "Dept" :['IT','HR' ,'IT','HR'],
    "Salary":[50000,40000,60000,45000]
    
}
df = pd.DataFrame(dataset,index=['employee1','employee2','employee3','employee4'])
print(df)

# avg salary per department
avg_salary_per_dept = df.groupby("Dept")["Salary"].mean()
print("\n AVERAGE SALARY PER DEPARTMENT :",avg_salary_per_dept)

# highest paid employee
highest_salary =df.groupby("Dept")["Name"].max()
print("\nHIGHEST SALARY PER DEPARTMENT :",highest_salary)

# number of employees per department
no_of_employees=df.groupby("Dept")["Name"].count()
print("\nNUMBER OF EMPLOYEES PER DEPARTMENT :",no_of_employees)

# Sort department by average salary
sort_dept_by_avg_salary = df.sort_values(by=["Dept"],ascending=False)
print("\nORT DEPARTMENT BY AVERAGE SALARY :",sort_dept_by_avg_salary)
