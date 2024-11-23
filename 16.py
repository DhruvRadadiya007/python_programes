# list

lst1 = ["dhruv", 16, 11, 2004, "radadiya"]
print(lst1)  # for printing whole list

print(lst1[0])  # for printing the 1st element in list

print(lst1[1:3])  # for printing elements from index 1 to 3

print(lst1[0 : len(lst1) : 2])  # for skipping the elements

print(lst1[-3])  # negative index
print(lst1[len(lst1) - 3])  # convert negative into positive

if 16 in lst1:
    print("yes there is 16")
else:  # for checking the element in list
    print("not found 16")

if "dh" in "dhruv":
    print("yes there is dh")  # for checking the element in string in list
else:
    print("not found dh")

lst = [i for i in range(10)]
print(lst)
lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]  # prints items with o in string
print(namesWith_O)

names = ["Mil", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [
    item for item in names if (len(item) >= 4)
]  # prints items with 4 OR MORE THEN 4 characters in string
print(namesWith_O)
