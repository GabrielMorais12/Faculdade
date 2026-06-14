from utils import limpar_tela
from fazenda import (
    cadastrar_animal, buscar_animal, atualizar_animal, remover_animal,
    registrar_leite, registrar_derivado, gerar_dashboard, ver_historico
)
from compras import ver_produtos, realizar_pedido, agendar_retirada
from rich.console import Console

console = Console()

def menu_adm(usuario: dict, dados: dict) -> None:
    op = -99
    while op != 0:
        limpar_tela()
        nome = usuario['nome']
        console.print(f'[bold green]  Bem-vindo(a), ADM {nome}![/bold green]')
        print('  --- MENU DO ADMINISTRADOR ---')
        print('  [1] Listar Clientes')
        print('  [2] Gerenciar Meu Rebanho')
        print('  [3] Gerenciar Minha Produção')
        print('  [4] Contato dos Clientes')
        print('  [5] Meu Dashboard / Relatório Geral')
        print('  [6] Meu Histórico de Movimentações')
        print('  [0] Logout')
        print()

        try:
            op = int(input('  Escolha: '))
        except ValueError:
            continue

        if op == 1:
            _listar_clientes(dados['clientes'])
        elif op == 2:
            _menu_rebanho(usuario, dados['rebanho'])
        elif op == 3:
            _menu_producao(usuario, dados['estoque'], dados['historico'])
        elif op == 4:
            _contato_clientes(dados['clientes'])
        elif op == 5:
            gerar_dashboard(usuario, dados['rebanho'], dados['estoque'])
        elif op == 6:
            ver_historico(usuario, dados['historico'])


def _listar_clientes(clientes: list) -> None:
    limpar_tela()
    print('  --- CLIENTES CADASTRADOS ---\n')
    if not clientes:
        input('  Nenhum cliente cadastrado. Pressione Enter...')
        return
    for c in clientes:
        print(f"  • {c['nome']} (Cidade: {c.get('cidade', '-')}/{c.get('uf', '-')})")
    input('\n  Pressione Enter...')


def _contato_clientes(clientes: list) -> None:
    limpar_tela()
    print('  --- CONTATO DOS CLIENTES ---\n')
    if not clientes:
        input('  Nenhum cliente cadastrado. Pressione Enter...')
        return
    for c in clientes:
        print(f"  {c['nome']} — {c['telefone']}")
    input('\n  Pressione Enter...')


def _menu_rebanho(usuario: dict, rebanho: list) -> None:
    op = -99
    while op != 0:
        limpar_tela()
        print('  --- GERENCIAR MEU REBANHO ---')
        print('  [1] Cadastrar animal')
        print('  [2] Buscar animal por brinco')
        print('  [3] Atualizar animal')
        print('  [4] Remover animal')
        print('  [0] Voltar')
        try:
            op = int(input('  Escolha: '))
        except ValueError:
            continue

        if op == 1:
            cadastrar_animal(usuario, rebanho)
        elif op == 2:
            buscar_animal(usuario, rebanho)
        elif op == 3:
            atualizar_animal(usuario, rebanho)
        elif op == 4:
            remover_animal(usuario, rebanho)


def _menu_producao(usuario: dict, estoque: list, historico: list) -> None:
    op = -99
    while op != 0:
        limpar_tela()
        print('  --- GERENCIAR MINHA PRODUÇÃO ---')
        print('  [1] Registrar produção de Leite')
        print('  [2] Registrar produção de Derivados')
        print('  [0] Voltar')
        try:
            op = int(input('  Escolha: '))
        except ValueError:
            continue

        if op == 1:
            registrar_leite(usuario, estoque, historico)
        elif op == 2:
            registrar_derivado(usuario, estoque, historico)





def menu_cliente(usuario: dict, dados: dict) -> None:
    op = -99
    while op != 0:
        limpar_tela()
        nome = usuario['nome']
        console.print(f'[bold cyan]  Bem-vindo(a), {nome}![/bold cyan]')
        print('  --- MENU DO CLIENTE ---')
        print('  [1] Ver produtos disponíveis')
        print('  [2] Realizar pedido de compra')
        print('  [3] Agendar retirada / gerar recibo')
        print('  [4] Contato do suporte')
        print('  [0] Logout')
        print()

        try:
            op = int(input('  Escolha: '))
        except ValueError:
            continue

        if op == 1:
            ver_produtos(dados['estoque'])
        elif op == 2:
            realizar_pedido(usuario, dados['estoque'], dados['historico'])
        elif op == 3:
            agendar_retirada(usuario, dados['agendamentos'], dados['estoque'])
        elif op == 4:
            print(f"\n  Suporte: {usuario['telefone']}")
            input('  Pressione Enter...')
