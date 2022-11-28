import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands =['start'])
def start(massege):
    bot.send_message(massege.chat.id, f'Привет, {massage.from_user.username}')