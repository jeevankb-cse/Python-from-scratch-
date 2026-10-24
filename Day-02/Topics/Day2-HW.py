# # Homework
# #1.Simple Greeting Program: Write a Python program that asks the user for their name 
# # and age, then prints a personalized greeting message. Use both the + operator 
# # and f-strings for output.
Greet="Hello,"
name=input("Enter the name : ")
age=input("Enter the age : ")
result=Greet +" "+ name + " You are " + age +" old. "


result=(f"{Greet} {name} You are {age} old . ")  #With fstring
print(result)

# #2.String Manipulation Exercise: Write a Python program that:

# # Takes a sentence as input from the user.
# # Prints the sentence in all uppercase and lowercase.
# # Replaces all spaces with underscores.
# # Removes leading and trailing whitespace.

n=input("Enter the sentence : ")
print(n.upper())
print(n.lower())
print(n.replace(" ","_"))
print(n.strip())

# 3.Character Counter: Write a Python program that:

# Asks the user for a string.
# Prints how many characters are in the string, excluding spaces.

n=input("Enter the sentence : ")
print(len(n))


#4.Escape Sequence Practice: Write a Python program 
# that uses escape sequences to print the following output:

message="Hello\n    World"
print(message)


