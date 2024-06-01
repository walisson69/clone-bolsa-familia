import PySimpleGUI as sg

sg.theme('reddit')

janela_principal = [
    [sg.Text('                 CADASTRO BOLSA FAMILIA')],
    [sg.Text('Dados do beneciário')],
    [sg.Text('Nome completo')],
    [sg.Input(key='Nome: ')],
    
    [sg.Text('Idade   ')],
    [sg.Input(key='Idade: ')],
    [sg.Text('Cpf      ')],
    [sg.Input(key='Cpf: ')],
    
    
    [sg.Text('Dados do intergrante da familia')],
    [sg.Text('Nome do filho')],
    [sg.Input(key='nome do fihlo: ')],
    [sg.Text('Idade do filho')],
    [sg.Input(key='Idade: ')],
    [sg.Text('Informe o CPF')],
    [sg.Input(key='CPf: ')],
    
    [sg.Button('Enviar dados')]
    
]



janela = sg.Window('Princinpal',layout=janela_principal)

while True:
    event, values= janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar dados':
        email = values['Nome: ']
        senha = values['Cpf: ']
        nome = values['nome do fihlo: ']
        cpf = values['CPf: ']
        print(f'nome do otario: {email}')
        print(f'cpf do otario: {senha}')
        print(f'nome do filho: {nome}')
        print(f'cpf do filho: {cpf}')
        

