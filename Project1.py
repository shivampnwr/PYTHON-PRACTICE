# Data Cleaner (list procdessing)
data =[10,None,20,10,"",30,None,40]
# remove duplicate values
unique_data = list(set(data))
print(unique_data)
# remove  invaled values
unique_data.remove(None)
unique_data.remove("")
print(unique_data)
# count of removed item
original_length=len(data)
cleaned_length = len(unique_data)
removed_length = original_length - cleaned_length
print(removed_length)
# sorted list
print(sorted(unique_data))




