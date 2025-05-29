#!/usr/bin/python3
"""
Sami Remili Pythonist
Fennec Calculator with Enhanced UI
"""
import PySimpleGUI as sg

# Custom Theme
sg.theme('DarkBlue3')
sg.LOOK_AND_FEEL_TABLE['FennecTheme'] = {
    'BACKGROUND': '#2c3e50',
    'TEXT': '#ecf0f1',
    'INPUT': '#34495e',
    'TEXT_INPUT': '#ecf0f1',
    'SCROLL': '#34495e',
    'BUTTON': ('#ecf0f1', '#3498db'),
    'PROGRESS': ('#ecf0f1', '#3498db'),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0
}
sg.theme('FennecTheme')

# Layout
layout = [
    [sg.Text('FENNEC CALCULATOR', font=('Arial', 24, 'bold'), 
     justification='center', expand_x=True, pad=(0,(20,10)))],
    [sg.Text('by Sami_Fennec_Deve', font=('Arial', 12), 
     text_color='#bdc3c7', justification='center', expand_x=True, pad=(0,20))],
    
    [sg.Frame('Input Numbers', [
        [sg.Text('First Number:', size=(12,1), font=('Arial', 12)),
         sg.Input(key='-NUM1-', size=(15,1), font=('Arial', 12), justification='right')],
        [sg.Text('Second Number:', size=(12,1), font=('Arial', 12)),
         sg.Input(key='-NUM2-', size=(15,1), font=('Arial', 12), justification='right')]
    ], border_width=0, pad=(10,10))],
    
    [sg.Frame('Operations', [
        [sg.Button('+ Addition', size=(12,2), font=('Arial', 14, 'bold'), button_color=('#ecf0f1','#27ae60')),
         sg.Button('- Subtraction', size=(12,2), font=('Arial', 14, 'bold'), button_color=('#ecf0f1','#e74c3c'))],
        [sg.Button('× Multiplication', size=(12,2), font=('Arial', 14, 'bold'), button_color=('#ecf0f1','#f39c12')),
         sg.Button('÷ Division', size=(12,2), font=('Arial', 14, 'bold'), button_color=('#ecf0f1','#9b59b6'))],
        [sg.Button('^ Exponent', size=(26,2), font=('Arial', 14, 'bold'), button_color=('#ecf0f1','#3498db'))]
    ], border_width=0, pad=(10,10))],
    
    [sg.Frame('Result', [
        [sg.Text('', key='-RESULT-', font=('Arial', 18, 'bold'), 
         size=(20,1), justification='center', background_color='#34495e')]
    ], border_width=0, pad=(10,20))],
    
    [sg.Button('Exit', size=(10,1), font=('Arial', 12), button_color=('#ecf0f1','#e74c3c'), pad=(0,10))]
]

# Create window
window = sg.Window('Fennec Calculator', layout, size=(400, 600), 
                   element_justification='center', finalize=True)

# Event loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    try:
        num1 = float(values['-NUM1-'])
        num2 = float(values['-NUM2-'])
    except ValueError:
        sg.popup_error('Please enter valid numbers!', title='Input Error')
        continue
    
    if event == '+ Addition':
        result = num1 + num2
        operation = '+'
    elif event == '- Subtraction':
        result = num1 - num2
        operation = '-'
    elif event == '× Multiplication':
        result = num1 * num2
        operation = '×'
    elif event == '÷ Division':
        if num2 == 0:
            sg.popup_error('Cannot divide by zero!', title='Math Error')
            continue
        result = num1 / num2
        operation = '÷'
    elif event == '^ Exponent':
        result = num1 ** num2
        operation = '^'
    
    # Display formatted result
    window['-RESULT-'].update(f'{num1} {operation} {num2} = {result:.4f}')

window.close()