import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('6086154409:AAGb9h8pZcTUhsLkCk6QuhjkgmyrHtWdYaY')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, {message.from_user.first_name}! Для дальнейшей работы введите /help."
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    exchange = types.KeyboardButton('/exchange')
    help = types.KeyboardButton('/about bot')
    humor = types.KeyboardButton('/humor')
    markup.add(exchange, help, humor)
    bot.send_message(message.chat.id, 'Выберите нужную команду', reply_markup=markup)

@bot.message_handler(commands=['exchange'])
def exchange(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт с котировками валют', url='https://ru.investing.com/currencies/streaming-forex-rates-majors'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['humor'])
def get_anecdote(message):
    anek_html = requests.get('https://nekdo.ru/random/').text
    anek_text = BeautifulSoup(anek_html, 'lxml').find('div',class_='text').get_text()
    bot.send_message(message.chat.id, anek_text)

@bot.message_handler(commands=['about'])
def description(message):
    bot.send_message(message.from_user.id, 'Приветствуем вас в познавательно-развлекательном боте!\n' +
        '1) Чтобы получить актуальную информацию о котировках валют, нажмите кнопку /exchange.\n' +  
        'Для вас откроется сайт Investing.com - Ведущий Финансовый Портал, где можно найти любую\n' +
        'интересующую вас информацию касательно обмена валют и не только.\n ' +
        '2) Если вы хотите немного отдохнуть и посмеяться нажмите кнопку /humor.\n' +
        'Вы увидите смешной анекдот.')
   




bot. polling(non_stop=True)