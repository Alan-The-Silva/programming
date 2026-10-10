# Ask the users weight in either lbs or kgs
weight = int(input("Enter your weight: "))
convert = input("(L)bs or (K)g: ")

# And then convert it to kilograms or pounds
lbs = 0.45359237
kgs = 2.20462

# Lastly give the converted output to the user 
if convert.lower() == "k":
    lb = weight * kgs
    print(f"You are {lb} lbs.")

elif convert.lower() == "l":
    kg = weight * lbs
    print(f"You are {kg} kg.")

else:
    print("Invalid input please try again.")
