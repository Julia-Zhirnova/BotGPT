from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

# тут будем писать наш код :)


app = ApplicationBuilder().token("telegram-token").build()
app.run_polling()
