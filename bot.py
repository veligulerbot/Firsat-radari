import telebot

TOKEN = '8061348104:AAHD6kVNvpbQqt-tTpLhvfsujTbmnqy91Yo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🚀 Fırsat Radarı aktif! 7/24 takipteyim.")

if __name__ == '__main__':
    bot.infinity_polling()
