# Student Score Analyzer
marks = [78,85,90,67,85,92,78]
sum = 0
for item in marks:
    sum+=item
avg = sum/len(marks)
print(avg)
highest = max(marks)
lowest = min(marks)
print(highest)
print(lowest)
count=0
for i in marks:
    if i> avg:
       count+=1
print(count)
score= int(input("Enter the marks obtained : "))
if score >=90:
    print("A grade")
elif score <90 and score>=85:
    print("B grade")
elif score <85 and score>=50:
    print("C grade")
else:
    print("Fail")
