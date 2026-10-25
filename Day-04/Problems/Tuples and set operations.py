# Q9. Create a list and convert it into a tuple and a set.
l=[10,20,30,"A","B"]
print("List:",l)
tu=(tuple(l))
print("Tuple:",tu)

se=(set(l))
print("Set:",se)

# Q11. Try to add new elements to the tuple and set. What differences do you observe?


# We cannot append the values 
tu=(10,20,30,)
tu.append(40)
print(tu)  #Error


# Another way to add to the tuple 
tu=(10,20,30,)
tu1=(40,)
tu2=tu+tu1
print(tu2)


#Set add
s={10,20,30}
s.add(40)
print(s)





















































