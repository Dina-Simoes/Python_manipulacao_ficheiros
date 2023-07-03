############################################################
#                                                          #
#  9191 - Introdução às Técnicas de Análise de Evidências  #
#                                                          #
#  23/03/2023                              Dina Simões     #
#                                                          #
############################################################


import os               # importa o módulo os
import shutil           # importa o módulo shutil ( neste programa usei para eliminar pastas com ficheiros

while True:
    dir_path = input("Digite o diretório onde deseja trabalhar: ")  # Guarda o caminho do diretório
    if os.path.isdir(dir_path):             # Verifica se o caminho digitado existe
        os.chdir(dir_path)                  # Entra no diretório
        break                       #  sai do loop while e continua a execução do programa
    else:
        print("O diretório não existe.")

while True:                         # menu Listagem de Ficheiros
    print("\nMenu de opções:")
    print("\n===== LISTAGEM DE FICHEIROS =====")
    print("1 - Ficheiros")
    print("2 - Eliminar pasta")
    print("3 - Criar pasta")
    print("4 - Mudar o nome da pasta")
    print("5 - Mudar de diretório")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        while True:             # entra num novo menu (Manipulação de Ficheiros)
            print("\n===== MANIPULAÇÃO DE FICHEIROS =====")
            print("1 - Listar")
            print("2 - Abrir")
            print("3 - Eliminar")
            print("4 - Procurar e contar")
            print("0 - Menu anterior")

            opcao2 = input("\nEScolha uma opção: ")

            if opcao2 == "1":
                print("\n===== LISTAR FICHEIROS =====")
                lista_ficheiros = os.listdir()          # Lista os ficheiros e pastas no diretório atual
                for ficheiro in lista_ficheiros:        # para cada elemento do diretório
                    print(ficheiro)                     # imprime o conteúdo do diretório
                input("Prima ENTER para continuar")

            elif opcao2 == "2":
                print("\n===== ABRIR FICHEIRO =====")
                lista_ficheiros = os.listdir()          # Lista os ficheiros e pastas no diretório atual
                for ficheiro in lista_ficheiros:        # para cada elemento do diretório
                    if ficheiro.endswith('.txt'):       # verifica se é um ficheiro de texto
                        print(ficheiro)
                nome_ficheiro = input("Digite o nome do ficheiro: ")    # pede ao utilizador o nome do ficheiro a abrir
                nome_ficheiro = nome_ficheiro + ".txt"      # acrescenta a extensão no ficheiro
                if os.path.exists(nome_ficheiro):           # verifica se o ficheiro existe
                    with open(nome_ficheiro, "r") as f:     # abre o ficheiro em modo de leitura
                        conteudo = f.read()                 # lê o ficheiro
                        print(conteudo)
                else:
                    print("O ficheiro não existe!")
                input("Prima ENTER para continuar")

            elif opcao2 == "3":
                print("\n===== ELIMINAR FICHEIRO =====")
                lista_ficheiros = os.listdir()          # Lista os ficheiros e pastas no diretório atual
                for ficheiro in lista_ficheiros:        # para cada elemento do diretório
                    if ficheiro.endswith('.txt'):       # verifica se é um ficheiro de texto
                        print(ficheiro)
                nome_ficheiro = input("Digite o nome do ficheiro: ") # pede ao utilizador o nome do ficheiro a eliminar
                nome_ficheiro = nome_ficheiro + ".txt"      # acrescenta a extensão no ficheiro
                if os.path.exists(nome_ficheiro):           # verifica se o ficheiro existe
                    os.remove(nome_ficheiro)                # elimina o ficheiro
                    print("Ficheiro eliminado com sucesso!")
                else:
                    print("O ficheiro não existe!")
                input("Prima ENTER para continuar")

            elif opcao2 == "4":
                print("\n===== PROCURAR E CONTAR =====")
                lista_ficheiros = os.listdir()          # Lista os ficheiros e pastas no diretório atual
                for ficheiro in lista_ficheiros:        # para cada elemento do diretório
                    if ficheiro.endswith('.txt'):       # verifica se é um ficheiro de texto
                        print(ficheiro)                 # mostra os ficheiros que estão dentro das condições
                nome_ficheiro = input("Digite o nome do ficheiro: ")    # pede ao utilizador o nome do ficheiro a abrir
                nome_ficheiro = nome_ficheiro + ".txt"  # acrescenta a extensão no ficheiro
                if os.path.exists(nome_ficheiro):       # verifica se o ficheiro existe
                    with open(nome_ficheiro, "r") as f:     # abre o ficheiro em modo de leitura
                        conteudo = f.read()                 # lê o ficheiro
                        print(conteudo)                     # mostra o conteudo do ficheiro



                input("Prima ENTER para continuar")

            elif opcao2 == "0":
                break           # sai deste loop while (menu manipulação de ficheiros) e volta ao menu anterior

            else:
                # Engloba todas as opções inválidas: letras, caracteres especiais, outros números
                print("Opção inválida!")
                input("Prima ENTER para continuar")


    elif opcao == "2":
        print("===== ELIMINAR PASTA =====")
        pastas = [p for p in os.listdir() if os.path.isdir(p)]      # Faz uma lista das pastas do diretório atual
        if not pastas:                                          # Se não existirem pastas
            print("Não existem pastas no diretório atual.")
        else:
            print("Pastas no diretório atual:")
            for p in pastas:                        # Para as pastas existentes
                print(p)                            # Mostra ao utilizador as pastas existentes
            pasta_eliminar = input("Digite o nome da pasta a eliminar: ")
            if not os.path.isdir(pasta_eliminar):       # se a pasta digitada não existe
                print("A pasta digitada não existe.")
            else:                                       # se a pasta digitada existe
                # quantidade de ficheiros == comprimento da lista de pastas
                qtd_ficheiros = len(os.listdir(pasta_eliminar))
                if qtd_ficheiros > 0:                   # se a pasta tem ficheiros
                    print(f"A pasta {pasta_eliminar} tem {qtd_ficheiros} ficheiros.")
                    confirma = input("Deseja mesmo eliminar a pasta e os seus ficheiros? (S/N) ")
                    if confirma.lower() == "s":     # caso o utilizador digite com minúsculas
                        # o comando rmtree do módulo shutil elimina uma pasta não vazia
                        shutil.rmtree(dir_path + "/" + pasta_eliminar)
                        print(f"A pasta {pasta_eliminar} e os ficheiros foram eliminados com sucesso.")
                else:       # se a pasta a eliminar não contém ficheiros
                    os.rmdir(pasta_eliminar)        # o comando os.rmdir elimina pastas vazias
                    print(f"A pasta {pasta_eliminar} foi eliminada com sucesso.")

    elif opcao == "3":
        print("===== CRIAR PASTA =====")
        pastas = [p for p in os.listdir() if os.path.isdir(p)]      # Faz uma lista das pastas do diretório atual
        print("Pastas no diretório atual:")
        for p in pastas:        # imprime as pastas existentes
            print(p)
        nova_pasta = input("Digite o nome da nova pasta: ")     # pede ao utilizador a nova pasta e guarda numa variável
        if os.path.isdir(nova_pasta):       # se a pasta digitada já existir
            print("A pasta digitada já existe.")
        else:
            os.mkdir(nova_pasta)        # cria a pasta cujo nome foi digitado pelo utilizador
            print(f"A pasta {nova_pasta} foi criada com sucesso.")

    elif opcao == "4":
        print("===== MUDAR O NOME DA PASTA =====")
        pastas = [p for p in os.listdir() if os.path.isdir(p)]      # Faz uma lista das pastas do diretório atual
        print("Pastas no diretório atual:")
        for p in pastas:        # imprime as pastas existentes
            print(p)
        # pede ao utilizador o nome da pasta a renomear
        pasta_renomear = input("Digite o nome da pasta que deseja mudar o nome: ")
        if not os.path.isdir(pasta_renomear):       # verifica se essa pasta existe
            print("A pasta digitada não existe.")
        else:
            # pede ao utilizador o novo nome da pasta a renomear e guarda numa variável
            novo_nome = input("Digite o novo nome da pasta: ")
            os.rename(pasta_renomear, novo_nome)         # os.rename() ==> atribui o novo_nome à pasta_renomer
            print(f"A pasta {pasta_renomear} foi renomeada para {novo_nome} com sucesso!")

    elif opcao == "5":
        print("===== MUDAR DE DIRETÓRIO =====")
        print("Diretório atual:", os.getcwd())      # os.getcwd() ==> Devolve o nome do diretório atual
        novo_diretorio = input("Digite o caminho do novo diretório")        # Guarda o nome do diretório pretendido
        os.chdir(novo_diretorio)                # Muda o diretório onde se está a trabalhar
        print(f"O caminho do novo diretório é {novo_diretorio}" )

    elif opcao == "0":
        print("A SAIR....!")
        break              # sai do programa

    else:
        print("Opção inválida!")       # Engloba todas as opções inválidas: letras, caracteres especiais, outros números
        input("Prima ENTER para continuar")