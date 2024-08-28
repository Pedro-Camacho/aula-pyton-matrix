def linha(largura):
  lista = []
  for i in range(largura):
    lista.append('.')
  return lista

def duas_linhas(largura):
    lista=[]

    for i in range(3):
        lista.append(linha(largura))

    return lista

def sete_linhas(largura):
    lista=[]

    for i in range(7):
        lista.append(linha(largura))

    return lista

def algumas_linhas(largura, altura):
    lista=[]

    for i in range(altura):
        lista.append(linha(largura))

    return lista

def mostrar_lista(lista):
    string=''

    for letra in lista:
        string+=letra
            
    return string

def mostar_listas(lista):
    string=''
    for i in range(len(lista)):
        string += mostrar_lista(lista[i])
        string += '\n'
        
    return string


nome=[['o','l','h','o'],['o','h','l','o']]


def primeira_linha(mapa):
    return mapa[0]


def linha_n(mapa,linha):
    return mapa[linha]


def posicao(mapa,linha,coluna):
    return mapa[linha][coluna]
        
novo_mapa=[['.','.','a'],['b','c','d']]
mapa_antigo = [['.','b','.'],
        ['a','.','.'],
        ['.','.','c'],
        ['.','.','.']]

novo_novo_mapa=[['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]

def coloca(mapa, n_linha, n_coluna, simbolo):
   mapa[n_linha][n_coluna]=simbolo
   return mapa

print(coloca(novo_novo_mapa,1,3,'a'))

