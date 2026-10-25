#Add
s={1,2,3}
s.add(4)
print(s)

#Remove
s={10,20,30}
s.remove(20)
s.remove(220) #Error
print(s)

#Discard
s={1,2,33}
s.discard(12)  #No error
s.discard(1) 
print(s)

#Pop -->Random Value na pop maduthi
s={10,20,30,40,50}
s.pop()
print(s)

#Clear
s={1,2,3,"Apple"}
s.clear()
print(s)