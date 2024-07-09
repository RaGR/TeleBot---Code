'''
author: Unknown LTH | date: 19-4-3
script to test a simple functionality in a bot(@allinone4u)
case= finding group ID
[ https://api.telegram.org/bot7220090779:AAE4fI6iseB8a7YBPQ0lIFUZklfhZ3PVT3Y/getUpdates ]

'''

import telebot

# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
BOT_TOKEN = '7220090779:AAE4fI6iseB8a7YBPQ0lIFUZklfhZ3PVT3Y'
bot = telebot.TeleBot(BOT_TOKEN)

# Replace 'YOUR_GROUP_USERNAME' with your group's username or URL (without 'https://t.me/')
group_username = '@langsysbot_test'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "i will snd a masssage to a group im admin in ,...")

#sending masssage to group:

# Replace 'YOUR_MESSAGE' with the message you want to send
message = 'salam be aAza goroh mohtaram'

def resolve_username(username):
    try:
        user = bot.get_chat(username)
        return user.id
    except Exception as e:
        print(f"Error: {e}")
        return None

group_id = resolve_username(group_username)

if group_id:
    bot.send_message(group_id, message)
    print("Message sent successfully!")
else:
    print("Failed to resolve the username.")

# Start the bot (this line is necessary to keep the bot running)
bot.polling(none_stop=True)