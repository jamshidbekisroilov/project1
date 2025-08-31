import telebot

TOKEN = "8394176339:AAGphpe1E8m8QwlaqUPZ-AWChAINpDtAhuM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm Jamshidbek's first bot")

bot.polling()