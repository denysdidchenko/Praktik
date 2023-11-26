import random
import PySimpleGUI as sg

def generate_random_number(upper_limit):
    return random.randint(1, upper_limit)

def main():
    layout = [
        [sg.Text('Виберіть верхню межу для числа:', background_color='black', text_color='white')],
        [sg.InputText(key='-UPPER_LIMIT-', background_color='lightgrey')],
        [sg.Button('Підтвердити', button_color=('white', 'black'))],
    ]

    window = sg.Window('Вибір верхньої межі', layout, background_color='black')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        try:
            upper_limit = int(values['-UPPER_LIMIT-'])

            if upper_limit > 0:
                window.close()
                target_number = generate_random_number(upper_limit)
                attempts = 0

                game_layout = [
                    [sg.Text(f'Вгадайте число від 1 до {upper_limit}:', background_color='black', text_color='white')],
                    [sg.InputText(key='-GUESS-', background_color='lightgrey')],
                    [sg.Button('Перевірити', button_color=('white', 'black')), sg.Button('Вийти', button_color=('white', 'black'))],
                    [sg.Text('', size=(20, 1), key='-OUTPUT-', background_color='black', text_color='white')]
                ]

                game_window = sg.Window('Вгадай число', game_layout, background_color='black')

                while True:
                    event, values = game_window.read()

                    if event == sg.WINDOW_CLOSED or event == 'Вийти':
                        break

                    try:
                        guess = int(values['-GUESS-'])
                        attempts += 1

                        if guess < target_number:
                            game_window['-OUTPUT-'].update('Загадане число більше!')
                        elif guess > target_number:
                            game_window['-OUTPUT-'].update('Загадане число менше!')
                        else:
                            game_window['-OUTPUT-'].update(f'Ви вгадали число {target_number} за {attempts} спроб!')
                            break

                    except ValueError:
                        game_window['-OUTPUT-'].update('Введіть коректне число!')

                game_window.close()
                break
            else:
                sg.popup('Введіть число більше 0!')

        except ValueError:
            sg.popup('Введіть коректне число!')

    window.close()

if __name__ == '__main__':
    main()
