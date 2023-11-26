import random
import PySimpleGUI as sg

def generate_random_number():
    return random.randint(1, 100)

def main():
    target_number = generate_random_number()
    attempts = 0

    layout = [
        [sg.Text('Вгадайте число від 1 до 100:')],
        [sg.InputText(key='-GUESS-')],
        [sg.Button('Перевірити'), sg.Button('Вийти')],
        [sg.Text('', size=(20, 1), key='-OUTPUT-')]
    ]

    window = sg.Window('Вгадай число', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Вийти':
            break

        try:
            guess = int(values['-GUESS-'])
            attempts += 1

            if guess < target_number:
                window['-OUTPUT-'].update('Загадане число більше!')
            elif guess > target_number:
                window['-OUTPUT-'].update('Загадане число менше!')
            else:
                window['-OUTPUT-'].update(f'Ви вгадали число {target_number} за {attempts} спроб!')
                break

        except ValueError:
            window['-OUTPUT-'].update('Введіть коректне число!')

    window.close()

if __name__ == '__main__':
    main()
