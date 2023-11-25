products = [
    {id: 12, "name": "Laranja", "price": 3},
    {id: 11, "name": "Abacate", "price": 5},
    {id: 6, "name": "Banana", "price": 7}
]

## Buscando Objeto pelo Nome
print('-------Buscando Objeto pelo Nome---------')
nome_desejado = input('Digite o produto que deseja: ')

for fruta in products:
    if fruta["name"] == nome_desejado:
        print(fruta)
        break

print('-----------------------------------------')

## Inserindo Objeto
print('-------Inserindo Objeto---------')
nameProduct = input('Nome do produto que deseja cadastrar: ')
priceProuct = int(input(('Preço do produto: ')))

products.append({
    id: 13,
    "name" : nameProduct,
    "price": priceProuct
})

print(products)
print('-----------------------------------------')
## Excluindo Objeto
print('-------Excluindo Objeto---------')

productDelete = input("Produto que deseja excluir: ")

for fruta in products:
    if fruta["name"] == productDelete:
        products.remove(fruta)
        break
print(products)
print('-----------------------------------------')