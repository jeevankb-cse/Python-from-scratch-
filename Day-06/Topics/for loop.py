#Even from 2 to 50
for i in range(2,51,2):
    print(i,end=" ")
    
#Odd from 1 to 50
for i in range(1,51,2):
    print(i)
 
#List compersion using the for loop:    
cities=["Bengaluru","Haveri","Hubbali","Shivamogga"]
for city in cities:
    print(city)


#Print 1 to 10
for i in range(1,11):
    print(i,end=" ")

#print 1 to 10 using while
i=1
while(i<=10):
    print(i,end=" ")
    i+=1
    
#Letters in the vertical

names="Jeevan"
for name in (names):
    print(name)
    
    
#index number:
names="Jeevan"
for name in enumerate(names):  #enumerate which is for indexing
    print(name)
  
#Unpacking like we can change name into names or etc.. anything   
name="Jeevan"
for index,letter in enumerate(name):
    print(letter*(index+1))  #position*index+1
 
 
#Indexing repersentation:    
l=[1,2,3,4,5]
for index,num in enumerate(l):
    print(f"{num} is in {index}th index")
    
    
#for loop using break condition:
numbers=[1,2,3,4,5]
for num in numbers:
    if(num==3):
        print(f"Found {num}!")
        break
    print(num)

#Continue:Which is used to skip the element
numbers=[1,2,3,4,5]
for num in numbers:
    if(num==3):
        continue
    print(num)
 
 
#Looping through a list with enumerate():    
cities=["Haveri","Koda","Bengalore"]
for index,city in enumerate(cities):
    print(f"City {index+1}: {city}")
    
#so how to use the dict in for loops

d={"name":"Jeevan","Age":21,"Income":"10rs"}

for key,value in d.items():
    print(key," ",value)

# mul of 2 :2X1=2
for i in range(1,11):
    print(f"{2}X{i}={2*i}")

#Nested for loop
# Homework
# Multiples of 3:

# Write a for loop that prints all multiples of 3 between 1 and 30.
# Sum of First 10 Numbers:

# Write a program using a for loop that calculates the sum of numbers from 1 to 10.
# Print Your Name Letter by Letter:

# Write a program that takes your name as input and prints each letter of your name using a for loop.
# Count Vowels in a String:

# Write a program that counts how many vowels are in a given string using a for loop.

    
    

