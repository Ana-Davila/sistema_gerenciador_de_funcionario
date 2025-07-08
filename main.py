#Mensagem de boas vindas
print('Sistema de RH-Cadastro de Funcionários da Aluna Ana Davila Kulek')

lista_funcionarios = [] #Lista para armazenar todos os funcionários
id_global = 5195946 #Id inicial baseado no meu RU

#Função para cadastrar novo funcionário
def cadastrar_funcionario(id1):
    nome1 = input('Qual o nome do funcinário? ')
    setor1 = input('Qual o setor? ')
    salario1 = float(input('Qual é o salário? '))

    funcionario= {'id': id1, 'nome': nome1, 'setor': setor1, 'salário': salario1}
    lista_funcionarios.append(funcionario.copy())
    print(f'Funcionário cadastrado com id: {id1}')

#Função para consultar funcionário
def consultar_funcionario():
    while True:
        print('1. Consultar Todos \n 2. Consultar por Id \n 3. Consultar por Setor \n 4. Retornar ao menu: ')
        opc= input('>>>')
        if(opc == '1'): # Consultar todos os funcionário
            for funcionario in lista_funcionarios:
                for chave in funcionario:
                    print(f'{chave}: {funcionario[chave]}')

        elif(opc == '2'): #Consultar por ID
            id_informado= int(input('Informe o id a ser buscado'))
            for funcionario in lista_funcionarios:
                if (funcionario['id'] == id_informado):
                    for chave in funcionario:
                        print(f'{chave}: {funcionario[chave]}')
                    break
        
        elif (opc == '3'): #Consultar por setor
            setor_informado = input('Informe o Setor a ser buscado: ')
            for funcionario in lista_funcionarios:
                if funcionario['setor'].lower() == setor_informado.lower():
                    for chave in funcionario:
                        print(f'{chave}: {funcionario[chave]}')

        elif (opc == '4'): #Retornar ao menu
            return

        else:
            print('Opção inválida')        

# Função para remover funcionário
def remover_funcionario():
    while True:
        id_informado= int(input('Informe o id a ser removido: '))
        for funcionario in lista_funcionarios:
            if (funcionario['id'] == id_informado):
                lista_funcionarios.remove(funcionario)
                return
        print('Id inválido')

#Menu principal do sistema
while True:
    print('1. Cadastrar Funcionário \n 2. Consultar Funcionário \n 3. Remover Funcionário \n 4. Encerrar Programa: ')
    opc= input('>>>')
    if(opc == '1'): #Cadastro com incremento de ID
        cadastrar_funcionario(id_global)
        id_global += 1 #Incrementa ID para o próximo cadastro
    elif(opc == '2'):
        consultar_funcionario()

    elif (opc == '3'):
        remover_funcionario()

    elif(opc == '4'): #Encerra o programa
        break
    else:
        print('Opção inválida, tente novamente...')
    