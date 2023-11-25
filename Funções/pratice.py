def take_parameter(parameter):
    print(f"Hello this is: {parameter}")

take_parameter("Josh")

def parameter_one(one):
    print(f"this is: {one}")

def parameter_two(two):
    print(f"this is: {two}")

def parameter_three(three):
    print(f"this is: {three}")

def multiple_parameters(p1, p2, p3):
    parameter_one(p1)
    parameter_two(p2)
    parameter_three(p3)

multiple_parameters("First", "Second", "Third")

def numbers_parameters(num1, num2, num3):
    return num1 + (num2 * num3)

result = numbers_parameters(1,2,3)
print(result)