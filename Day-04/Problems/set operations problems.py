# Q5. Create two sets of favorite fruits.
s1={"Mango","Bannana","Apple"}
s2={"Pinepile","Pomogranate","Sapotha"}
print(s1)
print(s2)


# Q6. Find union, intersection, and difference.
# union
s1={1,2,3}
s2={3,4,5}
print(s1|s2)
#intersection
s1={1,2,3}
s2={3,4,5}
print(s1&s2)
#difference
s1={1,2,3}
s2={3,4,5}
print(s1-s2)
print(s2-s1)

# Q7. Add a new fruit to your set.

fruits={"Mango","Bannana","Apple"}
fruits.add("Papaya")
print(fruits)

# Q8. Remove a fruit using remove() and discard().

fruits={"Mango","Bannana","Apple"}
fruits.remove("Mango")
print(fruits)


fruits={"Mango","Bannana","Apple"}
fruits.discard("Apple")
print(fruits)



