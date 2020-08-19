# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
x = int(input('Введите целое трехзначное число: '))

a = x // 100
b = (x % 100) // 10
c = x % 10

print(f'Сумма цифр числа {x}: {a + b + c}')
print(f'Произведение цифр числа {x}: {a * b * c}')

# Ссылка на Google Drive:
# https://drive.google.com/file/d/1kpN2hl3VIl5iq-WBNVHSzsh356vULU5A/view?usp=sharing