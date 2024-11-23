# exeption handling

a=input("enter the an integer:- ")
try:
    for i in range(int(a)):
        print(i)

except:
    print("enter a valid integer!!!!!!!!")


print("your code is here:")
print("end of the program")

try:
    a=int(input("enter the an integer:- "))
    print(a)
    
except ValueError:
    print("you must enter avalid integer")

except SyntaxError:
    print("Syntex is not proper")
    