#In python it is possible to nest
#Together different types of data structures
#for example here we are nesting togeter
#list and dictionary

people = [
    {"name":"Alan", "house":"Gasabo"},
    {"name":"Evan", "house":"Masaka"},
    {"name":"Ben", "house":"Nyanza"}
]

people.sort(key=lambda person: person["name"])

print(people)