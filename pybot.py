import telebot
from telebot import types

botID = 'bot_token'
bot = telebot.TeleBot(botID)
jpg_lock = '/home/okakc/GOSHA_bot/media/kirdik.jpg'

@bot.message_handler(commands=['start'])
def handle_start(message):
    gif = open(jpg_lock, 'rb')
    bot.send_photo(message.chat.id, gif, caption='Привет! Ты можешь узнать мои возможности через /help')

@bot.message_handler(commands=['help'])
def handle_help(message):
    gif = open(jpg_lock, 'rb')
    bot.send_photo(message.chat.id, gif, caption='Меню ГОШИ - /goshaMENU')

@bot.message_handler(commands=['goshaMENU'])
def handle_goshaMENU(message):
    gif = open(jpg_lock, 'rb')
    markup = types.InlineKeyboardMarkup()
    inl1 = types.InlineKeyboardButton('🐱‍👤Послать гошу нахуй', callback_data='pGOSHA')
    inl2 = types.InlineKeyboardButton('🙉Показать фотку гоши', callback_data='phGosha')
    inl3 = types.InlineKeyboardButton('📞Показать номер телефона Гоши', callback_data='numGosha')
    inl4 = types.InlineKeyboardButton('📃Информация о гоше', callback_data='info')
    inl5 = types.InlineKeyboardButton('🔐Сикретная информация', callback_data='secret')
    markup.row(inl2, inl1)
    markup.row(inl3, inl4)
    markup.row(inl5)
    bot.send_photo(message.chat.id, gif, caption='ГОША МЕНЮ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'pGOSHA':
        bot.send_message(call.message.chat.id, "🦜Гоша пошел нахуй сын собаки")
    elif call.data == 'phGosha':
        file_path = '/home/okakc/GOSHA_bot/media/gosha.jpg'
        file = open(file_path, 'rb')
        bot.send_photo(call.message.chat.id, file, caption="🙉Вот этот пидарас")
        file.close()
    elif call.data == 'numGosha':
        bot.send_message(call.message.chat.id, "📞+79898240107")
    elif call.data == 'info':
        gif = open(jpg_lock, 'rb')
        bot.send_photo(call.message.chat.id, gif, caption="Имя - Георгий\nФамилия - Ильинский\nВозраст - 13 лет\nГород-Краснодар\nШкола - №20\nКласс - 7Д\nПоложение в обществе - ЛОХ")
    elif call.data == 'secret':
        croc_lock = '/home/okakc/GOSHA_bot/media/croc.jpg'
        croc = open(croc_lock, 'rb')
        bot.send_photo(call.message.chat.id, croc, caption='Переможник')
    else:
        bot.send_message(call.message.chat.id, "⚠Ошибка")

bot.infinity_polling()
