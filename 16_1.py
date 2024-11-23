# list methods
lst1=[100,99,1,2,3,4]
print("--------------------------------------------------")
lst1[0] = "harry"  # for changing the 1st element in list
print(lst1)
print("--------------------------------------------------")

lst2 = ["python", "java", "c++"]
lst1.extend(lst2)  # for adding elements from lst2 to lst1
print(lst1)
print("--------------------------------------------------")

lst1.insert(2, "ruby")  # for inserting element at 2nd position
print(lst1)
print("--------------------------------------------------")

lst1.remove("python")  # for removing element
print(lst1)
print("--------------------------------------------------")

print(lst1.index("java"))  # for getting index of element
print("--------------------------------------------------")

lst1=[100,1000,99,1,2,3,4]
lst1.sort()  # for sorting list in ascending order
# lst1.sort(reverse=True)  # for sorting list in descending order
print(lst1)
print("--------------------------------------------------")

lst1.reverse()  # for reversing list
print(lst1)
print("--------------------------------------------------")

lst3 = lst1.copy()  # for copying list
print(lst3)
print("--------------------------------------------------")

lst1.clear()  # for clearing list
print(lst1)
print("--------------------------------------------------")

lst4 = [1, 2, 3, 4, 5]
print(max(lst4))  # for getting maximum element
print(min(lst4))  # for getting minimum element
print(sum(lst4))  # for getting sum of all elements

print("--------------------------------------------------")

lst4.append(6)  # for adding element at end
print(lst4)

print("--------------------------------------------------")

lst4.pop()  # for removing element at end
print(lst4)

print("--------------------------------------------------")
lst4.pop(2)  # for removing element at given index

print(lst4)
print("--------------------------------------------------")