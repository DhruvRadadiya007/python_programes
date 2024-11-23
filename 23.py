# set methods

# union method
s1 = {1, 2, 3, 4}
s2 = {1, 8, 9, 4}
print(s1.union(s2))  # adds element from s1 to ss2 without duplicates
s1.update(s2)  # update the values in s1
print(s1, s2)

# intersection method
s1 = {"dhruv", "radadiya", "dhulo"}
s2 = {"hello", "dhruv", "dhulo"}
s3 = s1.intersection(s2)  # find the common value and store in other variable
print(s3)
s1.intersection_update(s2)  # to store the common values in the s1
print(s1)
print("symetric")

# symmetric difference
s1 = {"dhruv", "radadiya", "dhulo"}
s2 = {"hello", "dhruv", "dhulo"}
s3 = s1.symmetric_difference(s2)  # to find the different values fron both the sets 
print(s3)
s1.symmetric_difference_update(s2)
print(s1) # to update the values in s1 set

# difference method

s1 = {"dhruv", "radadiya", "dhulo"}
s2 = {"hello", "dhruv", "dhulo"}
s3 = s1.difference(s2)  # to find the values in s1 that are not in s2
print(s3)
s1.difference_update(s2)   # to update the values in s1 that are not in s2

# isdisjoint set

s1 = {"dhruv", "radadiya", "dhulo"}
s2 = {"hello", "dhruv", "dhulo"}
print(s1.isdisjoint(s2))  # to check if the two sets have no common values

# issuperset set

s1 = {"dhruv", "radadiya", "dhulo"}
s2 = {"hello", "dhruv", "dhulo", "radadiya"}
print(s1.issuperset(s2))  # to check if s1 is a superset of s2

# issubset set

s1 = {"dhruv", "radadiya", "dhulo"}
s2 = {"hello", "dhruv", "dhulo", "radadiya"}
print(s1.issubset(s2))  # to check if s1 is a subset of s2

# add method

s1 = {"dhruv", "radadiya", "dhulo"}
s1.add("hello")  # to add a value to the set
print(s1)

# remove method

s1 = {"dhruv", "radadiya", "dhulo"}
s1.remove("dhruv")  # to remove a value from the set
print(s1)

# discard method

s1 = {"dhruv", "radadiya", "dhulo"}
s1.discard("radadiya")  # to remove a value from the set if it exists
print(s1)

# clear method

s1 = {"dhruv", "radadiya", "dhulo"}
s1.clear()  # to remove all values from the set
print(s1)

# pop method

s1 = {"dhruv", "radadiya", "dhulo"}
print(s1.pop())  # to remove and return a random value from the set
print(s1)

# update method

s1 = {"dhruv", "radadiya", "dhulo"}
s2 = {"hello", "dhruv", "dhulo", "radadiya"}
s1.update(s2)  # to add all values from s2 to s1
print(s1)

# copy method

s1 = {"dhruv", "radadiya", "dhulo"}
s2 = s1.copy()  # to create a copy of the set
print(s2)

# frozenset method

s1 = {"dhruv", "radadiya", "dhulo"}
s2 = frozenset(s1)  # to create a frozenset from the set
print(s2)

# delete entire set
s1 = {"dhruv", "radadiya",}
del s1
