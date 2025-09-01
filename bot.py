import os
from dotenv import load_dotenv
import telebot

load_dotenv()  # .env fayldan ma’lumotlarni yuklaydi

TOKEN = os.getenv("BOT_TOKEN")  # .env fayldan tokenni oladi
print("TOKEN: ", TOKEN)
if TOKEN is None:
    raise ValueError("BOT_TOKEN not found. Check your .env file.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men Jamshidning birinchi botiman.")

bot.polling()