'''
author: Unknown LTH | date: 19-4-3
script to send cridentials and assesment of STUDENT in the ADMIN group for teachers
CASE=  storing data in group
'''


import telebot
from telebot import types

# Initialize your bot
bot = telebot.TeleBot('7220090779:AAE4fI6iseB8a7YBPQ0lIFUZklfhZ3PVT3Y')

# Dictionary to store user inputs
user_inputs = {}

# Define the designated group chat ID
def resolve_username(username): #func to extract chatID of a group
    try:
        user = bot.get_chat(username)
        return user.id
    except Exception as e:
        print(f"Error: {e}")
        return None

group_username = '@langsysbot_test' # Replace with your group @handler
designated_group_id = resolve_username(group_username)

# Handle the /start command to greet the user and ask for requirements and user pass
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, English learner! Please provide your user pass.")

# Handle user pass input
@bot.message_handler(func=lambda message: True)
def handle_user_pass(message):
    user_id = message.chat.id
    user_name = message.from_user.username
    user_pass = message.text
    user_inputs[user_id] = {'user_pass': user_pass, 'username': user_name, 'requirements': {}}
    forward_user_inputs(user_id)

# Handle IELTS Test Speaking (voice input)
@bot.message_handler(content_types=['voice'])
def handle_ielts_speaking(message):
    user_id = message.chat.id
    user_inputs[user_id]['requirements']['ielts_speaking'] = message.voice.file_id
    forward_user_inputs(user_id)

# Handle IELTS Test Reading (poll input)
@bot.message_handler(func=lambda message: True)
def handle_ielts_reading(message):
    user_id = message.chat.id
    user_inputs[user_id]['requirements']['ielts_reading'] = message.text
    forward_user_inputs(user_id)

# Handle IELTS Test Writing (text input)
@bot.message_handler(func=lambda message: True)
def handle_ielts_writing(message):
    user_id = message.chat.id
    user_inputs[user_id]['requirements']['ielts_writing'] = message.text
    forward_user_inputs(user_id)

# Handle IELTS Test Listening (poll input)
@bot.message_handler(func=lambda message: True)
def handle_ielts_listening(message):
    user_id = message.chat.id
    user_inputs[user_id]['requirements']['ielts_listening'] = message.text
    forward_user_inputs(user_id)

# Function to forward user inputs to the designated group
def forward_user_inputs(user_id):
    username = user_inputs[user_id]['username']
    userpass = user_inputs[user_id]['user_pass']
    requirements = user_inputs[user_id]['requirements']
    text = f"User: {username}\nUser pass: {userpass}\nRequirements: {requirements}"
    bot.send_message(designated_group_id, text)

# Run the bot
bot.polling()
