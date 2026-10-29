
# Q9. Count the number of digits in an integer
# Write a Python program using a while loop to count 
# how many digits a number contains.

n=int(input("Enter the number : "))
count=0
while(n>0):
    n=n//10
    count+=1
print("Number of digits:",count)


# Q10. Find the sum of digits of a number
# Write a program using a while loop.
n=int(input("Enter the number : "))
sum=0
while(n>0):
    
    digit=n%10
    sum=sum+digit
    n=n//10
    
print("Number of digits:",sum)

# Q11. Reverse a number
# Write a program using a while loop.
n=int(input("Enter the number : "))
rev_num=0
while(n>0):
    digit=n%10
    rev_num=rev_num*10+digit
    n=n//10
print("Reversed_num:",rev_num)

# Q12. Check whether a number is a palindrome
# Write a Python program using a while loop to check whether a number reads the same forwards and backwards.

n=int(input("Enter the number : "))
temp=n
rev_num=0
while(n>0):
    digit=n%10
    rev_num=rev_num*10+digit
    n=n//10
if(temp==rev_num):
    print("Palindrome")
else:
    print("Not a plaindrome")
    
#  Q13. Find the factorial of a number 
# using a while loop.   
n=int(input("Enter the value : "))
i=1
fact_num=1
while(i<=n):
    fact_num=fact_num*i
    i+=1
print("Factorial_num : ",fact_num)

# Write a Python program to calculate the power without using the ** operator.

base=int(input("Enter the base value : "))
exponent=int(input("Enter the exponent : "))
result=1
i=1
while(i<=exponent):
    result=base**exponent
    i+=1
print(result)

#Find the product of the digits of a number
n=int(input("Enter the number : "))
product=1
while(n>0):
    digit=n%10
    product=product*digit
    n=n//10
print("Product of digits :",product)

#Fibonacci Series:

n=int(input("Enter the value : "))
a=0
b=1
count=0
while(count<n):
    print(a,end =" ")
    next_num=a+b
    a=b
    b=next_num
    count+=1
 
 
#Prime number    
n = int(input("Enter the number: "))
i = 2

if (n < 2):
    print("Not a prime number")
else:
    while (i < n):
        if (n % i == 0):
            print("Not a prime number")
            break
        i += 1
    else:
        print("Prime number")
        
        
        
#Largest digit
n=int(input("Enter the number : "))
largest=0
while(n>0):
    digit=n%10
    
    if(digit>largest):
        largest=digit
    
    n=n//10
print("Largest number :",largest)

# Question 19: Find the smallest digit

n=65413
smallest=9
while(n>0):
    digit=n%10
    if(digit<smallest):
        smallest=digit
    n=n//10
print("Smallest digit : ",smallest)


# Question 20: Count even and odd digits
n=45789611
even=0
odd=0
while(n>0):
    digit=n%10
    if(digit%2==0):
        even+=1
    else:
        odd+=1
    n=n//10
print("Even digits:",even)
print("Odd digits:",odd)


# Question 21: Armstrong Number
n=int(input("Enter the number : "))
temp=n
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit**3
    n=n//10
    
if(sum==temp):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    
# Question 22: Check whether a number is a palindrome

n=int(input("Enter the number : "))
temp=n
rev_num=0
while(n>0):
    digit=n%10
    rev_num=rev_num*10+digit
    n=n//10
if(temp==rev_num):
    print("Palindrome")
else:
    print("Not a palindrome")
    
    
n=int(input("Enter the value : "))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i+=1
print("Sum:",sum)

# Write a Python program using a while loop to calculate the sum of all even numbers from 1 to N.
n=int(input("Enter the value : "))
sum=0
i=2
while(i<=n):
    sum=sum+i
    i+=2
print("Sum : ",sum)


# Write a Python program using a while loop to count the number of multiples of 3 from 1 to N.
n=int(input("Enter the value : "))
count=0
i=3
while(i<=n):
    count+=1
    i+=3
print("Count:",count)    


# Write a Python program using a while loop to 
# print the multiplication table of a number from 1 to 10.
n=7
i=1
while(i<=10):
    mul=n*i
    print(mul)
    i+=1

# count the number of digits in a given positive integer.

n=56400
count=0
while(n>0):
    digit=n%10
    count+=1
    n=n//10
print("Count:",count)

#Rev
n=1234
rev_num=0
while(n>0):
    digit=n%10
    rev_num=rev_num*10+digit
    n=n//10
print("Rev_num:",rev_num)
 
 
 
#Strong Number:    
n=int(input("Enter the number : "))
temp=n
sum=0
while(n>0):
    digit=n%10
    fact=1
    i=1
    while(i<=digit):
        fact=fact*i
        i+=1
    sum=fact+sum
    n=n//10
    
if(sum==temp):
    print("Strong number")
else:
    print("Not an Strong number")




