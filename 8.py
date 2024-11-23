# string methods
# strings are immutable....all the methods return a new string

a="dhruv"

print(a.upper()) # to print upper case
print(a.lower()) # to print lower case 
############################### 
a="my name is dhruv"
print(a.capitalize()) # to print first character as upper case
###############################
print(a.replace("d","Dhh")) # to replace a character
###############################
print(a.count("r")) # to count the number of a character if not then throws a -1
print(a.index("u")) # to find the index of a character if not then throws a error
###############################
a="  hello dhruv  "
print(a.startswith("d")) # to check if the string starts with a given character
print(a.endswith("v")) # to check if the string ends with a given character
###############################
a="hello dhruv"
print(a.split("h")) # to split the string based on a given character
###############################
a="//hello dhruv//"
print(a.strip("/")) # to remove leading and trailing spaces
a="//i am dhruv//"
print(a.lstrip("/")) # to remove leading spaces
a="//i am dhruv//"
print(a.rstrip("/")) # to remove trailing spaces
###############################
a="HELLOdhruv007" # spaces will give false
print(a.isalnum()) # to check if the string contains only alphanumeric characters = a-z-A-Z-num//no punctuation
a="HELLOdhruv"
print(a.isalpha()) # to check if the string contains only alphabetic characters = a-z-A-Z// no number or punctuation
a="007"
print(a.isdigit()) # to check if the string contains only digits = only numbers
a="dhruv"
print(a.islower()) # to check if the string contains only lowercase characters
a="HELLO"
print(a.isupper()) # to check if the string contains only uppercase characters
a="Hello Dhruv"
print(a.istitle()) # to check if the string contains only titlecase characters

# print(a.isprintable()) # to check if the string contains printable characters

# print(a.isspace()) # to check if the string contains only spaces

# print(a.isnumeric()) # to check if the string contains only numeric characters

# print(a.isdecimal()) # to check if the string contains only decimal characters

###############################
a="this is lower case"
print(a.swapcase()) # to convert lowercase to uppercase and uppercase to lowercase
a="this is title"
print(a.title()) # to convert the first character of each word to uppercase and the remaining characters to lowercase
a="this is center"
print(a.center(50)) # to center align the string with spaces    
a="hiii"
###############################
print(a.ljust(10)) # to left align the string with spaces
a='hiii'
print(a.rjust(10)) # to right align the string with spaces
a="string"
print(a.zfill(10)) # to fill the string with zeros at the left side
###############################
a="radadiya"
print(a.find("r")) # to find the index of the first occurrence of a character

a="radadiya"
print(a.rfind("a")) # to find the index of the last occurrence of a character
###############################
a="dhruv"
# print(a.format_map({"name":a})) # to format the string using a dictionary

# print(a.format_args(a)) # to format the string using arguments

# print(a.format_spec(a)) # to format the string using format specification

# print(a.isidentifier()) # to check if the string is a valid identifier




##############################
# txt = "My name is dhruv"
# x = txt.encode() # to convert the string to bytes
# print(x)

# print(x.encode().decode()) # to convert the bytes back to string

# a="hello i am dhruv"
# # print(a.format("dhruv")) # to format the string using placeholders
###############################