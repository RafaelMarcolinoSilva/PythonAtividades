#o white se não existe algo escrito no arquivo ele gera uma escrita
# e se já existe algo escrito ele sobrescreve e substitui

#só escrita usa o w, se precisa atualizar utiliza o a




def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w' )#Através do primeiro atributo da função onde fica o nome do arquivo a ser manipulado, pode-se passar 
    #um endereço de outro diretório onde o arquivo será criado, não somente no diretório corrente do programa
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a' )
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')#separa por enter e o transforma em lista
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')#separa o arquivo por virgula e o transforma em lista
        aluno = lista_notas[0] #separa pelo nome
        notas = lista_notas.pop(0) #elimina a parte dos nomes para deixar somente os números
       # print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int (i) for i in notas])/4 #cria uma função anônima para passar os numeros de caracteres para tipo inteiro
        # e já realiza a soma e  faz a media e passa para uma variável
        print(media(lista_notas)) #imprime o resultado da função que recebe a lista criada
        lista_media.append({aluno:media(lista_notas)}) # cria um dicionário através do nome e da média e adiciona em uma variável
    return lista_media


def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/OneDrive/Desctop')

if __name__ == '__main__':
    copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira Linha.\n')
    #aluno = '\nFelipe, 9,8,7,6'
   # atualizar_arquivo('notas.txt',aluno)
    #ler_arquivo('teste.txt')