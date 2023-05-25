from variaveis import (TEXT_BEM_VINDO, TEXT_MENU_FILMES, DADOS_CADASTRO, FILMES_SELECIONADOS, LISTA_FILMES, FILMES_ALUGADOS, TEXT_ESTRUTURA_1, TEXT_GENEROS)
import os

def cadastro(nome: str, email: str, senha: str) -> None: # Função de cadastro
    """
    Função que realiza o cadastro das informações informadas através dos inputs.
    """

    # Printa a variavel que contém o texto de bem vindo
    print(TEXT_BEM_VINDO)

    # Variável para criar um objeto dos dados e adiciona-la na lista geral
    dados = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    # Repetição para perguntar ao usuário se quer salvarb as informações informadas
    while True:
        print(f"Seus dados são: ")
        for k, v in dados.items():
            print(f"{k}: {v}")

        opcao_continuar = int(input('Eles conferem? [1]SIM [2]NÃO '))

        #  Condição para somente seguir com o salvamento dos dados 
        if opcao_continuar == 1:
            DADOS_CADASTRO.append(dados)
            break

        #  Condição para ajustes nos dados antes de salvar 
        elif opcao_continuar == 2:
            limpaTela()
            print("-=-= LOCADORA DO GUILHERME =-=-")
            dados['Nome'] = str(input('Digite o seu nome: '))
            dados['Email'] = str(input('Digite o seu email: '))
            dados['senha'] = str(input('Digite a sua senha: '))

            DADOS_CADASTRO.append(dados)
            break

        #  Caso a opção informada não for nem 1 e nem 2 
        else:
            print('Opção inválida!')
        
        
