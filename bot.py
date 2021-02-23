import telebot
bot = telebot.TeleBot('420101398:AAGqALSlN_MWSMRFtw8OczVHF3nOyRBijlc')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
##Добавим ещё один обработчик для получения текстовых сообщений. Если бот получит «Привет», он также поздоровается. Все остальные сообщения будут определены, как нераспознанные:

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
##Запускаем бота следующей строкой:

bot.polling(none_stop=True)