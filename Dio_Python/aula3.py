nota1 = float(input("Primeira nota do aluno:\n"))
if nota1 > 10:
    nota1 = float(input("nota incorreta. Digite novamente a primeira nota"))
nota2 = float(input("segunda nota do aluno:\n"))
if nota2 > 10:
    nota2 = float(input("nota incorreta. Digite novamente a segunda nota"))
nota3 = float(input("terceira nota do aluno:\n"))
if nota3 > 10:
    nota3 = float(input("nota incorreta. Digite novamente a terceira nota"))
nota4 = float(input("quarta nota do aluno:\n"))
if nota4 > 10:
    nota4 = float(input("nota incorreta. Digite novamente a quarta nota"))

media = (nota1 + nota2 + nota3 + nota4) /4
#if (nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10):
print(f'média do aluno: {media}')
#else:
 #   print("Alguma nota foi informada incorretamente")


#a = int(input("Entre com um valor: \n"))
#b = int(input("Entre com um valor: \n"))
#resto_a = a % 2
#resto_b = b % 2
#if resto_a == 0 or resto_b == 0:
#    print("Foi digitado um número par!")
#else:
#    print("nenhum número par foi digitado")


#a = int(input('Primeiro valor: \n'))
##b = int(input('Segundo valor: \n'))
#c = int(input('Segundo valor: \n'))

#if a > b and a > c:
#    print(f'O mmaior número é {a}')
#elif b > a and b > c:
#    print(f"O maior número é {b}")
#else:
#    print(f"O maior número é {c}")
#print("Final do Programa")