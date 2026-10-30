#Question 1: Multiples of 3
for i in range(1,11):
    print(f"{3}X{i}={3*i}")
    
for i in range(3,31,3):
    print(i,end= " ")


# Question 2: Sum of First 10 Numbers
sum=0   
for i in range(1,11):
    sum=sum+i
print("Sum:",sum)


# Question 3: Print Your Name Letter by Letter
name="Jeevan"
for index,letter in enumerate(name):
    print(letter*(index+1)) 

# Question 4: Count Vowels in a String

name=input("Enter a name: ")
vowels="aeiouAEIOU"
count=0
for letter in name:
    if (letter in vowels):
        count+=1
print("Count:",count)


# Question 5: Count Even and Odd Numbers
numbers =1,2,3,4,5
even=0
odd=0
for num in numbers:
    
    if(num%2==0):
        even+=1
    else:
        odd+=1
print("Even Count:",even)
print("Odd Count:",odd)


#By Entering the input counting the even and odd
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even count:", even)
print("Odd count:", odd)

#Sum of numbers:
numbers=[5,10,15,20]
sum=0
for num in numbers:
    sum=sum+num
print(sum)

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)
    
name="Jeevan"
for letter in name:
    print(letter)
    
name="Jeevan"
for index,letter in enumerate(name):
    print(letter*(index+1)) 


name="Jeevan"
vowels="aeiouAEIOU"
count=0
for letter in name:
    if(letter in vowels):
        count+=1
print("Count:", count) 


