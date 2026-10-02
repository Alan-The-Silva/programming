full_name = input("what is your full name: ")
print(str(full_name))

birth_year = input("In which year where your born in: ")
print(str(birth_year))

current_year = 2026
age = current_year - int(birth_year)

print(f"Hello {full_name}, you are {age} years old in {current_year}.")
