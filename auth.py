import requests
from utils import limpar_tela, validar_telefone, validar_senha

def cadastrar_adm(adms: list) -> None:
    limpar_tela()
    print('  --- CADASTRO DE ADMINISTRADOR ---\n')
    nome = input('  Nome de usuário: ').strip()
    if any(a['nome'] == nome for a in adms):
        input(f'\n  Erro: usuário "{nome}" já existe. Pressione Enter...')
        return
    
    senha = input('  Senha (mínimo 6 caracteres): ').strip()
    if not validar_senha(senha):
        input('  Erro: Senha muito curta. Pressione Enter...')
        return
        
    telefone = input('  Telefone (apenas números, 10 ou 11 dígitos): ').strip()
    if not validar_telefone(telefone):
        input('  Erro: Formato de telefone inválido. Pressione Enter...')
        return
        
    cep = input('  CEP (apenas números): ').strip()
    cidade, uf = "Desconhecido", "Desconhecido"
    if cep.isdigit() and len(cep) == 8:
        try:
            resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/', timeout=5)
            if resposta.status_code == 200:
                dados_cep = resposta.json()
                if 'erro' not in dados_cep:
                    cidade = dados_cep.get('localidade', 'Desconhecido')
                    uf = dados_cep.get('uf', 'Desconhecido')
                    print(f'  Localidade encontrada: {cidade} - {uf}')
        except Exception:
            print('  Aviso: Não foi possível buscar o CEP no momento.')

    adms.append({'nome': nome, 'senha': senha, 'telefone': telefone, 'cidade': cidade, 'uf': uf})
    input(f'\n  Administrador "{nome}" cadastrado com sucesso! Pressione Enter...')

def cadastrar_cliente(clientes: list) -> None:
    limpar_tela()
    print('  --- CADASTRO DE CLIENTE ---\n')
    nome = input('  Nome de usuário: ').strip()
    if any(c['nome'] == nome for c in clientes):
        input(f'\n  Erro: usuário "{nome}" já existe. Pressione Enter...')
        return
        
    senha = input('  Senha (mínimo 6 caracteres): ').strip()
    if not validar_senha(senha):
        input('  Erro: Senha muito curta. Pressione Enter...')
        return
        
    telefone = input('  Telefone (apenas números, 10 ou 11 dígitos): ').strip()
    if not validar_telefone(telefone):
        input('  Erro: Formato de telefone inválido. Pressione Enter...')
        return
        
    cep = input('  CEP (apenas números): ').strip()
    cidade, uf = "Desconhecido", "Desconhecido"
    if cep.isdigit() and len(cep) == 8:
        try:
            resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/', timeout=5)
            if resposta.status_code == 200:
                dados_cep = resposta.json()
                if 'erro' not in dados_cep:
                    cidade = dados_cep.get('localidade', 'Desconhecido')
                    uf = dados_cep.get('uf', 'Desconhecido')
                    print(f'  Localidade encontrada: {cidade} - {uf}')
        except Exception:
            print('  Aviso: Não foi possível buscar o CEP no momento.')

    clientes.append({'nome': nome, 'senha': senha, 'telefone': telefone, 'cidade': cidade, 'uf': uf})
    input(f'\n  Cliente "{nome}" cadastrado com sucesso! Pressione Enter...')

def autenticar_usuario(adms: list, clientes: list):
    limpar_tela()
    print('  --- LOGIN ---\n')
    login = input('  Usuário: ').strip()
    senha = input('  Senha: ').strip()

    for a in adms:
        if a['nome'] == login and a['senha'] == senha:
            return ('adm', a)

    for c in clientes:
        if c['nome'] == login and c['senha'] == senha:
            return ('cliente', c)

    return None
