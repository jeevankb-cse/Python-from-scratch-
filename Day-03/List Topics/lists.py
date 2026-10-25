list=["bru","Coffce","Milk","Tea"]
print(list[-1:])
list.pop()
print(list)  #it removes the last element of the list 
list.pop(3)
print(list)

#Insert----> it adds the value at the specifice place that we want in the list ls.
ls=[10,20,30,40]
ls.insert(3,35)
print(ls)

#Clear
ls1=[10,20,30,40,50]
ls1.clear()
print(ls1)

#Append------>It add the values at the last place 
ls2=[10,20,30,40,50]
ls2.append(45)
print(ls2)   

#pop 
ls3=[10,20,30,40,50,60,70,80,90,100]
ls3.pop()
print(ls3)  #it removes the last element in the list 
ls3.pop(0)  #whenever we mention it will removes the particular element in ls3
print(ls3)


#Changing the element in the list using the list oprations 
ls4=[10,20,30,40,50]
ls4[0]=5
print(ls4)  #[5, 20, 30, 40, 50]