from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler

bot_token = '5561873128:AAHMMJjfipo0ehD-MjNmuKKn53My9jRPE8E'

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher




# def start(update, context):
#     context.bot.send_message(update.effective_chat.id, "Добрый день!")


# # def message(update, context):
# #     text = update.message.text
# #     context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
# #     return text

# start_handler = CommandHandler('start', start)
# # message_handler = MessageHandler(Filters.text, message)

# dispatcher.add_handler(start_handler)
# # dispatcher.add_handler(message_handler)


print('Бот запущен')
updater.start_polling()
updater.idle()
print('Бот остановлен')
