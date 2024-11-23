# kon banega carorepati exercise
Q=["what is my favourite food?", "what was my pets name?","which phone do i use?"]
A=["pizza","sheru","samsung"]
win=0
st=10000
for i in Q:
    print(i)
    user_input = input("answer: ")
    if (user_input.lower() == A[0] and user_input.lower() == A[1] and user_input.lower() == A[2] ):
        print("Correct!")
        print("you win",st)
        win=win+st
        st=st*2
    else:
        print("Wrong!")
        print("you win nothing")
        continue

print("your winnning amount is :-",win)

# # List of questions and corresponding answers
# Q = ["What is my favorite food?", "What was my pet's name?", "Which phone do I use?"]
# A = ["pizza", "sheru", "samsung"]

# win = 0  # Initialize winning amount
# st = 10000  # Start amount for the first correct answer

# # Loop through each question
# for i in range(len(Q)):
#     print(Q[i])  # Print the question
#     user_input = input(
#         "Your answer: "
#     ).lower()  # Take user input and convert it to lowercase

#     # Check if the user's answer is correct for the current question
#     if user_input == A[i]:
#         print("Correct!")
#         print(f"You win {st} points.")
#         win += st  # Add the current prize to the winning amount
#         st *= 2  # Double the stake for the next correct answer
#     else:
#         print("Wrong answer!")
#         print("You win nothing for this question.")

# # Final output of the total winning amount
# print("Your total winning amount is:", win)
