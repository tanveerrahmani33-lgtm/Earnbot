import telebot
from telebot import types
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

user_points = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    if user_id not in user_points:
        user_points[user_id] = 0
    
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo("https://tanveerrahmani33-lgtm.github.io/Earnbot/")
    btn1 = types.InlineKeyboardButton("💰 Watch Ad +10 Points", web_app=web_app)
    btn2 = types.InlineKeyboardButton("💎 My Points", callback_data="my_points")
    markup.add(btn1, btn2)
    
    bot.send_message(user_id, f"Welcome to Tanaweer Earn Bot! 💰\n\nYour Points: {user_points[user_id]}\n\nWatch ads and earn!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.from_user.id
print("Bot started successfully!")
bot.infinity_polling()
   
