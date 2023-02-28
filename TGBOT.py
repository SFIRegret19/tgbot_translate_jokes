from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
#from credits import bot_token
import datetime
import random
 
bot_token = '5157864036:AAHUbQC71KYB7u-lrsqP1C4meEDlD4TCYtg'

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher
 
def roll(update,context):
    a = random.randint(1,6)
    context.bot.send_message(update.effective_chat.id,a) 
def help(update, context):
    context.bot.send_message(update.effective_chat.id,'Я бот и ничего не умею')

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет!')

def joke(update, context):
    jokes = ['Шутка 1','Шутка 2','Шутка 3']
    x = random.randint(0,len(jokes))
    context.bot.send_message(update.effective_chat.id, jokes[x])

dictionary = {'яблоко': 'apple' , 'апельсин': 'orange' , 'груша': 'pear', 'персик': 'peach' , }

def translater(update, context):
    word = context.args
    result = ''
    for i in word: 
        result += dictionary[i] + ' '   
    context.bot.send_message(update.effective_chat.id, result)

'''
def hello(update, context):
    context.bot.send_mesage(update.effective_chat)
'''

def alarm(context):
    job = context.job
    context.bot.send_message(job.context, 'ДЗЗЗЫНЬ! Время прошло')

#def timer(update, context):
  #  seconds = context.args[0]
   # context.job_queue.run_once(alarm, seconds, context = update.effective_chat.id, name = str(update.effective_chat.id))
    #context.bot.send_message(update.effective_chat.id, 'Таймер установлен')
##

#def unset(update, context):
 #   set_handler = CommandHandler('set', timer)

def start(update, context):
    keyboard = [
        [InlineKeyboardButton('Таймер 5', callback_data='1'), InlineKeyboardButton('Таймер 10', callback_data='2')],
        [InlineKeyboardButton('Кнопка 3', callback_data='3'), InlineKeyboardButton('Кнопка 4', callback_data='4')]
    ]
    update.message.reply_text('Нажми на кнопку',reply_markup=InlineKeyboardMarkup(keyboard))

def button(update,context):
    query = update.callback_query
    query.answer()
    if query.data == '1':
        context.job_queue.run_once(alarm, 5, context=update.effective_chat.id, name=str(update.effective_chat.id))
        context.bot.send_message(update.effective_chat.id, 'Таймер поставили')
    elif query.data == '2':
        context.job_queue.run_once(alarm, 10, context=update.effective_chat.id, name=str(update.effective_chat.id))
        context.bot.send_message(update.effective_chat.id, 'Таймер поставили')
    elif query.data == '3':
        context.bot.send_message(update.effective_chat.id, 'Вы нажали на третью кнопку')
    elif query.data == '4':
        context.bot.send_message(update.effective_chat.id, 'Вы нажали на четвертую кнопку')

def writeToWall(update, context):
    line = ''.join(context.args) + '\n'
    f = open

start_handler = CommandHandler('start', start)
button_handler = CallbackQueryHandler(button)
help_handler = CommandHandler('help', help) 
roll_handler = CommandHandler('roll', roll)
jokes_handler = CommandHandler('joke',joke)
translate_handler = CommandHandler('translate',translater)

dispatcher.add_handler(translate_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler) 
dispatcher.add_handler(roll_handler)
dispatcher.add_handler(jokes_handler)
#dispatcher.add_handler(set_handler)

updater.start_polling()
updater.idle()