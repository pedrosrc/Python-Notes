import os

#open("caminho", "r")

# Modes
# r - Leitura
# a- Append / incrementar
# w - write / escrever -> apaga o arquivo e escreve oq foi pedido
# x - create / criar
# r+ - leitura + escrita

arquivo = open("test.txt", "a")
arquivo2 = open("test2.txt", "w")
# arquivo3 = open("test3.text", "x")
arquivo4 = open("test4.txt", "r+")
# -----------READ---------
# print(arquivo.readable())
# print(arquivo.read())
# print(arquivo.readline()) -> Return top list

# lista = arquivo.readlines() -> Transformar o arquivo em uma lista manipulavel

# -----------APPEND---------
# arquivo.write("\nNode\n")
# arquivo.write("JSON\n")
# arquivo.write("Mongo\n")
# -----------WRITE---------
# arquivo2.write("Node\n")
# arquivo2.write("JSON\n")
# arquivo2.write("Mongo\n")
# -----------CREATE---------
# arquivo3.write("Node\n")
# arquivo3.write("JSON\n")
# arquivo3.write("Mongo\n")
# ------REMOVE------
# arquivo3.close()
os.remove("test3.text")

# ------LEITURA+ESCRITA------
# arquivo4.write("Node\n")
# arquivo4.write("JSON\n")
# arquivo4.write("Mongo\n")



arquivo4.close()

arquivo2.close()
arquivo.close()