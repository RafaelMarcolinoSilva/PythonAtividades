contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro','rinoceronte','canguru']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5,10))
print(subtracao(10,5))

calculadora = {
    'soma': lambda a, b: a +b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a  * b,
    'dividao': lambda a, b: a / b,

}

print(type(calculadora))
soma = calculadora['soma']
multiplicaca = calculadora['multiplicacao']
subtracao = calculadora['subtracao']
divisao = calculadora['dividao']