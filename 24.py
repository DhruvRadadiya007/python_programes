# DICTIONARY

# Create a dictionary

student_data = {

    "Name": "John Doe",

    "Age": 25,

    "City": "New York"

}

# Access a value

print(student_data["Name"])

# print(student_data["name2"]) # it will show error due to no data in dictionary
print(student_data.get("name2")) # it will show [none] for not having any data in dictionary 
print(student_data.keys()) # to print all the keys in dictionary

for key in student_data.keys():
    print(student_data[key])
    

print(student_data.items())
for key, value in student_data.items():
    print(f"The value corresponding to the key {key} is {value}")