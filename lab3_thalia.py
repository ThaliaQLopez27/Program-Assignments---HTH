# Thalia L / Lab 3 / Intro to Python

#Ticket 1
username = "Toodles"
print(len(username))
#Prediction 7
#It counted every single letter. The output was 7

#Ticket 2
print(username[0]) #first letter T
print(username[len(username)-1]) #last Letter S
# PREDICT letter T and s printed
# EXPLAIN the number -1 = the index number

#Ticket 3
# PREDICT I predict both will look the same because both lines of code have the same function
Greeting = "Welcome to Loop,"
GreetingEnd = "!"

EntireGreeting = Greeting + username + GreetingEnd
print(EntireGreeting)

print(f"Welcome to Loop, {username} !")
# EXPLAIN: The F string method was 1000x easier and quicker. Using the + sign felt like I was doing unnesscary steps.

#Ticket 4
#PREDICT: I think it will give an error message since there is no X and X doesn't make it cpatial letters, its just random code.
#username[0] = "X"
print(username.upper())
#EXPLAIM: I think immutable means it can't be changed because in the incorrect code, I tried to alter that actual contents of the thread instead of the format.

#Ticket 5

