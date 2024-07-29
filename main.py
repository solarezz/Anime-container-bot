import telebot
from telebot import types
import database as db

bot = telebot.TeleBot("6588713567:AAGoPx0v6rCbndSkgGN6rhCwapOTFdpks2c")

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    button_profile = types.InlineKeyboardButton('Профиль', callback_data='profile')
    markup.row(button_profile)
    bot.reply_to(message, f"""\
    Привет, {message.from_user.first_name}. Я бот - Аниме Контейнер. Можешь мне отправить список аниме, которых ты уже просмотрел(а) и я добавлю их в твою базу данных.\n\
В этой базе данных будет отображаться: количество просмотренных аниме и средний рейтинг каждого аниме.""", reply_markup=markup)
    db.table_input(message.chat.id, message.from_user.username)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    bot.answer_callback_query(call.id)
    if call.data == 'profile':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"""
@{db.info(call.message.chat.id)[2]}, Ваш профиль:
ID: {db.info(call.message.chat.id)[0]}
Количество просмотренных аниме: {db.info(call.message.chat.id)[3]}""")

bot.infinity_polling()