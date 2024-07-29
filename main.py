import telebot
from telebot import types

bot = telebot.TeleBot("6588713567:AAGoPx0v6rCbndSkgGN6rhCwapOTFdpks2c")

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    button_profile = types.InlineKeyboardButton('Профиль', callback_data='profile')
    markup.row(button_profile)
    bot.reply_to(message, f"""\
    Привет, {message.from_user.first_name}. Я бот - Аниме Контейнер. Можешь мне отправить список аниме, которых ты уже просмотрел(а) и я добавлю их в твою базу данных.\n\
В этой базе данных будет отображаться: количество просмотренных аниме и средний рейтинг каждого аниме.""", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    bot.answer_callback_query(call.id)
    if call.data == 'profile':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"""
{call.message.from_user.first_name}, Ваш профиль:
ID:
Количество просмотренных аниме: """)

bot.infinity_polling()