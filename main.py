from func import cadastro, escolher_filme, mostrar_dados, limpaTela

# Estrutura que referencia o arquivo principal do projeto
if __name__ == '__main__':
    
    while True:   # Loop para o cadastro
        print("-=-= LOCADORA DO GUILHERME =-=-")
        nome = str(input('Digite o seu nome: '))
        if nome == '':  # Caso o Usuário não digite nada
            limpaTela()
            continue
        else: 
            break
    while True:   # Loop para o cadastro
        email = str(input('Digite o seu email: '))      
        if email == '':
            limpaTela()
            print("-=-= LOCADORA DO GUILHERME =-=-")
            print(f'Digite o seu nome: {nome}')
            continue
        else: 
            break
    while True:   # Loop para o cadastro
        senha = str(input('Digite a sua senha: '))
        if senha == '':
            limpaTela()
            print("-=-= LOCADORA DO GUILHERME =-=-")
            print(f'Digite o seu nome: {nome}')
            print(f'Digite o seu email: {email}')
            continue
        else: 
            break
    
    # +++++++++++++++++++++++++++++++++ 
    cadastro(nome, email, senha)
    escolher_filme()    # Chamar funções
    mostrar_dados()
    # +++++++++++++++++++++++++++++++++ #
