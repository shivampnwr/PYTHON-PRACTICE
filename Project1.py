# Data Cleaner (list procdessing)
data =[10,None,20,10,"",30,None,40]
# Remove None and empty string from the list
junk_data = [None, ""]
unique_data=[]

cleaned_data = []
for item in data:
    if item not in junk_data:
        cleaned_data.append(item)
print(cleaned_data)
for item in cleaned_data:
    if item not in unique_data:
        unique_data.append(item)
print(unique_data)



original_length = len(data)
cleaned_length = len(unique_data)
removed_length = original_length - cleaned_length
print(removed_length)
# sorted list
unique_data.sort()
print(unique_data)
