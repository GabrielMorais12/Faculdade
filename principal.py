from auth import autenticar_usuario, cadastrar_adm, cadastrar_cliente
from menus import menu_adm, menu_cliente
from utils import limpar_tela, cabecalho

dados = {
    'adms': [],
    'clientes': [],
    'rebanho': [],
    'estoque': [],
    'agendamentos': [],
    'historico': []
}

def main():
    op = -99
    while op != 0:
        limpar_tela()
        cabecalho()
        print('[1] Cadastrar Administrador')
        print('[2] Cadastrar Cliente')
        print('[3] Realizar Login')
        print('[0] Sair do sistema')
        print()

        try:
            op = int(input('  Escolha uma opção: '))
        except ValueError:
            input('  Opção inválida! Pressione Enter para continuar...')
            continue

        if op == 1:
            cadastrar_adm(dados['adms'])
        elif op == 2:
            cadastrar_cliente(dados['clientes'])
        elif op == 3:
            resultado = autenticar_usuario(dados['adms'], dados['clientes'])
            if resultado:
                tipo, usuario = resultado
                if tipo == 'adm':
                    menu_adm(usuario, dados)
                else:
                    menu_cliente(usuario, dados)
            else:
                input('\n  Usuário ou senha inválidos. Pressione Enter...')
        elif op == 0:
            print('\n  Encerrando o sistema...\n')
        else:
            input('\n  Opção inválida! Pressione Enter para continuar...')

if __name__ == '__main__':
    main()
