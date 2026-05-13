adms = []
clientes = []
rebanho = []
estoque_producao = []
op = -99

while op != 0:
    print('\n=== MENU PRINCIPAL ===')
    print('1 - Cadastrar novo Administrador')
    print('2 - Cadastrar novo Cliente')
    print('3 - Realizar Login')
    print('0 - Sair do sistema')
    
    op = int(input('Escolha uma opção: '))

    if op == 1:
        print("\n--- CADASTRO DE ADM ---")
        nome = input('Defina o nome de usuário para o ADM: ')
        senha = input('Defina a senha para este ADM: ')
        numero = input('digite o numero de telefone do ADM: ')
        adms.append([nome, senha, numero])
        print(f'Sucesso: Administrador "{nome}" cadastrado!')

    elif op == 2:
        print("\n--- CADASTRO DE CLIENTE ---")
        nome = input('Defina o nome de usuário para o Cliente: ')
        senha = input('Defina a senha para este Cliente: ')
        numero = input('digite o numero de telefone do Cliente: ')
        clientes.append([nome, senha, numero])
        print(f'Sucesso: Cliente "{nome}" cadastrado!')

    elif op == 3:
        print("\n--- TELA DE ACESSO ---")
        login = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')
        
        achei = False
        
        for a in adms:
            if login == a[0] and senha == a[1]:
                print(f'\n>>> Bem-vindo(a) ADM {login}!')
                achei = True
                op_adms = -99
                while op_adms != 0:
                    print('\n--- MENU DO ADMINISTRADOR ---')
                    print('1 - Listar Clientes cadastrados')
                    print('2 - Gerenciar Rebanho')
                    print('3 - Gerenciar Produção')
                    print('4 - Contato dos Clientes')
                    print('0 - Sair do menu ADM (Logout)')
                    op_adms = int(input('Escolha uma opção: '))
                    
                    if op_adms == 1:
                        print('\n--- CLIENTES CADASTRADOS ---')
                        if not clientes:
                            print('Nenhum cliente cadastrado no sistema.')
                        for c in clientes:
                            print(f'Usuário: {c[0]}')
                            
                    elif op_adms == 2:
                        op_rebanho = -99
                        while op_rebanho != 0:
                            print('\n--- GERENCIAMENTO DE REBANHO ---')
                            print('1 - Cadastrar novo Animal')
                            print('2 - Buscar Animal por ID')
                            print('3 - Atualizar dados de um Animal')
                            print('4 - Remover Animal do sistema')
                            print('0 - Voltar ao Menu do ADM')
                            op_rebanho = int(input('Escolha uma opção: '))
                            
                            if op_rebanho == 1:
                                tipo = input('Digite a espécie/tipo do animal: ')
                                id_animal = input('Digite o número de identificação do animal: ')
                                status = input('Informe o status (lactação, engorda ou venda): ')
                                rebanho.append([id_animal, tipo, status])
                                print('Sucesso: Animal registrado no rebanho!')
                                
                            elif op_rebanho == 2:
                                busca = input('Digite o ID do animal que deseja localizar: ')
                                encontrado = False
                                for animal in rebanho:
                                    if animal[0] == busca:
                                        print(f'>> Animal Localizado: [ID: {animal[0]}, Tipo: {animal[1]}, Status: {animal[2]}]')
                                        encontrado = True
                                if not encontrado: 
                                    print('Aviso: Animal com este ID não foi encontrado.')
                                    
                            elif op_rebanho == 3:
                                busca = input('Digite o ID do animal que deseja atualizar: ')
                                for animal in rebanho:
                                    if animal[0] == busca:
                                        animal[1] = input('Digite o novo tipo do animal: ')
                                        animal[2] = input('Digite o novo status do animal: ')
                                        print('Sucesso: Os dados do animal foram atualizados!')
                                        break
                                        
                            elif op_rebanho == 4:
                                busca = input('Digite o ID do animal que deseja remover: ')
                                achou_rem = False
                                for animal in rebanho:
                                    if animal[0] == busca:
                                        rebanho.remove(animal)
                                        print(f'Sucesso: Animal {busca} removido do sistema.')
                                        achou_rem = True
                                        break
                                if not achou_rem: 
                                    print('Erro: ID não encontrado para remoção.')

                    elif op_adms == 3:
                        op_prod = -99
                        while op_prod != 0: 
                            print('\n--- GERENCIAMENTO DE PRODUÇÃO ---')
                            print('1 - Cadastrar produção de Leite (L)')
                            print('2 - Cadastrar produção de Derivados') 
                            print('0 - Voltar ao Menu do ADM')
                            op_prod = int(input('Escolha uma opção: '))

                            if op_prod == 1:
                                litros = float(input('Quantidade de leite produzida (em litros): '))
                                estoque_producao.append(['Leite', litros])
                                print('Sucesso: Produção de leite registrada!')
                                
                            elif op_prod == 2:
                                nome_p = input('Nome do produto derivado (ex: Queijo): ')
                                peso = float(input('Peso total produzido (kg): '))
                                valor = float(input('Valor de venda por unidade/kg: R$ '))
                                estoque_producao.append([nome_p, peso, valor])
                                print(f'Sucesso: Produto "{nome_p}" adicionado ao estoque!')

                    elif op_adms == 4:
                        print('\n--- CONTATO DOS CLIENTES ---')
                        if not clientes:
                            print('Nenhum cliente cadastrado no sistema.')
                        for c in clientes:
                            print(f'Cliente: {c[0]} - Telefone: {c[2]}')
                break

        if not achei: 
            for c in clientes:
                if login == c[0] and senha == c[1]:
                    print(f'\n>>> Bem-vindo(a) Cliente {login}!')
                    achei = True
                    break
        
        if not achei:
            print('\nErro: Nome de usuário ou senha inválidos.')

    elif op == 0:
        print('\nEncerrando o sistema... Até logo!')
    else:
        print('\nOpção inválida! Tente novamente.')
