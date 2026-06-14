from datetime import date
from utils import limpar_tela
from rich.console import Console
from rich.table import Table

console = Console()

def cadastrar_animal(usuario: dict, rebanho: list) -> None:
    limpar_tela()
    print('  --- CADASTRAR ANIMAL ---\n')
    brinco = input('  Número do brinco (ID): ').strip()
    
    meus_animais = [a for a in rebanho if a['adm'] == usuario['nome']]
    if any(a['brinco'] == brinco for a in meus_animais):
        input(f'  Animal com brinco "{brinco}" já existe no seu rebanho. Pressione Enter...')
        return
        
    tipo = input('  Espécie/tipo (Bovino, Caprino...): ').strip()
    status = input('  Status (lactação / engorda / venda): ').strip()
    try:
        peso = float(input('  Peso (kg): '))
    except ValueError:
        peso = 0.0
    rebanho.append({'adm': usuario['nome'], 'brinco': brinco, 'tipo': tipo, 'status': status, 'peso': peso})
    input(f'\n  Animal {brinco} registrado! Pressione Enter...')


def buscar_animal(usuario: dict, rebanho: list) -> None:
    limpar_tela()
    print('  --- BUSCAR ANIMAL ---\n')
    busca = input('  ID (brinco) do animal: ').strip()
    for a in rebanho:
        if a['adm'] == usuario['nome'] and a['brinco'] == busca:
            print(f"\n  Encontrado: brinco={a['brinco']}, tipo={a['tipo']}, status={a['status']}, peso={a['peso']} kg")
            input('\n  Pressione Enter...')
            return
    input('  Animal não encontrado no seu rebanho. Pressione Enter...')


def atualizar_animal(usuario: dict, rebanho: list) -> None:
    limpar_tela()
    print('  --- ATUALIZAR ANIMAL ---\n')
    busca = input('  ID (brinco) do animal a atualizar: ').strip()
    for a in rebanho:
        if a['adm'] == usuario['nome'] and a['brinco'] == busca:
            a['tipo'] = input(f"  Novo tipo [{a['tipo']}]: ").strip() or a['tipo']
            a['status'] = input(f"  Novo status [{a['status']}]: ").strip() or a['status']
            try:
                a['peso'] = float(input(f"  Novo peso [{a['peso']}]: ") or a['peso'])
            except ValueError:
                pass
            input('  Animal atualizado! Pressione Enter...')
            return
    input('  Animal não encontrado no seu rebanho. Pressione Enter...')


def remover_animal(usuario: dict, rebanho: list) -> None:
    limpar_tela()
    print('  --- REMOVER ANIMAL ---\n')
    busca = input('  ID (brinco) do animal a remover: ').strip()
    for a in rebanho:
        if a['adm'] == usuario['nome'] and a['brinco'] == busca:
            rebanho.remove(a)
            input(f'  Animal {busca} removido. Pressione Enter...')
            return
    input('  Animal não encontrado no seu rebanho. Pressione Enter...')


def registrar_leite(usuario: dict, estoque: list, historico: list) -> None:
    limpar_tela()
    print('  --- REGISTRAR LEITE ---\n')
    try:
        litros = float(input('  Litros produzidos: '))
    except ValueError:
        input('  Valor inválido. Pressione Enter...')
        return
        
    for p in estoque:
        if p['adm'] == usuario['nome'] and p['produto'] == 'Leite':
            p['quantidade'] += litros
            break
    else:
        estoque.append({'adm': usuario['nome'], 'produto': 'Leite', 'quantidade': litros, 'valor': 0.0})
        
    historico.append({
        'adm': usuario['nome'],
        'data': str(date.today().strftime('%d/%m/%Y')),
        'acao': 'produção',
        'item': 'Leite',
        'qtd': litros,
        'cliente': '-'
    })
    input(f'  {litros} L de leite adicionados ao estoque. Pressione Enter...')


def registrar_derivado(usuario: dict, estoque: list, historico: list) -> None:
    limpar_tela()
    print('  --- REGISTRAR DERIVADO ---\n')
    nome = input('  Nome do derivado (ex: Queijo Coalho): ').strip()
    try:
        peso = float(input('  Quantidade (kg): '))
        valor = float(input('  Valor por kg: R$ '))
    except ValueError:
        input('  Valor inválido. Pressione Enter...')
        return
        
    for p in estoque:
        if p['adm'] == usuario['nome'] and p['produto'] == nome:
            p['quantidade'] += peso
            if valor > 0:
                p['valor'] = valor
            break
    else:
        estoque.append({'adm': usuario['nome'], 'produto': nome, 'quantidade': peso, 'valor': valor})
        
    historico.append({
        'adm': usuario['nome'],
        'data': str(date.today().strftime('%d/%m/%Y')),
        'acao': 'produção',
        'item': nome,
        'qtd': peso,
        'cliente': '-'
    })
    input(f'  "{nome}" adicionado ao estoque. Pressione Enter...')


def gerar_dashboard(usuario: dict, rebanho: list, estoque: list) -> None:
    limpar_tela()
    console.print(f"[bold yellow]--- RELATÓRIO GERAL DA FAZENDA ({usuario['nome']}) ---[/bold yellow]\n")

    meus_animais = [a for a in rebanho if a['adm'] == usuario['nome']]
    contagem: dict = {}
    for a in meus_animais:
        contagem[a['tipo']] = contagem.get(a['tipo'], 0) + 1

    console.print(f"[bold cyan]Total de animais: {len(meus_animais)}[/bold cyan]")
    if contagem:
        table_rebanho = Table(show_header=True, header_style="bold magenta")
        table_rebanho.add_column("Espécie")
        table_rebanho.add_column("Quantidade")
        for tipo, qtd in contagem.items():
            table_rebanho.add_row(tipo, str(qtd))
        console.print(table_rebanho)
    else:
        console.print("(sem animais cadastrados)")

    meu_estoque = [p for p in estoque if p['adm'] == usuario['nome']]
    total_leite = sum(p['quantidade'] for p in meu_estoque if p['produto'] == 'Leite')
    derivados = [p for p in meu_estoque if p['produto'] != 'Leite']
    
    console.print(f"\n[bold cyan]Leite em estoque: {total_leite:.1f} L[/bold cyan]")
    if derivados:
        table_estoque = Table(show_header=True, header_style="bold green")
        table_estoque.add_column("Derivado")
        table_estoque.add_column("Quantidade")
        table_estoque.add_column("Valor/kg")
        for p in derivados:
            table_estoque.add_row(p['produto'], f"{p['quantidade']} kg", f"R$ {p['valor']:.2f}")
        console.print(table_estoque)
    else:
        console.print("(sem derivados em estoque)")

    input('\n  Pressione Enter para voltar...')


def ver_historico(usuario: dict, historico: list) -> None:
    limpar_tela()
    console.print("[bold yellow]--- HISTÓRICO DE MOVIMENTAÇÕES ---[/bold yellow]\n")
    
    meu_historico = [h for h in historico if h['adm'] == usuario['nome']]
    if not meu_historico:
        input('  Nenhuma movimentação registrada. Pressione Enter...')
        return
        
    table_hist = Table(show_header=True, header_style="bold cyan")
    table_hist.add_column("Data")
    table_hist.add_column("Ação")
    table_hist.add_column("Item")
    table_hist.add_column("Qtd")
    table_hist.add_column("Cliente")
    
    for h in meu_historico:
        table_hist.add_row(h['data'], h['acao'], h['item'], str(h['qtd']), h.get('cliente', '-'))
        
    console.print(table_hist)
    input('\n  Pressione Enter para voltar...')
