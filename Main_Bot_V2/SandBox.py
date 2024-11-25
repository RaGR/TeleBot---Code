import telebot
from telebot import types

# Create bot instance
BOT_TOKEN = 'TOKEN IS HIIDEN BY THE AUTHOR !!!'
bot = telebot.TeleBot ( BOT_TOKEN )

# Define courses
COURSES = [ 'PL' , 'CHC' , 'ADC' , 'T' , 'B' , 'E' , 'PI' , 'I' , 'UI' , 'ADV' , 'IELTS' , 'CAE' , 'CPE' ]


# Define teachers group chat id
def resolve_username(username) :  #func to extract chatID of a group
    try :
        user = bot.get_chat ( username )
        return user.id
    except Exception as e :
        print ( f"Error: {e}" )
        return None


GROUP_URL = '@langsysbot_test'
TEACHERS_GROUP = resolve_username ( GROUP_URL )

# Define user data dictionary
user_data = { }


@bot.message_handler ( commands=[ 'start' ] )
def start(message) :
    markup = types.ReplyKeyboardMarkup ( one_time_keyboard=True )
    markup.add ( *COURSES )
    bot.send_message ( message.chat.id , 'Hi! What course would you like to enroll in?' , reply_markup=markup )
    bot.register_next_step_handler ( message , course )


def course(message) :
    user_data [ message.chat.id ] = { 'course' : message.text }
    bot.send_message ( message.chat.id , 'Please send us your documents or a text to prove your level.' )
    bot.register_next_step_handler ( message , document )


def document(message) :
    user_data [ message.chat.id ] [ 'document' ] = message.text
    user = message.from_user
    info = f"New student enrollment:\nName: {user.first_name}\nCourse: {user_data [ message.chat.id ] [ 'course' ]}\nDocument: {user_data [ message.chat.id ] [ 'document' ]}"
    bot.send_message ( TEACHERS_GROUP , info )
    bot.send_message ( message.chat.id , 'Thank you! We will review your documents and get back to you.' )


@bot.message_handler ( commands=[ 'cancel' ] )
def cancel(message) :
    bot.send_message ( message.chat.id , 'Bye! I hope we can talk again some day.' )


bot.polling ()
