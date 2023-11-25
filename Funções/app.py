def take_hamb():
    print('Welcome to Fast Food')

take_hamb()

# -> Using Parameter
def make_burguer(name):
    print(f"hamburguer big for {name}")

def take_botato(size):
    print(f"Botato Size is: {size}")

def take_refri(type, size):
    print(f"Refri is {type} and size: {size}")

def make_combo(name_client, size_botato, type_refri, size_refri):
    make_burguer(name_client)
    take_botato(size_botato)
    take_refri(type_refri, size_refri)

make_combo("Dave", "XL", "Cola", "500ml")

# -> Using Number

def sum_numbers(num1, num2):
    return num1 + num2

result_sum = sum_numbers(1, 5)
print(result_sum)

def numbers_max(list_numbers):
  list_numbers.sort()
  number_max = list_numbers[-1]
  return number_max
   

result_test = numbers_max([2,45,67,8,6,1,3,4545])
print(result_test)