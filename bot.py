from keep_alive import keep_alive
import telebot

keep_alive()

TOKEN = '8061348104:AAHD6kVNvp bQqt-tTpLh...' # Token'ını buraya yapıştır
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot aktif!")

if __name__ == '__main__':
    bot.infinity_polling()
