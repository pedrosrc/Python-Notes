family = ["Jack", "Thomas", "Abdul", "Rakim"] 

# print(family.index("Jack")) -> Return Index according to parameter
# print(family.count("Jack")) -> Return quantity "Jack" in list
# print(family[0]) -> Return Family Index
# print(family[-3]) -> Return Family Index Back for Front
# print(family[1:]) -> Return Family index 1 and next
# print(family[1:3]) -> Return Family index 1 to 3

# -> Modified Value
family[3] = "Rocky" 

# -> Add a value in list
family.append("Dog")

# -> Add a list in list
family.extend(["Kanye", "Kid Cudi"])

# -> Add a value according to parameter
family.insert(1,"Tyla")

#-> Remove last value
family.pop()

# -> Remove value according to parameter
family.remove("Jack")

print(family)

family_age = [23,15,16,17,3, 42]

# family_age.sort() -> Return list in order crescent
# family_age.reverse() -> Return list in order descending


# -> Copy in new variable
family2 = family.copy()

# -> Create a Tuple
# Tuples is ( )
cod = (23,24,25)