# Question: Write a program that counts from 1 to 10 using a while loop.
i=1
while(i<=10):
    print(i)
    i+=1

# Question: Print all odd numbers between 1 and 20 using a while loop.


#By using the while and if
i=1
while(i<=20):
    if(i%2!=0):
        print(i)
    i+=1

#Only using the while loop    
i=1
while(i<=20):
    print(i)
    i+=2
    
# A bus has 8 seats. Each time a seat is booked, 
# the available seats decrease. When no seats remain,
# stop the loop and display "All seats are booked."
    
i=8
while(i>0):
    print("Seat booked Successfully!")
    i-=1
    print("Available seats",i)
print("All seats are booked.")
            

# Question: Count down from 10 to 1 using a while loop, then print "Happy New Year!"

i=10
while(i>=1):
    print(i)
    i-=1
print("Happy New Year!..")

# Question: Print numbers from 1 to 10 using a while loop.
i=1
while(i<=10):
    print(i)
    i+=1
    
# Print numbers from 10 to 1 in reverse order.
i=10
while(i>=1):
    print(i)
    i-=1 
    
# Print all even numbers from 1 to 20.
i=1
while(i<=20):
    if(i%2==0):
        print(i)
    i+=1    
    
# Q4. Print all odd numbers from 1 to 20.
i=1
while(i<=20):
    print(i)
    i+=2

# Q5. Print the multiplication table of 5
i=1
while(i<=10):
    n=5*i
    print(f"5 X {i}= {n}")
    i+=1


i=1    
while(i<=10):
    n=2*i
    print(f"2 X {i}={n}")
    i+=1    
    
# Q6. Find the sum of numbers from 1 to 10 using a while loop.

i=1
sum=0
while(i<=10):
    sum=sum+i
    i+=1
print(sum)

# Print the squares of numbers from 1 to 10.
i=1
while(i<=10):
    print(i*i)
    i+=1
    

# Write a program that asks the user to enter a number and prints from 1 up to that number.
n=int(input("Enter the nummber : "))
i=1
while(i<=n):
    print(i)
    i+=1

        


        