# string formatting and f-string

a=("i am {} and i am from {}") # string with empty brackets

# a=("i am {0} and i am from {1}") # you can also use 1 or 0 to add the variables

st="Gujarat" #state to add to string a
nm="Dhruv" #name to add to string a

print(a.format(nm,st)) # method for formatting the string

# using f-string to do same thing in more better way
# by the use of f-string you can directly put the string while printing it
nm="Dhruv" #name to add to string b
st="Gujarat" #state to add to string b
b = "i am {} and i am from {}"
print(f"i am {nm} and i live in {st}")

# 
price = 49.09999
txt = f"For only {price:.2f} dollars!" # you can add any variable to f-string(the .2f is used to select 2 decimal only)
print(txt)
# print(txt.format())
print(type(f"{2 * 30}")) # you can also directly type the equation and the output will be in string
