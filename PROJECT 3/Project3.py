phonebook={
    "Kushal" : 8595628246,
    "Harshit" : 9958844561,
    "Prashant" : 9756880621,
    "Shruti" : 7060708390
}
print(phonebook)
# add contact 
phonebook.update({"Gurmeet": 9087654321})
print(phonebook)
# search contact
key=input(" Enter the name to search contact number :\n")
value = phonebook.get(key)
print(value)
# # delete contact 
x = input("Enter the key to delete the contact number :\n")
phonebook.pop(x)
print(phonebook)

# prevent duplicate entries
name = input(" Enter the name :")
checkname=list(phonebook)
number = input("Enter the number :")
checknumber = list(phonebook.values())

if name in checkname or number in checknumber:
    print("Contact already exists!")
else:
    phonebook.update({name : number})
print(phonebook)

# partial contact search
search=input(" Enter the partial name from the phonebook : ")
found=0
for x in phonebook.keys():
    if search.lower() in x.lower(): 
        found=1
        break
        
if found:
    print(x)
else:
    print("contact not found!")


 
