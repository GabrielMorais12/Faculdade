import os
import re

def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho() -> None:
    print('--------------------------------------')
    print('           FAZENDA SERTÃO             ')
    print('   Sistema de Gestão Agropecuária     ')
    print('--------------------------------------\n')

def validar_telefone(telefone: str) -> bool:
    padrao = r'^\d{10,11}$'
    return bool(re.match(padrao, telefone))

def validar_senha(senha: str) -> bool:
    return len(senha) >= 6
