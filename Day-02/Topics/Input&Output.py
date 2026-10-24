boy_name=input("Enter the name of the boy : ")  #Input
girl_name=input("Enter the name of the girl : ")  #Input
boy_age=int(input("Enter the boy age : "))
girl_age=int(input("Enter the girl age : "))
Age_differnce=boy_age - girl_age
Age_differnce=abs(boy_age - girl_age)   #It's Nothing but modules value(abs)-->Abosulate value  when you give the -50 age happens it give only 50.. 

print(boy_name +" Loves "+  girl_name +" Age_difference is "+ str(Age_differnce))  #Output
print(f"{boy_name} Loves {girl_name}  Age differnce is {Age_differnce}") #Output

