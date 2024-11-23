# for loop with else statement in python

# for i in range(5):
#     print(i)
    
# else:
#     print("limit reached!!!!!")
    
print("-------------------example:-2------------------")
# in this case it will not print the else statement because the loop is break not completed
for i in range(5):
    print(i)
    if i == 3:
        break

else:
    print("limit reached!!!!!")
    

for x in range(5):
        print("the number {} in for loop".format(x+1))
        
else:
    print("your for loop is over")




