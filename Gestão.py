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
        
        
        for a in adms:
            if login == a[0] and senha == a[1]:
                print(f'Bem-vindo ADM {login}!')
                achei = True
                op_adms = -99
                while op_adms != 0:
                    print('=== Menu do ADM ===')
                    print('1 - Ver clientes cadastrados')
                    print('2 - Gerencia Rebanho')
                    print('0 - Sair do menu do ADM')
                    op_adms = int(input('Escolha uma opção: '))
                    
                    if op_adms == 1:
                        print('Clientes cadastrados:')
                        for c in clientes:
                            print(f'- {c[0]}')  
                    elif op_adms == 2:
                        print('===Gerenciando rebanho===')
                        print('1 - Cadastrar Animal')
                        print('2 - Buscar Animal')
                        print('3 - Atualizar Animal')
                        print('4 - Remover Animal')
                        print('0 - Voltar ao menu do ADM')
                        op_rebanho = int(input('Escolha uma opção: '))
                        if op_rebanho == 1:
                            print('Cadastrando animal...')
                            
                        elif op_rebanho == 2:
                            print('Buscando animal...')
                            
                        elif op_rebanho == 3:
                            print('Atualizando animal...')
                            
                        elif op_rebanho == 4:
                            print('Removendo animal...')
                            
                        elif op_rebanho == 0:
                            print('Voltando ao menu do ADM...')
                        else:
                            print('Opção inválida no menu de rebanho!')
        
        
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

