from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler


bot = Bot(token='5253182574:AAEH-NbpIzWxpYokgHcvA_RDtJjUJb2FOmQ')
updater = Updater(token='5253182574:AAEH-NbpIzWxpYokgHcvA_RDtJjUJb2FOmQ', use_context=True)
dispatcher = updater.dispatcher

START = 0
BIO = 1
PHOTO = 2


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введи мнимую часть: ')

    return START


def input_data_1(update, context):
    global first_number
    first_number = update.message.text
    print(first_number)
    context.bot.send_message(update.effective_chat.id, 'Введи действительную часть: ')

    return BIO


def input_data_2(update, context):
    global second_number
    second_number = update.message.text
    print(second_number)
    context.bot.send_message(update.effective_chat.id, 'Введи действие: ')

    return PHOTO


def photo(update, context):
    text = update.message.text
    if text == '+':
        context.bot.send_message(update.effective_chat.id, f'{int(second_number) + int(first_number)}')


def cancel(update, context):
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
first_handler = MessageHandler(Filters.text, input_data_1)
second_handler = MessageHandler(Filters.text, input_data_2)
cancel_handler = CommandHandler('cancel', cancel)
photo_handler = MessageHandler(Filters.text, photo)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={START: [first_handler],
                                           BIO: [second_handler],
                                           PHOTO: [photo_handler]},

                                   fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()