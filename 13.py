# for loop

name="dhruv" # for printing the chracters in string
for i in name:
    print(i)
    
print("----------------------------------------------------------------")

a=["yellow","green","red"] # for printing strings in the list and the characters in the string
for i in a:
    print(i)
    for a in i:
        print(a)
print("----------------------------------------------------------------")
for a in range(5): # range function used to print numbers (n-1) starts from 0
    print(a)

print("----------------------------------------------------------------")
for b in range(1,5): # start= 1 and end =5-1
    print(b)        

print("----------------------------------------------------------------")
for C in range(0,11,2): # start= 0 and end =11-1 and step=2 
    print(C)        