# BIBLIOTECAS----------------------------------------------------------------------
import os
os.system('cls')

import csv

from datetime import datetime
agora = datetime.now()
formatado = agora.strftime('Hoje: %d/%m/%y Horário: %H:%M')

# FUNCOES---------------------------------------------------------------------------
# cadastro
def cadastro():
    print(f'{"Crie Sua Conta":^60}')

    usuario = input('Usuário: ').strip()

    with open('TermPlan/contas.csv', 'r') as contas:
        leitor = csv.reader(contas)

        for linha in leitor:
            if usuario == linha[0]:
                print('Esse usuário já existe!')
                return
            
    senha = input('Senha: ').strip()

    with open('TermPlan/contas.csv', 'a', newline='') as contas:
        escritor = csv.writer(contas)
        escritor.writerow([usuario, senha])

        print('Cadastro realizado com sucesso!')

# login
def login():
    print(f'{"Entrar":^60}')

    usuariologin = input('Usuário: ').strip()

    with open ('TermPlan/contas.csv', 'r') as contas:
        leitor = csv.reader(contas)

        for linha in leitor:
            if usuariologin == linha[0]:
                senhalogin = input('Senha: ').strip()
                if senhalogin == linha[1]:
                    print(f'{"Bem-vindo(a)" + usuariologin + "!":^60}')

                else:
                    print('Senha incorreta. Tente novamente.')
                    return
                
            else:
                print('Usuário não encontrado. Tente novamente.')

# criar evento
def criarevento():
    print(f'{"Criação de Evento\n":^60}')
    diaevento = int(input('Dia (Ex.: 08): '))
    mesevento = int(input('Mês (Ex.: 08): '))
    anoevento = int(input('Ano (Ex.: 2026): '))
    horaevento = int(input('Horário (Ex: 15:30): '))
    nomeevento = input('Nome do evento (Ex.: Médico): ')

    with open ('TermPlan/eventos.csv', 'a', newline='') as eventos:
        escritor = csv.writer(eventos)
        escritor.writerow([diaevento, mesevento, anoevento, horaevento, nomeevento])

        print(f'Evento salvo com sucesso!')

# agenda da semana
def agendadasemana():
    print(f'{"Agenda da Semana".center(60)}')

    diassemana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira',
                   'Sexta-feira', 'Sábado', 'Domingo']
    
    hoje = agora.isoweekday()

    for i, dia in enumerate(diassemana, start=1): # → start=1 faz com que o loop comece em 1
        if i == hoje:
            print(f'→ \033[1;33m{dia}\033[m \033[1;32m(Hoje)\033[m: ')

        else:
            print(f'{dia}: ')

# CODIGO MAIN-----------------------------------------------------------------------

# titulo
print('-=-' * 20)
print(f'{"TermPlan":^60}')
print('-=-' * 20)
print()

# ja tem conta / sim ou nao 
print(f'{'Você já tem uma conta?':^60}')
print('[1] Sim\n[2] Não')

Rjatemconta = int(input('----→ 1 ou 2: '))
print('___' * 20)

# cadastro e login

if Rjatemconta == 2:
    cadastro()

elif Rjatemconta == 1:
    login()
    
# titulo tela de inicio
print('___' * 20)
print(formatado.center(60))

# acessar agenda ou adicionar compromisso

print('\n[1] Acessar agenda\n[2] Criar evento')
Rteladeinicio = int(input('----→ 1 ou 2: '))
print('___' * 20)

if Rteladeinicio == 2:
    criarevento()

elif Rteladeinicio == 1:
    agendadasemana()
















