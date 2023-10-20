import telebot
import random
from dotenv import load_dotenv
import os
from telebot import types  # для создания кнопок


#Безопасная подгрузка token
load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))  # Token бота берётся из BotFather

# Keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
random_sender = types.KeyboardButton("Скинь Рандомное число")
markup.add(random_sender)

# Создание кнопки после команды Start
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, '<b>Генератор Рандома Активирован</b> (бип-пуп-пиип)', parse_mode='html',
                     reply_markup=markup)

# Отслеживание нажатий кнопки
@bot.message_handler(content_types=['text'])
def first_number_step(message):
    if message.text == 'Скинь Рандомное число':
        msg = bot.send_message(message.chat.id, 'Введите начало диапазона')
        bot.register_next_step_handler(msg, second_number_step)             # переход на функцию second_number_step
    else:
        bot.send_message(message.chat.id, 'Такой команды нет')

# Получение первого числа диапазона
def second_number_step(message):
    global NUM_first
    NUM_first = int(message.text)
    msg = bot.send_message(message.chat.id, 'Введите конец диапазона')
    bot.register_next_step_handler(msg, result_number_step)                 # переход на функцию result_number_step

# Получение второго числа диапазона
def result_number_step(message):
    global NUM_second
    NUM_second = int(message.text)
    result(message)                                                          # Вызов функции result(message)

# Вывод результата (рандом)
def result(message):
    bot.send_message(message.chat.id, 'Случайное число:  ' + str(random.randint(NUM_first, NUM_second)))

#Run
bot.polling(none_stop=True)