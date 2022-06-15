

nota1 = float(input("Primeira nota do aluno:\n"))
while (nota1 < 0 or nota1 > 10):
    nota1 = float(input("nota incorreta. Digite novamente a primeira nota"))
nota2 = float(input("segunda nota do aluno:\n"))
while (nota2 < 0 or nota2 > 10):
    nota2 = float(input("nota incorreta. Digite novamente a segunda nota"))
nota3 = float(input("terceira nota do aluno:\n"))
while (nota3 < 0 or nota3 > 10):
    nota3 = float(input("nota incorreta. Digite novamente a terceira nota"))
nota4 = float(input("quarta nota do aluno:\n"))
while (nota4 < 0 or nota4 > 10):
    nota4 = float(input("nota incorreta. Digite novamente a quarta nota"))

media = (nota1 + nota2 + nota3 + nota4) /4
print(media)
#a = 0
#while a <= 10:
 #   print(a)
  #  a += 1


#for i in range(999):
 #   div = 0
  #  tot = 0
   # for  x in range(1, i + 1):
    #    resto = i % x
     #  # print(x, resto)
      #  if resto == 0:
       #     div += 1
#
 #   if div ==2:
  #      tot =+ 1
   #     print(i)
    #print(tot)



#n = int(input("Entre com um número"))
#div = 0
#for x in range(1, n + 1):
#    resto = n % x
#    print(n, resto)
#    if resto == 0:
#        div += 1

#if div ==2:
#    print(f"Número {n} é primo")
#else:
#    print(f"O número {n} não é primo")