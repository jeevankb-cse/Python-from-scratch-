# Python Practice Questions & Code
# Based on the Python topics practiced
# Q1. Swap Two Variables Using a Third Variable
# Write a Python program that swaps the values of two variables using a third variable.
a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)
# Q2. Swap Two Variables Without a Third Variable
# Write a Python program that swaps the values of two variables without using a third variable.
a=10
b=20
a,b=b,a
print(a)
print(b)
# Q3. Division and Floor Division
# Take two numbers and demonstrate normal division (/) and floor division (//).
a=12
b=11
print(a/b) # 1.0909090909090908
print(a//b)
# Q4. Swap Variables Without a Third Variable
# Swap the values of two variables without using a third variable.
a=10
b=40
a,b=b,a
print(a)
print(b)
# Q5. Swap Variables Using a Third Variable
# Swap the values of two variables using a temporary variable.
a=10
b=40
temp=a
a=b
b=temp
print(a)
print(b)
# Q6. Minutes to Seconds
# Take minutes as input and convert the value into seconds.
n=int(input("Enter the minute : "))
seconds=n*60
print(seconds)
# Q7. Reverse a String
# Take a name as input and print it in reverse.
n=input("Enter your name : ")
reverse_name=n[::-1]
print(reverse_name)
# Q8. Reverse the Order of Words
# Take a sentence and reverse the order of its words.
sentence=("Jeevan is a cse engineering student at city engineering college")
reverse_sentence=" ".join(sentence.split()[::-1])
print(reverse_sentence)
# Q9. String Slicing
# Given the string "Programming", print the last 7 characters and then print the string in reverse.
text = "Programming"
print(text[-7:])
print(text[::-1])
# Q10. List Indexing and Reverse
# Given a list of numbers, print the first element and the list in reverse.
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[::-1])
# Q11. List Comprehension
# Given nums = [2, 4, 6, 8], create a new list containing 3 × each number.
nums = [2, 4, 6, 8]
new_nums=[3*num for num in nums]
print(new_nums)
# Q12. Power Using List Comprehension
# Given nums = [2, 4, 6, 8], create a new list containing 3 ** num for every number.
nums = [2, 4, 6, 8]
new_nums=[3**num for num in nums]
print(new_nums)
# Q13. Tuple
# Create a tuple containing 5 numbers and print the first element, length, and last element.
nums=(10,2,3,4,5)
print(nums[0])
print(len(nums))
print(nums[-1]) # Last Element
# Q14. Enumerate
# Given fruits = ["Apple", "Banana", "Mango", "Orange"], print each index along with its value.
fruits = ["Apple", "Banana", "Mango", "Orange"]
for index,fruit in enumerate(fruits):
    print(index,"---->",fruit)
# Q15. Function to Add Two Numbers
# Create a function add() that adds two numbers and prints the sum.
def add():
    a=10
    b=20
    sum=a+b
    print(sum)
add()
# Q16. Even or Odd
# Check whether a number is even or odd using the modulus operator.
z=12
if(z%2==0):
    print("Even")
else:
    print("Odd")
# Q17. Function to Find Square
# Create a function square(n) that returns the square of a number.
def square(n):
    squr=n**2
    return squr
print(square(5))
