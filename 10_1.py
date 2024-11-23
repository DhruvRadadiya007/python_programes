# elif ladder

a=int(input("enter your budget:-"))

if(a<200):
    print("your budget is not sufficient for groceries")
    
elif(a>200):
    print("your budget is sufficient for")
    
    
else:
    print("your budget is exactly sufficient for groceries")