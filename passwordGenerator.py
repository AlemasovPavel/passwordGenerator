import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


print('Введите количество паролей для генерации')
number_of_passwords = input()
while not(number_of_passwords.isdigit() and int(number_of_passwords) > 0):
    print('Введите положительное число!!!')
    number_of_passwords = input()
number_of_passwords = int(number_of_passwords)


print('Введите длину пароля')
password_length = input()
while not(password_length.isdigit() and int(password_length) > 0):
    print('Введите положительное число!!!')
    password_length = input()
password_length = int(password_length)


print('Пароль будет включать в себя цифры?')
numeric_password = input().lower()
while not(numeric_password == 'да' or numeric_password == 'нет'):
    print('Введите только "да" или "нет"')
    numeric_password = input().lower()
if numeric_password == 'да':
    chars += digits


print('Пароль будет включать в себя прописные буквы?')
password_in_uppercase_letters = input().lower()
while not(password_in_uppercase_letters == 'да' or password_in_uppercase_letters == 'нет'):
    print('Введите только "да" или "нет"')
    password_in_uppercase_letters = input().lower()
if password_in_uppercase_letters == 'да':
    chars += uppercase_letters


print('Пароль будет включать в себя строчные буквы?')
password_in_lowercase_letters = input().lower()
while not(password_in_lowercase_letters == 'да' or password_in_lowercase_letters == 'нет'):
    print('Введите только "да" или "нет"')
    password_in_lowercase_letters = input().lower()
if password_in_lowercase_letters == 'да':
    chars += lowercase_letters


print('Пароль будет включать в себе спец символы?')
special_character_password = input().lower()
while not(special_character_password == 'да' or special_character_password == 'нет'):
    print('Введите только "да" или "нет"')
    special_character_password = input().lower()
if special_character_password == 'да':
    chars += punctuation


print('Исключить ли из пароля неоднозначные символы "il1Lo0O"?')
ambiguous_symbols = input().lower()
while not(special_character_password == 'да' or special_character_password == 'нет'):
    print('Введите только "да" или "нет"')
    special_character_password = input().lower()
if special_character_password == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(lenght, chars):
    password = ''
    list_password = []
    for _ in range(1, number_of_passwords + 1):
        for i in range(lenght):
            password += random.choice(chars)
        list_password.append(password)
        password = ''
    return list_password


print(*generate_password(password_length, chars), sep='\n')
