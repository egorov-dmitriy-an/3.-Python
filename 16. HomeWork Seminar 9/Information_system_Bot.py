from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler, ConversationHandler
from datetime import datetime as dt
import csv

import os
print(os.getcwd())

bot_token = '5561873128:AAHMMJjfipo0ehD-MjNmuKKn53My9jRPE8E'

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

VIEW_ALL, SEARCH_KID = range(2)

contact = ''
index = 0
surname = ''
variant = 0


def start(update, _):
    keyboard = [
        [
            InlineKeyboardButton("Показать полный список воспитанников", callback_data='1')],
            [InlineKeyboardButton("Поиск воспитанника по фамилии", callback_data='2')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Добро пожаловать в информационную систему\nнашего небольшого детского сада!', reply_markup=reply_markup)


def button_start(update, context):
    query = update.callback_query
    global variant
    variant = query.data
    query.answer()
    print(variant)
    if variant == '1':
        context.bot.send_message(update.effective_chat.id, f'Отправьте любой символ для просмотра списка всех воспитанников')
        return VIEW_ALL
    elif variant == '2':
        context.bot.send_message(update.effective_chat.id, f'Введите фамилию: ')
        return SEARCH_KID


def print_all_kid(update, context):
    with open('Seminar_10_data_kids.csv', 'r', encoding='UTF-8') as r_file:
        file = list(csv.reader(r_file, delimiter=','))
        count = 0
        for row in file:
            context.bot.send_message(update.effective_chat.id, f'{row[1]}.  {row[2]}  {row[3]}')
            count += 1









def message_search(update, context):
    global surname
    global variant
    count = 0
    surname = update.message.text
    with open('guide_Bot.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            surname_sp = line.split(';')
            if surname in surname_sp[0]:
                context.bot.send_message(update.effective_chat.id, f'Фамилия: {surname_sp[0]}\nИмя: {surname_sp[1]}\nТелефон: {surname_sp[2]}\nОписание: {surname_sp[3]}')
                count = 1
    if count == 0:
        context.bot.send_message(update.effective_chat.id, f'Совпадений не найдено')

    time = dt.now().strftime('%H:%M')
    with open('log_seminar_10.csv', 'a') as file:
        file.write(f'{time};Find contact;{surname}\n')
        
    return ConversationHandler.END
    

def message_save(update, context):
    global contact
    global index
    if index == 0:
        contact += update.message.text + ';'
        context.bot.send_message(
            update.effective_chat.id, f'Введите имя: ')
        index += 1
    elif index == 1:
        contact += update.message.text + ';'
        context.bot.send_message(
            update.effective_chat.id, f'Введите телефон: ')
        index += 1
    elif index == 2:
        contact += update.message.text + ';'
        context.bot.send_message(
            update.effective_chat.id, f'Введите описание: ')
        index += 1
    elif index == 3:
        contact += update.message.text + ';'
        con = contact.split(';')
        context.bot.send_message(
            update.effective_chat.id, f'Добавлен контакт: \nФамилия: {con[0]}\nИмя: {con[1]}\nТелефон: {con[2]}\nОписание: {con[3]}')
        index += 1
        with open('guide_Bot.txt', 'a') as file:
            file.write(f'\n{contact}')
        
        time = dt.now().strftime('%H:%M')
        with open('log_seminar_10.csv', 'a') as file:
            file.write(f'{time};Add contact;{contact}\n')
    else:
        return ConversationHandler.END


def cancel(update, context):
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
button_start_handler = CallbackQueryHandler(button_start)
cancel_handler = CommandHandler('cancel', cancel)
print_all_kid_handler = MessageHandler(Filters.text, print_all_kid)



message_handler_search = MessageHandler(Filters.text, message_search)
message_handler_save = MessageHandler(Filters.text, message_save)

conv_handler = ConversationHandler(
    entry_points=[start_handler, button_start_handler],

    states={
        VIEW_ALL: [print_all_kid_handler],
        SEARCH_KID: [message_handler_save]
    },

    fallbacks=[cancel_handler]
)

dispatcher.add_handler(conv_handler)

print('Бот запущен')
updater.start_polling()
updater.idle()
print('Бот остановлен')