# argument types 1.Default Arguments/2.Keyword Arguments/3.Variable length Argurnents/4.Required Arguments


print("--------------------DEFAULT ARGUMENT-----------------------------")
# 1 default argument

print("-------------------example:-1------------------")
def sum(a=12,b=20): #default arguments are (a and b)
    print("sum =",(a+b))

sum()
print("-------------------example:-2------------------")

def name(fname = "Amy", mname = "Jhon" ,Lname = "Whatson" ) :
    print( "Hello, " ,fname, mname, Lname)
    
    

print("--------------------KEYWORDD ARGUMENT-----------------------------")
# 2 Keyword argument
print("-------------------example:-1------------------")

def sum(a=12, b=20): 
    print("sum =", (a + b))


sum(b=56,a=90)  # default arguments are (a and b) ||| you can write in any order just defin the keyword |||

print("-------------------example:-2------------------")
def name( fname, mname, lname):
    print( "Hello, " ,fname, mname, lname )

name(mname = "Peter",lname = "Wesker" ,fname=" Jade" )



print("--------------------REQUIRED ARGUMENT-----------------------------")
# 3 Required argument
print("-------------------example:-1------------------")
def sum(a, b, c=90):
    print("sum =", (a + b + c))

# if default argument is not given then they become required
sum( a=56, b=90)  # required arguments are (a and b) ||| you can write in any order just defin the keyword |||




print("-------------------- VARIABLE-LENGTH ARGUMENT-----------------------------")
# 4 Required argument
print("-------------------example:-1------------------")

def average(*numbers):
    sum = 0
    for i in numbers :
        sum = sum + i
    print( "Average is:",sum / len(numbers))
    # return sum / len(numbers) # return statement also can be used to return the value

average(9,8,7,6)    
# c=average(9,8,7,6) # after using return statement you have to asign the value to the variable
# print(c) # and print the variable

print("-------------------example:-2------------------")


def name(**name):
    print("Hello, ", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="James", fname="Barnes")
