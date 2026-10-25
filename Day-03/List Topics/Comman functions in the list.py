#len function
list=[1,2,3,4,5,6]
print(len(list))

#sorted function-->Arrange in the ascending order
numbers=[420,231,103,63,70,60]
print(sorted(numbers))

#Creating the new sorted list
numbers=[20,30,60,52,10,5,2]
new_numbers=sorted(numbers)
print(new_numbers)

#Desc order  --> using Sorted function
num=[102,200,3044,40]
print(sorted(num,reverse=True))



#Sum --->Adding the numbers
num=[10,20,30,40,50]
print(sum(num))


#Sum --->Adding the numbers and char it give's error!!
num=[10,20,30,40,50,"Jeevan"]  #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(sum(num))

