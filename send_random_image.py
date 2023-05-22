import requests

from telegram import Bot

bot = Bot(token='6171597290:AAECS1APDsPcqF8hzpAodi1-ZBF4dYzXnIU')

URL = 'https://api.thecatapi.com/v1/images/search'
# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python
response = requests.get(URL).json()

# Рассмотрим структуру и содержимое переменной response
print(response)

# Посмотрим, какого типа переменная response
print(type(response))

# response - это список. А какой длины?
print(len(response))

# Посмотрим, какого типа первый элемент
print(type(response[0]))
