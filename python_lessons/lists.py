#Define a list of names
names = ["Ikuzwe","Alain","Salvador"]

#Adding a new member in the list
names.append("Cedric")
print(names)

#using for loop to display all members
for i in range(len(names)):
    print(i, names[i])

#using sort function to sort the list
names.sort()
print(names)
