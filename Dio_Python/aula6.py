#conjunto em pytho também é feito com chaves
# a diferença é que não tem a representação
# de chave e valor como no dicionário
# não permite duplicidade, e só se permite adicionar um elemento por vez
#set representa o nome conjunto

conjunto = {1,2,3,4,5}
conjunto2 = {6,7,8,9,2,4}

conjunto_uniao = conjunto.union(conjunto2)
print(f'União:{conjunto_uniao}')

conjunto_interseccao = conjunto.intersection(conjunto2)
print(f'Intersecção:{conjunto_interseccao}')

conjunto_diferenca = conjunto.difference(conjunto2)
print(f'Conjunto da primeira diferença: {conjunto_diferenca}')
#primeira diferença mostra o que está no conjunto 1 e não está no conjunto 2
conjunto_diferenca2 = conjunto2.difference(conjunto)
#segunda diferença mostra o que está no cojunto 2 mas não está no conjunto 1
print(f'Conjunto da seguna diferença: {conjunto_diferenca2}')

conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print(f'Diferencça simétrica: {conjunto_dif_simetrica}')

conjunto_a = {1, 2, 3 }

conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b) #comando issubset returna um true or false para saber se é subconjunto
print(f'Conjunto subset:{conjunto_subset}')#comando issuperset também retorna um true or false para saber se pertence ao superconjunto

lista = ['cachorro','cachorro', 'gato','gato','elefante' ]
conjunto_animais = set(lista)
print(conjunto_animais)
#conjunto = {1,5,2,6,1,5,2,6}
#conjunto.add(7)
#print(conjunto)
# 
