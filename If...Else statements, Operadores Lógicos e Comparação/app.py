im_hungry = True
im_thirsty = False
# -> Normal
if im_hungry:
    print("I eat a soup")
else:
    print("I dont eat a soup")

# -> Or 
if im_hungry or im_thirsty:
    print("I drink milkshake")
else:
    print("i dont drink nothing")

# -> And
if im_hungry and im_thirsty:
    print("I drink milkshake")
else:
    print("i dont drink nothing")

# -> Elif

if im_hungry and im_thirsty:
    print("I buy a lanch")
elif not(im_thirsty):
    print("I buy a lanch but i dont take a milkshake")
else:
    print('I dont buy nothing')


# -> Operadores 
num1 = 5
num2 = 10

if num1 == num2:
    print("Number One equals Number Two")
# elif num1 != num2:
#     print("Numeber One is different Number Two")
elif num1 > num2:
    print("Numeber One is more to Number Two")
elif num1 < num2:
    print("Numeber One is smoller to Number Two")

# if num1 <= num2:
#     print("Numeber One is smoller or equal to Number Two")