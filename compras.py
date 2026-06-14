from datetime import date
from utils import limpar_tela
from rich.console import Console
from rich.table import Table
from fpdf import FPDF
import os

console = Console()

def ver_produtos(estoque: list) -> None:
    limpar_tela()
    console.print("[bold yellow]--- PRODUTOS DISPONÍVEIS ---[/bold yellow]\n")
    if not estoque:
        input('  Nenhum produto no estoque. Pressione Enter...')
        return
        
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Vendedor (ADM)")
    table.add_column("Produto")
    table.add_column("Estoque")
    table.add_column("Valor/unid")
    
    for p in estoque:
        if p['quantidade'] > 0:
            qtd_str = f"{p['quantidade']} {'L' if p['produto'] == 'Leite' else 'kg'}"
            val_str = f"R$ {p['valor']:.2f}" if p['valor'] > 0 else "—"
            table.add_row(p['adm'], p['produto'], qtd_str, val_str)
        
    console.print(table)
    input('\n  Pressione Enter...')


def realizar_pedido(usuario: dict, estoque: list, historico: list) -> None:
    limpar_tela()
    print('  --- REALIZAR PEDIDO ---\n')
    nome_prod = input('  Nome do produto: ').strip()
    adm_nome = input('  Nome do vendedor (ADM): ').strip()
    try:
        quantidade = float(input('  Quantidade (L ou kg): '))
    except ValueError:
        input('  Valor inválido. Pressione Enter...')
        return

    for p in estoque:
        if p['produto'].lower() == nome_prod.lower() and p['adm'].lower() == adm_nome.lower():
            if quantidade > p['quantidade']:
                input('  Estoque insuficiente. Pressione Enter...')
                return
            p['quantidade'] -= quantidade
            historico.append({
                'adm': p['adm'],
                'data': date.today().strftime('%d/%m/%Y'),
                'acao': 'venda',
                'item': p['produto'],
                'qtd': quantidade,
                'cliente': usuario['nome']
            })
            if p['produto'] == 'Leite':
                print(f'\n  Pedido de {quantidade} L de leite realizado com sucesso!')
            else:
                total = quantidade * p['valor']
                print(f"\n  Pedido de {quantidade} kg de {p['produto']} realizado!")
                print(f'  Total a pagar: R$ {total:.2f}')
            input('  Pressione Enter...')
            return

    input('  Produto/Vendedor não encontrado no estoque. Pressione Enter...')


def agendar_retirada(usuario: dict, agendamentos: list, estoque: list) -> None:
    limpar_tela()
    print('  --- AGENDAR RETIRADA ---\n')
    adm_nome = input('  Nome do vendedor (ADM): ').strip()
    item = input('  O que vai retirar (ex: Leite, Queijo Coalho, Animais): ').strip()
    data_ret = input('  Data da retirada (ex: 20/06/2026): ').strip()
    hora_ret = input('  Horário (ex: 14:00): ').strip()

    agendamento = {
        'cliente': usuario['nome'],
        'telefone': usuario['telefone'],
        'adm': adm_nome,
        'item': item,
        'data': data_ret,
        'hora': hora_ret
    }
    agendamentos.append(agendamento)

    _gerar_recibo_pdf(agendamento, estoque)


def _gerar_recibo_pdf(ag: dict, estoque: list) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'RECIBO / TICKET DE CARGA', ln=True, align='C')
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, 'Fazenda Sertao', ln=True, align='C')
    pdf.ln(6)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 8, 'DADOS DO CLIENTE', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, f"Nome: {ag['cliente']}", ln=True)
    pdf.cell(0, 6, f"Telefone: {ag['telefone']}", ln=True)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 8, 'AGENDAMENTO', ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 6, f"Vendedor (ADM): {ag['adm']}", ln=True)
    pdf.cell(0, 6, f"Item: {ag['item']}", ln=True)
    pdf.cell(0, 6, f"Data: {ag['data']}  |  Hora: {ag['hora']}", ln=True)
    pdf.ln(4)

    relacionados = [p for p in estoque if ag['item'].lower() in p['produto'].lower() and p['adm'].lower() == ag['adm'].lower()]
    if relacionados:
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 8, 'ITENS DO ESTOQUE DO VENDEDOR (referência)', ln=True)
        pdf.set_font('Helvetica', '', 10)
        for p in relacionados:
            linha = f"  {p['produto']} - {p['quantidade']} {'L' if p['produto'] == 'Leite' else 'kg'}"
            if p['valor'] > 0:
                linha += f"  (R$ {p['valor']:.2f}/unid)"
            pdf.cell(0, 6, linha, ln=True)

    pdf.ln(8)
    pdf.set_font('Helvetica', 'I', 9)
    pdf.cell(0, 6, f"Gerado em: {date.today().strftime('%d/%m/%Y')}", ln=True, align='R')

    nome_arquivo = f"recibo_{ag['cliente']}_{ag['data'].replace('/', '-')}.pdf"
    pdf.output(nome_arquivo)

    console.print(f'\n[bold green]  Agendamento confirmado! Recibo PDF gerado: {nome_arquivo}[/bold green]')
    input('  Pressione Enter para voltar...')