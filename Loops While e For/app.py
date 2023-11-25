# -> Using WHILE
example = 1

# while example < 10:
#     print(example)
#     example += 1

# -> Using FOR
people = ["Deck", "Dave", "Delay"]

# for name in people:
#     print(name)

# for name in range(3):
#     print(name)

# for name in range(len(people)):
#     print(people[name], name)

numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for column in numbers:
    # print(column)
    for line in column:
        print(line)