def escolher_filme(): # Função da tabla de escolhas
    """
    Função que permite gerir os filmes da locadora...
    """
    # printanto a variável que tem o texto de menu de filmes disponíveis
    while True:
        limpaTela()
        print(TEXT_MENU_FILMES)

        dados_filmes = {
            'genero': None,
            'filme': None,
            'quantidade': int
        }

        opcao_menu = int(input("Sua escolha: "))

        # Essa estrutura Match trabalha da mesma forma do Swicth Case
        match opcao_menu:
            case 1: # Caso a opção escolhida for comprar filmes
                quantidade_filmes = int(input('Quantos filmes você deseja comprar? '))

                print('Escolha um dos seguintes gêneros: ')

                for c in range(quantidade_filmes):
                    # For usado para percorrer o dicionário de filmes e pegar somente as chaves que são os nomes dos tipos de filmes
                    for indice, genero_filme in enumerate(LISTA_FILMES.keys()):
                        print(f'[ {indice+1}° ] -> {genero_filme}')
                    
                    escolha_genero = int(input("Sua escolha: "))
                    
                    # ESCOLHA DO GENERO DO FILME
                    match escolha_genero:
                        case 1: # Caso o genero escolhido for AÇÃO
                            print(f'Gênero escolhido: AÇÃO\n')
                            print('Filmes disponíveis:')

                            for indice, filme in enumerate(LISTA_FILMES['AÇÃO']):
                                print(f'[ {indice+1}° ] -> {filme}')
                            
                            print('Preço por filme R$25,00')

                            opcao_filme = int(input('Filme escolhido: '))-1

                            dados_filmes = {
                                'genero': "AÇÃO",
                                'filme': LISTA_FILMES['AÇÃO'][opcao_filme],
                                'quantidade': quantidade_filmes,
                                'preco': quantidade_filmes*25
                            }
                            FILMES_SELECIONADOS.append(dados_filmes)

                            print('\nAdiconado com sucesso!')

                        case 2: # Caso o genero escolhido for ROMANCE
                            print(f'Gênero escolhido: ROMANCE\n')
                            print('Filmes disponíveis:')

                            for indice, filme in enumerate(LISTA_FILMES['ROMANCE']):
                                print(f'[ {indice+1}° ] -> {filme}')
                            
                            print('Preço por filme R$25,00')

                            opcao_filme = int(input('Filme escolhido: '))-1
                            
                            dados_filmes = {
                                'genero': "ROMANCE",
                                'filme': LISTA_FILMES['ROMANCE'][opcao_filme],
                                'quantidade': quantidade_filmes,
                                'preco': quantidade_filmes*25
                            }
                            FILMES_SELECIONADOS.append(dados_filmes)

                            print('\nAdiconado com sucesso!')
                            
                        case 3: # Caso o genero escolhido for COMÉDIA
                            print(f'Gênero escolhido: COMÉDIA\n')
                            print('Filmes disponíveis:')

                            for indice, filme in enumerate(LISTA_FILMES['COMÉDIA']):
                                print(f'[ {indice+1}° ] -> {filme}')
                            
                            print('Preço por filme R$25,00')

                            opcao_filme = int(input('Filme escolhido: '))-1
                            
                            dados_filmes = {
                                'genero': "COMÉDIA",
                                'filme': LISTA_FILMES['COMÉDIA'][opcao_filme],
                                'quantidade': quantidade_filmes,
                                'preco': quantidade_filmes*25
                            }
                            FILMES_SELECIONADOS.append(dados_filmes)

                            print('\nAdiconado com sucesso!')
                        
                        case 4: # Caso o genero escolhido for TERROR
                            print(f'Gênero escolhido: TERROR\n')
                            print('Filmes disponíveis:')

                            for indice, filme in enumerate(LISTA_FILMES['TERROR']):
                                print(f'[ {indice+1}° ] -> {filme}')
                            
                            print('Preço por filme R$25,00')

                            opcao_filme = int(input('Filme escolhido: '))-1
                            
                            dados_filmes = {
                                'genero': "TERROR",
                                'filme': LISTA_FILMES['TERROR'][opcao_filme],
                                'quantidade': quantidade_filmes,
                                'preco': quantidade_filmes*25
                            }
                            FILMES_SELECIONADOS.append(dados_filmes)

                            print('\nAdiconado com sucesso!')

                        case _: # Caso a opção escolhida não exista
                            print('Opção de tipo de gênero não existe.')
                escolhaCaso = int(input("[1] Voltar menu [2] Encerrar Programa "))
                if escolhaCaso == 1:
                    continue
                else:
                    break
                
            case 2: # Caso a opção escolhida for alugar filmes
                limpaTela()
                print("-=-=-= Alugar filmes =-=-=-")
                print("Aluguel por dia R$10,00")
                
                quantidade_alugar = int(input("Quantos filmes você deseja alugar? "))
                for c in range(quantidade_alugar):
                    for indice, genero_filme in enumerate(LISTA_FILMES.keys()):
                        print(f'[ {indice+1}° ] -> {genero_filme}')
                        
                    escolha_genero = int(input("Sua escolha: "))
                    
                    match escolha_genero:
                        case 1: # Caso o genero escolhido for AÇÃO
                            print(f'Gênero escolhido: AÇÃO\n')
                            print('Filmes disponíveis:')

                            for indice, filme in enumerate(LISTA_FILMES['AÇÃO']):
                                print(f'[ {indice+1}° ] -> {filme}')
                            
                            print('Preço por aluguel de filme R$10,00')

                            opcao_filme = int(input('Filme escolhido: '))-1
                            quantidade_dias = int(input('Quantidade de dias para alugar: '))

                            dados_filmes = {
                                'genero': "AÇÃO",
                                'filme': LISTA_FILMES['AÇÃO'][opcao_filme],
                                'quantidade': quantidade_alugar,
                                'dias': quantidade_dias,
                                'preco': quantidade_alugar*quantidade_dias*10
                            }
                            FILMES_ALUGADOS.append(dados_filmes)

                            print('\nAdiconado com sucesso!')
                            
                        case 2: # Caso o genero escolhido for ROMANCE
                            print(f'Gênero escolhido: ROMANCE\n')
                            print('Filmes disponíveis:')

                            for indice, filme in enumerate(LISTA_FILMES['ROMANCE']):
                                print(f'[ {indice+1}° ] -> {filme}')
                            
                            print('Preço por aluguel de filme R$10,00')

                            opcao_filme = int(input('Filme escolhido: '))-1
                            quantidade_dias = int(input('Quantidade de dias para alugar: '))

                            dados_filmes = {
                                'genero': "ROMANCE",
                                'filme': LISTA_FILMES['ROMANCE'][opcao_filme],
                                'quantidade': quantidade_alugar,
                                'dias': quantidade_dias,
                                'preco': quantidade_alugar*quantidade_dias*10
                            }
                            FILMES_ALUGADOS.append(dados_filmes)

                            print('\nAdiconado com sucesso!')
                            
                        case 3: # Caso o genero escolhido for COMÉDIA
                            print(f'Gênero escolhido: COMÉDIA\n')
                            print('Filmes disponíveis:')

                            for indice, filme in enumerate(LISTA_FILMES['COMÉDIA']):
                                print(f'[ {indice+1}° ] -> {filme}')
                            
                            print('Preço por aluguel de filme R$10,00')

                            opcao_filme = int(input('Filme escolhido: '))-1
                            quantidade_dias = int(input('Quantidade de dias para alugar: '))

                            dados_filmes = {
                                'genero': "COMÉDIA",
                                'filme': LISTA_FILMES['COMÉDIA'][opcao_filme],
                                'quantidade': quantidade_alugar,
                                'dias': quantidade_dias,
                                'preco': quantidade_alugar*quantidade_dias*10
                            }
                            FILMES_ALUGADOS.append(dados_filmes)

                            print('\nAdiconado com sucesso!')
                            
                        case 4: # Caso o genero escolhido for TERROR
                            print(f'Gênero escolhido: TERROR\n')
                            print('Filmes disponíveis:')

                            for indice, filme in enumerate(LISTA_FILMES['TERROR']):
                                print(f'[ {indice+1}° ] -> {filme}')
                            
                            print('Preço por aluguel de filme R$10,00')

                            opcao_filme = int(input('Filme escolhido: '))-1
                            quantidade_dias = int(input('Quantidade de dias para alugar: '))

                            dados_filmes = {
                                'genero': "TERROR",
                                'filme': LISTA_FILMES['TERROR'][opcao_filme],
                                'quantidade': quantidade_alugar,
                                'dias': quantidade_dias,
                                'preco': quantidade_alugar*quantidade_dias*10
                            }
                            FILMES_ALUGADOS.append(dados_filmes)

                            print('\nAdiconado com sucesso!')
                            
                        case _: # Caso a opção escolhida não exista
                            print('Opção de tipo de gênero não existe.')
                escolhaCaso = int(input("[1] Voltar menu [2] Encerrar Programa "))
                if escolhaCaso == 1:
                    continue
                else:
                    break
                    
            case 3: # Caso a opção escolhida adicionar filmes
                print('-=-=-= Adicionando filmes =-=-=-')
                qt_add_filme = int(input('Quantos filmes você quer adicionar? '))

                for c in range(qt_add_filme):
                    escolha_3 = int(input("[1] Adicionar filme a um gênero já existente "))

                    match escolha_3:
                        case 1:
                            print(TEXT_ESTRUTURA_1)
                            print(TEXT_GENEROS)
                            escolha_add = int(input("Escolha um dos seguintes gêneros: "))
                            
                            match escolha_add:
                                case 1:
                                    LISTA_FILMES["AÇÃO"].append(str(input("Nome do filme: ")))
                                    print('Filme adicionado com sucesso!')
                                case 2:
                                    LISTA_FILMES["ROMANCE"].append(str(input("Nome do filme: ")))
                                    print('Filme adicionado com sucesso!')
                                case 3:
                                    LISTA_FILMES["COMÉDIA"].append(str(input("Nome do filme: ")))
                                    print('Filme adicionado com sucesso!')
                                case 4:
                                    LISTA_FILMES["TERROR"].append(str(input("Nome do filme: ")))
                                    print('Filme adicionado com sucesso!')
                                
                
            case _: # Caso for inserida uma opção inválida
                print("Opção Inválida")
        escolhaFinal = int(input("[1] Encerrar [2] Voltar Menu "))
        if escolhaFinal == 1:
            break
    print('-='*22)
    for filme in FILMES_SELECIONADOS:
        print(f'Filmes comprados: {filme["filme"]}')
    print('-='*22)
    for filme in FILMES_ALUGADOS:
        print(f'Filmes alugados: {filme["filme"]}')
    print('-='*22)
    print(f"Total a pagar (FILMES COMPRADOS): R${len(FILMES_SELECIONADOS) * 25},00")
    print(f"Total a pagar (FILMES ALUGADOS): R${quantidade_alugar*quantidade_dias*10},00")
    
def mostrar_dados():
    print(f'Contas cadastradas: {DADOS_CADASTRO}')
    print(f'Filmes escolhidos: {FILMES_SELECIONADOS}')
   

def limpaTela():
    os.system("cls")