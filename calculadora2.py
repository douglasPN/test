from PySimpleGUI import PySimpleGUI as sg

number1 = 0
number2 = 0
resultado = 0
operacao = ''

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Número1'),sg.Input(key=number1, size=(20,1))],
    [sg.Text('Operação'),sg.Input(key=operacao,size=(20,1))],
    [sg.Text('Número2'),sg.Input(key=number2,size=(20,1))],
    [sg.Button('Resultado')]
]
# Janela
janela = sg.Window('Calculadora', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if valores['numero1'] == '2' and valores['operacao'] == '+' and valores['numero2'] == '2':
        if eventos == 'Resultado': 
            print(number1, operacao, number2, '=', resultado )

#NAO CONSEGUI AINDA