adms = []
clientes = []
rebanho = []
estoque_producao = []
agendamentos = [] 
op = -99

while op != 0:
    print('\n===MENU PRINCIPAL===')
    print('1 - Cadastrar novo Administrator')
    print('2 - Cadastrar novo Cliente')
    print('3 - Realizar Login')
    print('0 - Sair do sistema')
    
    op = int(input('Escolha uma opção: '))

    if op == 1:
        print("\n===CADASTRO DE ADM===")
        nome = input('Defina o nome de usuário para o ADM: ')
        senha = input('Defina a senha para este ADM: ')
        numero = input('Digite o numero de telefone do ADM: ')
        adms.append({'nome': nome, 'senha': senha, 'telefone': numero})
        print(f'Sucesso: Administrador "{nome}" cadastrado!')

    elif op == 2:
        print("\n===CADASTRO DE CLIENTE===")
        nome = input('Defina o nome de usuário para o Cliente: ')
        senha = input('Defina a senha para este Cliente: ')
        numero = input('Digite o numero de telefone do Cliente: ')
        clientes.append({'nome': nome, 'senha': senha, 'telefone': numero})
        print(f'Sucesso: Cliente "{nome}" cadastrado!')

    elif op == 3:
        print("\n--- TELA DE ACESSO ---")
        login = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')
        
        achei = False
        
        for a in adms:
            if login == a['nome'] and senha == a['senha']:
                print(f'\n>>> Bem-vindo(a) ADM {login}!')
                achei = True
                op_adms = -99
                while op_adms != 0:
                    print('\n===MENU DO ADMINISTRADOR===')
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
                            print(f'Usuário: {c["nome"]}')
                            
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
                                rebanho.append({'id': id_animal, 'tipo': tipo, 'status': status})
                                print('Sucesso: Animal registrado no rebanho!')
                                
                            elif op_rebanho == 2:
                                busca = input('Digite o ID do animal que deseja localizar: ')
                                encontrado = False
                                for animal in rebanho:
                                    if animal['id'] == busca:
                                        print(f">> Animal Localizado: [ID: {animal['id']}, Tipo: {animal['tipo']}, Status: {animal['status']}]")
                                        encontrado = True
                                if not encontrado: 
                                    print('Aviso: Animal com este ID não foi encontrado.')
                                    
                            elif op_rebanho == 3:
                                busca = input('Digite o ID do animal que deseja atualizar: ')
                                for animal in rebanho:
                                    if animal['id'] == busca:
                                        animal['tipo'] = input('Digite o novo tipo do animal: ')
                                        animal['status'] = input('Digite o novo status do animal: ')
                                        print('Sucesso: Os dados do animal foram updated!')
                                        break
                                        
                            elif op_rebanho == 4:
                                busca = input('Digite o ID do animal que deseja remover: ')
                                achou_rem = False
                                for animal in rebanho:
                                    if animal['id'] == busca:
                                        rebanho.remove(animal)
                                        print(f'Sucesso: Animal {busca} removido do sistema.')
                                        achou_rem = True
                                        break
                                if not achou_rem: 
                                    print('Erro: ID não encontrado para remoção.')

                    elif op_adms == 3:
                        op_prod = -99
                        while op_prod != 0: 
                            print('\n===GERENCIAMENTO DE PRODUÇÃO===')
                            print('1 - Cadastrar produção de Leite (L)')
                            print('2 - Cadastrar produção de Derivados') 
                            print('0 - Voltar ao Menu do ADM')
                            op_prod = int(input('Escolha uma opção: '))

                            if op_prod == 1:
                                litros = float(input('Quantidade de leite produzida (em litros): '))
                                estoque_producao.append({'produto': 'Leite', 'quantidade': litros, 'valor': 0.0})
                                print('Sucesso: Production de leite registrada!')
                                
                            elif op_prod == 2:
                                nome_p = input('Nome do produto derivado (ex: Queijo): ')
                                peso = float(input('Peso total produzido (kg): '))
                                valor = float(input('Valor de venda por unidade/kg: R$ '))
                                estoque_producao.append({'produto': nome_p, 'quantidade': peso, 'valor': valor})
                                print(f'Sucesso: Produto "{nome_p}" adicionado ao estoque!')

                    elif op_adms == 4:
                        print('\n--- CONTATO DOS CLIENTES ---')
                        if not clientes:
                            print('Nenhum cliente cadastrado no sistema.')
                        for c in clientes:
                            print(f'Cliente: {c["nome"]} - Telefone: {c["telefone"]}')
                break

        if not achei: 
            for c in clientes:
                if login == c['nome'] and senha == c['senha']:
                    print(f'\n>>> Bem-vindo(a) Cliente {login}!')
                    achei = True
                    op_clientes = -99
                    while op_clientes != 0:
                        print('\n=== MENU DO CLIENTE ===')
                        print('1 - Ver produtos disponíveis para compra')
                        print('2 - Realizar pedido de compra')
                        print('3 - Agendar retirada de produtos')
                        print('4 - Contato do Suporte')
                        print('0 - Sair do menu Cliente (Logout)')
                        op_clientes = int(input('Escolha uma opção: '))

                        if op_clientes == 1:
                            print('\n--- PRODUTOS DISPONÍVEIS ---')
                            if not estoque_producao:
                                print('Nenhum produto disponível no momento.')
                            for p in estoque_producao:
                                if p['produto'] == 'Leite':
                                    print(f"Produto: {p['produto']} - Quantidade: {p['quantidade']} litros")
                                else:
                                    print(f"Produto: {p['produto']} - Quantidade: {p['quantidade']} kg - Valor: R$ {p['valor']:.2f}")
                                    
                        elif op_clientes == 2:
                            nome_prod = input('Digite o nome do produto que deseja comprar: ')
                            quantidade = float(input('Digite a quantidade desejada (litros ou kg): '))
                            encontrado = False
                            for p in estoque_producao:
                                if p['produto'].lower() == nome_prod.lower():
                                    encontrado = True
                                    if p['produto'] == 'Leite':
                                        if quantidade <= p['quantidade']:
                                            p['quantidade'] -= quantidade
                                            print(f'Sucesso: Pedido de {quantidade} litros de leite realizado!')
                                        else:
                                            print('Erro: Quantidade solicitada excede o estoque disponível.')
                                    else:
                                        if quantidade <= p['quantidade']:
                                            valor_total = quantidade * p['valor']
                                            p['quantidade'] -= quantidade
                                            print(f"Sucesso: Pedido de {quantidade} kg de {p['produto']} realizado! Total a pagar: R$ {valor_total:.2f}")
                                        else:
                                            print('Erro: Quantidade solicitada excede o estoque disponível.')
                            if not encontrado:
                                print('Erro: Produto não encontrado no estoque.')

                        elif op_clientes == 3:
                            print('\n===AGENDAR RETIRADA / TRANSPORTE===')
                            item_retirada = input('Digite o que vai retirar (Leite, Queijos ou Animais): ')
                            data_retirada = input('Digite a data da retirada (ex: 20/05/2026): ')
                            hora_retirada = input('Digite o horário da retirada (ex: 14:00): ')
                            agendamentos.append({'cliente': login, 'item': item_retirada, 'data': data_retirada, 'hora': hora_retirada})
                            print(f'Sucesso: Retirada de "{item_retirada}" agendada para {data_retirada} às {hora_retirada}h!')
                        
                        elif op_clientes == 4:
                            print('\n--- CONTATO DO SUPORTE ---')
                            print(c['telefone'] + ' - Suporte Técnico')
        if not achei:
            print('\nErro: Nome de usuário ou senha inválidos.')

    elif op == 0:
        print('\nEncerrando o sistema... Até logo!')
    else:
        print('\nOpção inválida! Tente novamente.')
