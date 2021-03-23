#verificação se o arquivo existe
def verificaArquivo (arquivo):
    try:
        a = open(arquivo, "rt")
        a.close()
    except :
        print("Erro... não foi possivel encontrar arquivo")
        return False
    else:
        return True



#Criação do arquivo
def criacaoArquivo (arquivo):
    try:
        a = open(arquivo, 'wt+')
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso...')



#Cadastro de itens
def cadastro (arquivo, jogo, videogame):
    try:
       a = open(arquivo, 'at')
    except:
        print("Erro ao cadastrar")
    else:
        a.write('{}:{}'.format(jogo,videogame))
    finally:
        a.close()


#Listar
def listar (arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        "Erro na listagem do arquivo"
    else:
        print(a.read())
    finally:
        a.close()



#Aqruivo princial que será utilizado
arquivoPrincipal = 'arquivoPrincipal.txt'



#Verificação da existencia do arquivo /ou criação do arquivo
if verificaArquivo(arquivoPrincipal) == True:
    print("Arquivo encontrado...")
else:
 criacaoArquivo(arquivoPrincipal)
 print('Arquivo {} criado com sucesso'.format(arquivoPrincipal))


#Criar Menu (Cadastrar, Listar e encerrar)
while True:
    print('Menu')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Encerrar')
    resultado = int(input("Qual opção? "))

    if resultado == 1:
        print('Cadastrar selecionado...')
        jogo = input("Qual o nome do jogo?")
        videogame = input('Qual o nome do videogame? ')
        cadastro(arquivoPrincipal,jogo, videogame)

    elif resultado == 2:
        print('Listar selecionado...')
        listar(arquivoPrincipal)

    elif resultado == 3:
        print('Encerrando...')
        break

    elif resultado != 1 and 2 and 3:
        print('Encerrando...')
        break
