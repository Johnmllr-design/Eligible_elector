# this is a python file for the "how old are you" project
# in the externship

age = int(input("how old are you?"))            # take the users input

if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")           # eligible case
else:
    print("Oops! You’re not eligible yet. But hey, only " + str(18 - age) + " years to go")     # ineligible case