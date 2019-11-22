from telegram.ext import Updater, CommandHandler


def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('694637108:AAEAX7cS0nGqgCgv0u_uN9Co6yS-zKviO8s', use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()