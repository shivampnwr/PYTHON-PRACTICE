import numpy as np
import pandas as pd
import io
result ="""
NAME,MATHS,SCIENCE,ENGLISH
AMIT,80,70,85
RIYA,90,88,92
JOHN,60,65,70
"""
df = pd.DataFrame
df = pd.read_csv(io.StringIO(result))

df["AVERAGE"] = (df["MATHS"] + df["SCIENCE"] + df["ENGLISH"])/3
# avg_score_per_student = df.groupby("NAME")["AVERAGE"].mean()
avg_score_per_student = df.groupby("NAME")["AVERAGE"].mean()
print("AVERAGE SCORE PER STUDENT  :",avg_score_per_student)
topper = avg_score_per_student.idxmax()
print("\nTOPPER :",topper)

# Calculate the class average
average = df["AVERAGE"].mean()
print(f"\nClass Average: {average:.2f}")

# Filter the dataframe and count the number of rows
num_above_average = len(df[df["AVERAGE"] > average])
# OR: num_above_average = df[df["AVERAGE"] > average].shape[0]

print(f"\nNumber of students above average: {num_above_average}")

# add grade column 
#adding grade column based on average marks
df["GRADE"] = np.where(df["AVERAGE"] >= 90, 'A',
                       np.where(df["AVERAGE"] >= 80, 'B',
                                np.where(df["AVERAGE"] >= 70, 'C', 'D')))
print(df)
# subject wise average
sub_avg = df[["MATHS", "SCIENCE", "ENGLISH"]].mean()
print(f"\nSUBJECT WISE AVERAGE :\n{sub_avg}")