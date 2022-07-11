from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler
import logging

bot_token = '5561873128:AAHMMJjfipo0ehD-MjNmuKKn53My9jRPE8E'

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, _):
    keyboard = [
        [InlineKeyboardButton("Телефонный справочник", callback_data='1')],
        [InlineKeyboardButton("Информационная система", callback_data='2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Пожалуйста, выберите:',
                              reply_markup=reply_markup)


def message(update, _):
    text = update.message.text
    return text


def button(update, _):
    query = update.callback_query
    variant = query.data

    # `CallbackQueries` требует ответа, даже если
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы.
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
    # редактируем сообщение, тем самым кнопки
    # в чате заменятся на этот ответ.
    query.edit_message_text(text=f"{variant}")


def guide_choice(update, _):
    keyboard = [
        [InlineKeyboardButton("Поиск контакта", callback_data='1')],
        [InlineKeyboardButton("Добавление контакта", callback_data='2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Пожалуйста, выберите:',
                              reply_markup=reply_markup)


# if __name__ == '__main__':

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))


updater.dispatcher.add_handler(MessageHandler(Filters.text, message))
updater.dispatcher.add_handler(CallbackQueryHandler(button))


    
# Запуск бота
updater.start_polling()
updater.idle()
