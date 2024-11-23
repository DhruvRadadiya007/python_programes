#function in python 

def cgpaconvert(): 
    cgpa = float(input("Enter your CGPA: "))
    if cgpa >= 4.0:
        print("Grade: A+")
    elif cgpa >= 3.7:
        print("Grade: A")
    elif cgpa >= 3.3:
        print("Grade: B+")
    elif cgpa >= 3.0:
        print("Grade: B")
    elif cgpa >= 2.7:
        print("Grade: C+")
    elif cgpa >= 2.3:
        print("Grade: C")
    elif cgpa >= 2.0:
        print("Grade: D")
    else:
        print("Grade: F")
        
cgpaconvert()

def unknown(): # for passing this function
    pass

def names(): 
    name1=input("enter your first name:-")
    name2=input("enter your last name:-")
    print("hello "+name1,name2)
    
names()

# def names(a,b): 
#     print("hello "+a,b)
    
# a="dhruv"
# b="radadiya"    
# names(a,b)    