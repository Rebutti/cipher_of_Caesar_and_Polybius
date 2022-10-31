from unittest import result
import PySimpleGUI as sg
from cezar import cezar_cipher
from polibiy import polibiy_cipher, polibiy_decipher
from myerrors import MyError
sg.theme('DarkAmber')

def cezar_errors(text,size, decipher=False):
    result = cezar_cipher(text, size,decipher)
    if result == ValueError or result == MyError:
        layout = [ 
            [sg.Text('Введіть ціле число від 1 до 25 для кроку')],
            [sg.Button('Закрити')] 
        ]
        create_window(layout)
        raise ValueError
    return result


def create_window(layout):
    window = sg.Window('LAB2', layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Закрити': # if user closes window or clicks cancel
            break
        if values['cipher'] == True:
            try:
                new_layout = []
                if values['cezar']:
                    cezar_cipher = cezar_errors(values['text'], values['size'])
                    new_layout.append([sg.Text(f'Зашифроване слово методом Цезаря: {cezar_cipher}')])
                elif values['polibiy']:
                    polibiy_cipher_ = polibiy_cipher(values['text'])
                    new_layout.append([sg.Text(f'Зашифроване слово методом Полібія: {polibiy_cipher_}')])
            except ValueError:
                continue
            new_layout.append([sg.Button('Закрити')])
        else:
            try:
                new_layout = []
                if values['cezar']:
                    print(values['cipher'])
                    cezar_cipher = cezar_errors(values['text'], values['size'], decipher=True)
                    new_layout.append([sg.Text(f'Дешифроване слово методом Цезаря: {cezar_cipher}')])
                elif values['polibiy']:
                    polibiy_cipher_ = polibiy_decipher(values['text'])
                    new_layout.append([sg.Text(f'Дешифроване слово методом Полібія: {polibiy_cipher_}')])
            except ValueError:
                continue
            new_layout.append([sg.Button('Закрити')])
        create_window(new_layout)

    window.close()





if __name__ == "__main__":
    layout = [ 
                [sg.Text('Введіть текст, що потрібно зашифрувати або дешифрувати'), sg.InputText(key='text')],
                [sg.Radio('Шифр Цезаря',
                                 "RADIO1", default=False, key="cezar"),
                       sg.Radio('Шифр Полібія',
                                "RADIO1", default=True, key="polibiy")],
                [sg.Text('Введіть крок для шифру Цезаря'), sg.InputText(key='size')],
                [sg.Checkbox('Зашифрувати', default=True, key='cipher')],
                [sg.Button('Ok'), sg.Button('Закрити')] 
            ]
    create_window(layout)


