#módulo em python é cada arquivo .py
# if __name__ == '__main__', significa que se 
#quem chama o arquivo for o próprio arquivo, executa o que está abaixo do main
#caso contrário executoa o que está fora do main



from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8ContadorLetras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora (5,10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'rinoceronte']
    print(contador_letras(lista))
    print(teste())