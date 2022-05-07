# Напишите функцию, которая проверяет: является ли слово палиндромом

import string


def reverse(text):
    '''Вазвращает текст задом на перед'''
    return text[::-1]


def is_palindrome(text):
    '''Сравнивает исходный текст с перевёрнутым'''
    return text == reverse(text)


something = input('Введите текст: ')
a = ''

# Перебираем тескст, убираем пробелы, знаки пунктуации, и переводим в нижний регистр..
for i in something:
    if i in string.punctuation or i == " ":
        a = something.replace(i, '')
        a = a.lower()

if is_palindrome(a):
    print('Это полиндром')
else:
    print('Не полиндром')
