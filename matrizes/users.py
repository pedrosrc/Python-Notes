## Headquarter Basic
friends = [["John", 25, "Dev"], ["Maria", 23, "QA"], ["Dave", 28, "DevOps"]]
print(friends)

## Adding new user
friends.append(["Clau", 22, "DevFront"])
print(friends)

## Adding location in user by index
friends[3].append("Fortaleza")
print(friends)

## Removing location in user
friends[3].remove("Fortaleza")
print(friends)

## Removing user using index
friends.pop(0)
print(friends)

## Looping
for x in friends: 
    print(x)