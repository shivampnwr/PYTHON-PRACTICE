# Open CSV file
file = open("data.csv", "r")

# Read all lines
lines = file.readlines()

# Close file
file.close()

# Empty list to store data
students = []

# Skip header line using [1:]
for line in lines[1:]:

    # Remove extra spaces/newline
    line = line.strip()

    # Split data using comma
    parts = line.split(",")

    # Store in dictionary
    student = {
        "NAME": parts[0],
        "AGE": int(parts[1]),
        "MARKS": int(parts[2])
    }

    # Add dictionary to list
    students.append(student)

# Print final data
print(students)

# BONUS → Calculate average marks
total = 0

for student in students:
    total += student["MARKS"]

average = total / len(students)

print("\nAverage Marks:", average)
