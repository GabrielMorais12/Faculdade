adms = []
clientes = []
op = -99

while op != 0:
    print('=== MENU ===')
    print('1 - Cadastrar ADM')
    print('2 - Cadastrar Cliente')
    print('3 - Login')
    print('0 - Sair')
    
    op = int(input('Escolha uma opção: '))

    if op == 1:
        print("--- Cadastro de ADM ---")
        nome = input('Defina o login do ADM: ')
        senha = input('Defina a senha do ADM: ')
        # Salvamos como uma sublista [nome, senha]
        adms.append([nome, senha])
        print('Administrador cadastrado com sucesso!')

    elif op == 2:
        print("--- Cadastro de Cliente ---")
        nome = input('Defina o login do Cliente: ')
        senha = input('Defina a senha do Cliente: ')
        clientes.append([nome, senha])
        print('Cliente cadastrado com sucesso!')

    elif op == 3:
        print("--- Sistema de Login ---")
        login = input('Diga o login: ')
        senha = input('Diga a senha: ')
        
        achei = False
        
        # Procura primeiro na lista de ADMs
        for a in adms:
            if login == a[0] and senha == a[1]:
                print(f'Bem-vindo ADM {login}!')
                achei = True
                break
        
        # Se não achou no ADM, procura nos Clientes
        if not achei:
            for c in clientes:
                if login == c[0] and senha == c[1]:
                    print(f'Bem-vindo Cliente {login}!')
                    achei = True
                    break
        
        if not achei:
            print('Login ou senha incorretos.')

    elif op == 0:
        print('Encerrando programa...')
    else:
        print('Opção inválida!')