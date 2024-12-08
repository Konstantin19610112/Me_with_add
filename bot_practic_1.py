import telebot
from telebot import types
from telebot.types import Message

BOT_TOKEN = "7739343110:AAGyU_2XxqB-oxVpGU1vr7-qh-w7k9mkkPw"
APP_URL = "https://493e4027-65fb-4777-be8d-2a0f062c4f41-00-jmz43w1f07gx.janeway.repl.co/"

bot = telebot. TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start_command(message: Message):

    web_app_info = types.WebAppInfo(APP_URL)
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    menu_button = types.KeyboardButton("Menu", web_app = web_app_info)
    markup.add(menu_button)
    bot.send_message(message.chat.id,"Well Come. Push the button", reply_markup=markup)
bot.polling()