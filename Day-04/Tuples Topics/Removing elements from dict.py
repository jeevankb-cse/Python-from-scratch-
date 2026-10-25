birthday={"Jeevan":"29-07-2005",
          "Vijay":"06-02-1977",
          "Virat":"13-2-2004"
        }
print(birthday)


#pop
print("Poping the jeevan birthday")
birthday.pop("Jeevan")
print(birthday)

#del
print("Deleting the vijay birthday")
del birthday["Vijay"]
print(birthday)

# clear
print("Clearing the dictionary using the clear")
birthday.clear()
print(birthday)

