

# Definindo as chaves em uma tupla
chaves = ('Nome Completo', 'Data de Nascimento', 'CPF', 'Telefone', 'Profissão', 'E-mail', 'Endereço')

# Cadastro do Clientr
usuario = {}
print('Iniciando cadastro....\n')
for chave in chaves:
    usuario[chave] = input(f'Informe o/a {chave}: ')
usuario['Saldo'] = 0.0  # Define o saldo inicial como zero

print('\nUsuário cadastrado com sucesso!')

while True:
    print(f'\n{"-"*10} Banco Senai {"-"*10}')
    print('1 - Listar dados Cadastrados.')
    print('2 - Alterar dados da conta.')
    print('3 - Depositar.')
    print('4 - Sacar.')
    print('5 - Sair do programa.')
    opcao = input('Opção Desejada: ')

    match opcao:
        case '1':
            print(f'\n{"="*10} DADOS DO USUÁRIO {"="*10}\n')
            for chave in chaves:
                print(f'{chave}: {usuario.get(chave)}')
            print(f'Saldo: R$ {usuario["Saldo"]:.2f}')
            print(f'\n{"-"*10}\n')

        case '2':
            print("1 - Nome Completo")
            print("2 - Data de Nascimento")
            print("3 - CPF")
            print("4 - Telefone")
            print("5 - Profissão")
            print("6 - E-mail")
            print("7 - Endereço")
            chave = int(input("Informe o número correspondente ao dado que deseja alterar: ")) - 1
            if 0 <= chave < len(chaves):
                novo_valor = input(f'Informe o novo valor para {chaves[chave]}: ')
                usuario[chaves[chave]] = novo_valor
                print("Dado alterado com sucesso.")
            else:
                print("Chave inválida!")

        case '3':
            try:
                valor = float(input('Informe o valor do depósito: '))
                usuario['Saldo'] += valor
                print(f'Valor de R$ {valor:.2f} depositado com sucesso.')
            except:
                print('Entrada inválida! Informe números corretamente.')

        case '4':
            try:
                valor = float(input('Informe o valor do saque: '))
                if usuario['Saldo'] >= valor:
                    usuario['Saldo'] -= valor
                    print(f'Valor de R$ {valor:.2f} sacado com sucesso.')
                else:
                    print('Saldo insuficiente!')
            except:
                print('Entrada inválida! Informe números corretamente.')

        case '5':
            print('Saindo do programa.')
            break

        case _:
            print('Opção inválida! Tente novamente.')
