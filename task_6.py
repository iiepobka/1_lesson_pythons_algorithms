# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
letter_number = int(input('Введите цифрой от 1 до 26 номер буквы английского алфавита: '))

letter_number = chr(letter_number + 96)

print(f'Введенное значение соответствует букве: {letter_number}')
