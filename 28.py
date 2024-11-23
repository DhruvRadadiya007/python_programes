# finallly keyword in python with exception handling

try:
    a=int(input("enter the index value:- "))
    b=[9,8,7,6]
    print(b[a])
except:
    print("enter a valid index value")
    
finally:
    print("this block will always execute") # This programme will run in any situation