# Q1. Accessing a String
# Given:
# text = "Python"
# Print the first character and the last character.
text="Python"
print(text[0:6:5])

# Q2. String Indexing
# Given:
# text = "Programming"


# Print the character at:
# - Index 0
# - Index 4
# - Index -1

text = "Programming"
print(text[0])
print(text[4])
print(text[-1])


# Q3. String Slicing
# Given:
# text = "Programming"


# Print:
# - First 5 characters
# - Last 4 characters
# - The complete string in reverse

text = "Programming"
print(text[0:5])
print(text[-4:])
print(text[::-1])

# Q4. String Length
# Take a string as input and print its length using len().
# Example:
# Input: Python
# Output: 6

n="Python"
print(len(n))

# Q5. Length Excluding Spaces
# Take a sentence as input and print the number of characters excluding spaces.
# Example:
# Input: Python is awesome
# Output: 16

sentence=input("Enter the sentence : ")
print(len(sentence))

'''Q6. String Concatenation
Take two strings as input and combine them 
into one string.
Example:
Input:
Hello
World'''

n1=input("Enter the word : ")
n2=input("Enter the word : ")
print(n1+n2)

'''Q7. Concatenation With Space
Take first name and last name as input and create the full name with a space between them.
Example:
Input:
Jeevan
K B

Output:
Jeevan K B'''
first_name="Jeevan"
last_name="K B"
print(first_name+last_name)
full_name=(first_name + " "+ last_name)
print(full_name)


'''
Q8. String Repetition
Given:
text = "Python "
Print the string 3 times using the repetition operator.'''

text = "Python"
print(text*3)



'''Q11. Remove Spaces
Given:
text = "   Python is awesome!   "


Remove the spaces from the beginning and end of the string.'''

text = "   Python is awesome!   "
print(text.strip())

'''Q12. Replace Spaces
Given:
text = "   Python is awesome!   "


Replace every space with _.'''

text = "   Python is awesome!   "
print(text.replace(" ","_"))


'''Q13. Count a Character
Take a string and a character as input. Count how many times that character occurs in the string.
Example:
Input:
Python programming
p

Output:
2
'''

word=input("Enter the word : ")
char=input("Enter the char : ")
print(word.count(char))


'''Q14. Escape Sequences
Write a Python program to produce exactly this output:
Hello
    World

Use an escape sequence.
'''
sentence="Hello\n   World"
print(sentence)





























