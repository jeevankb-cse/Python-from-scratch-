t=("apple",)  # Comma, is mandatory in the tuple 
print(type(t))  #---> Type checking

#Len in the tuple 
print(len(t))


#Indexing in the tuple in tuple (Nested tuple)
tu=("Papaya","Mango","Bannana",(1,2,3))
print(tu[3][1])



#Indexing tuple in  list
tu=("Papaya","Mango","Bannana",[1,2,3])
print(tu[3][1])


gender=("Male","Female","Others")
print(gender[1:2])


#Tuple Cannot be changed  so it's immutable

gender=("Male","Female","Others")
print(gender[1:2])
gender[0]="Male 1.0"
print(gender)


#List can change so it's muttable 
gender=["Male","Female","Others"]
gender[0]="Male 1.0"
print(gender)

#Indexing
tu=(10,20,30,40)
print(tu.index(30))

#Count
tu=(10,20,30,40,10,10,20,30,40,10,100)
print(tu.count(30))



#Sum
tu=(10,20,30,40,10,10,20,30,40,10,100)
print(sum(tu))

#ConCatenate 2 tuple's 
tu1=(10,20,30)
tu2=(40,50,60,"Apple")
concatenate_tu=tu1+tu2
print(concatenate_tu)


#Repatation Tuple 
tu=(10,20,30)*3
print(tu)

# or
#Repatation Tuple 
tu=(10,20,30)
print(tu*3)


# Membership Operation

tu=(10,0,20,30,1,0)
print(10 in tu)  #True
print(10 not in tu) #False
