dataset = {
    "Name" :['A','B','C','D'],
    "Salary" :[23030,45300,459034,75600],
    "Age" : [23,45,56,18]}
import pandas as pd


df=pd.DataFrame(dataset,index=["emp1","emp2","emp3","emp4"])
expected_salary=df[df["Salary"]>50000]
print("\nSalary :\n",expected_salary)
age = df[df["Age"]<30]
print("\nAge :\n",age)
output= df[(df["Salary"]>50000 )& (df["Age"]<30)]
print("\nCombined Output \n:",output) 
with open("Newfile.txt","w") as file:
    file.write(str(output))
