import os #importa o módulo ou biblioteca os
#(integra os programas e recursos do S.O)

print("#" * 60) #imprime o # 60 vezes

ip_ou_host = input("Digite o IP ou host a ser verificado:\n")# variável que vai receber um valor do usuário
print("-" * 60)#imprime o - 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host))#chamando o system da biblioteca os - comando ping -n - numero de pacotes que serão 6 {}
print("-" * 60)#imprime o - 60 vezes