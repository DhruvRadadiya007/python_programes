import time # time module
# timings according to time zone
a=time.strftime('%H:%M:%S')  # according to 24 hours time 
print(a)

# according to 12 hours time
b=int(time.strftime('%I')) #hour
print(b)
c=int(time.strftime('%M')) #minute
print(c)
d=time.strftime('%p') # AM or PM
print(d)

# logic to find the right greeting according to time
if(b>=5 and d=="AM"):
    print("good morning")
elif(b>=12 or b<=6 and d=="PM"):
    print("good afternoon")
elif(b>=6 and d=="PM"):
    print("good evening")