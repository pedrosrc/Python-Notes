cont = [10]

def ImprimeArvoreRecurs(raiz, nivel):
     if (raiz == None):
        return nivel += cont[0]

# Imprime Filhos à Direita
ImprimeArvoreRecurs(raiz.direita, nivel)
print()
for i in range(cont[0], nivel): 
    print(end=" ")
    print(f"{raiz.chave}<")

# Imprime Filhos à Esquerda
ImprimeArvoreRecurs(raiz.esquerda, nivel)

def ImprimeArvore(raiz):
   ImprimeArvoreRecurs(raiz, 0)