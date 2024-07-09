'''
author: Unknown LTH | date: 19-4-3
script to manage basic STUDENT inputs and tests individuals skills
case= private chat with student -initialze-
'''

import telebot

# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
BOT_TOKEN = '7220090779:AAE4fI6iseB8a7YBPQ0lIFUZklfhZ3PVT3Y'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm here to help you practice for your IELTS test.\nPlease send your username and password to log in.")

# Function to handle login credentials (simple version)
@bot.message_handler(func=lambda message: 'password' in message.text.lower())
def ask_for_test_requirements(message):
    bot.send_message(message.chat.id, "Thank you for logging in. What would you like to practice today? (Speaking/Reading/Writing/Listening)")

@bot.message_handler(func=lambda message: 'speaking' in message.text.lower())
def speaking_test(message):
    bot.send_message(message.chat.id, "Please record your voice talking about your favorite book for one minute and send it here.")

@bot.message_handler(func=lambda message: 'writing' in message.text.lower())
def writing_test(message):
    bot.send_message(message.chat.id, "Please write 250 words about the impact of social media and send your text here.")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    bot.reply_to(message, "Thanks for submitting your speaking test!")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.reply_to(message, "Thanks for submitting your writing test!")

@bot.message_handler(func=lambda message: 'reading' in message.text.lower() or 'listening' in message.text.lower())
def poll_test(message):
    poll_options = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']
    text = "Do you think technology benefits society?" if 'reading' in message.text.lower() else "Listen to the clip (not implemented here) and rate your understanding."
    bot.send_poll(message.chat.id, question=text, options=poll_options, is_anonymous=False)

bot.infinity_polling()
