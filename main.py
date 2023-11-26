import random
import PySimpleGUI as PySimpleGUI
#

def generate_random_number(upper_limit):
    return random.randint(1, upper_limit)


def main():
    PySimpleGUI.theme('DarkAmber')  # Встановлюємо тему

    layout = [
        [PySimpleGUI.Text('Виберіть верхню межу для числа:', text_color='white')],
        [PySimpleGUI.InputText(key='-UPPER_LIMIT-')],
        [PySimpleGUI.Button('Підтвердити', button_color=('white', 'black'))],
    ]

    window = PySimpleGUI.Window('Вибір верхньої межі', layout)

    while True:
        event, values = window.read()

        if event == PySimpleGUI.WINDOW_CLOSED:
            break

        try:
            upper_limit = int(values['-UPPER_LIMIT-'])

            if upper_limit > 0:
                window.close()
                target_number = generate_random_number(upper_limit)
                attempts = 0

                game_layout = [
                    [PySimpleGUI.Text(f'Вгадайте число від 1 до {upper_limit}:', text_color='white')],
                    [PySimpleGUI.InputText(key='-GUESS-')],
                    [PySimpleGUI.Button('Перевірити'), PySimpleGUI.Button('Вийти')],
                    [PySimpleGUI.Text('', size=(20, 1), key='-OUTPUT-', text_color='white')]
                ]

                game_window = PySimpleGUI.Window('Вгадай число', game_layout)

                while True:
                    event, values = game_window.read()

                    if event == PySimpleGUI.WINDOW_CLOSED or event == 'Вийти':
                        break

                    try:
                        guess = int(values['-GUESS-'])
                        attempts += 1

                        if guess < target_number:
                            game_window['-OUTPUT-'].update('Загадане число більше!')
                        elif guess > target_number:
                            game_window['-OUTPUT-'].update('Загадане число менше!')
                        else:
                            PySimpleGUI.popup(f'Ви вгадали число {target_number} за {attempts} спроб!',
                                              title='Привітання')
                            break

                    except ValueError:
                        game_window['-OUTPUT-'].update('Введіть коректне число!')

                game_window.close()
                break
            else:
                PySimpleGUI.popup('Введіть число більше 0!')

        except ValueError:
            PySimpleGUI.popup('Введіть коректне число!')

    window.close()


if __name__ == '__main__':
    main()
