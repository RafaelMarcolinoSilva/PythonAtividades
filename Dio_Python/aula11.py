#procurar pelas exceções do python
lista = [1,10]

try:
    arquivo = open('teste.txt','r')
    texto = arquivo.read()
    divisão = 10 / 1
    numero = lista[1]
    
    
    
except ZeroDivisionError:
    print('Não é possível a realização de divisão por 0')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print(f'erro desconhecido. Erro: {ex}')

else: 
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()