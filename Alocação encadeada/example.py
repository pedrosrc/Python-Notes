## Busca em listas em alocação encadeada

def busca(self, k):
    noAtual = self.head
    if noAtual.chave == k:
        return noAtual
    while noAtual.prox != None:
        noAtual = noAtual.prox
        if noAtual.chave == k:
            return noAtual
    return None
        