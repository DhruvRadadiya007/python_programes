# raise a custom error

a=int(input("enter the number :- "))

if a<5 or a>7:
    raise  ValueError("enter a correct number betweeen 5 to 7")
else:
    print("your number is:-",a)
    