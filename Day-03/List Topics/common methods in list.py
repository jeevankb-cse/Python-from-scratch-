#copy

ls1=[1,2,3,4,5]
ls2=ls1.copy()
print(ls2)

#Count--->Count how many times a particular value appears or number of appereances in the ls or occurances in the list
ls3=[10,20,30,40,50,30,20,10]
print(ls3.count(20))


#Remove  removes()  a value from the list..
ls3 = [1020, 3040, 5060]
ls3.remove(1020)
print(ls3)


#Sort 
ls4=[1,32,20,400,52,21,11]
ls4.sort()
print(ls4)

#Want in descending order 
ls4.sort(reverse=True)
print(ls4)


#Index
ls=["Apple","Mango",True,"Lash"]
print(ls.index(True))

#Reverse

ls=["Apple","Mango","Banana","Jackfurit"]
ls.reverse()
print(ls)

#Append--->Taking only one items at one time

l=[10,20,30,40,50,60]
l.append(70)
print(l)

#Extend
list=[10,20,30]
list.extend([40,50,60,70,80,90,100])
print(list)
