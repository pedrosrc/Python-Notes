#-> Sets
# São listas desordenadas, que não aceitam valores duplicados nem modificaçõoes
# apenas inserção e remoção

colors = {"Blue", "Red", "Green"}
colors.add("Yellow")
colors.remove("Red")
print(colors)

colorsDuplicate = {"Blue", "Red", "Green", "Red"}
print(colorsDuplicate)