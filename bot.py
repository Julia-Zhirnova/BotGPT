from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

async def start(update, context):
    text = load_message("main")
    await send_photo(update, context, "main")
    await send_text(update, context, text)

# тут будем писать наш код :)
async def hello(update, context):
    await send_text(update, context, "Привет!")
    await send_text(update, context, "Ты написал " + update.message.text)

    await send_photo(update, context, "avatar_main")
    await send_text_buttons(update, context, "Выберите режим работы", {  # Текст перед кнопкой
        "btn_start": " Старт ", # Текст и команда кнопки "Старт"
        "btn_stop": " Стоп "  # Текст и команда кнопки "Стоп"
    })
    

async def hello_button(update, context):
    query = update.callback_query.data   #код кнопки
    await update.callback_query.answer() #помечаем что обработали нажатие на кнопку
    #await send_text(update, context, "Вы нажали на кнопку " + query)
    if query == "btn_start":
        await send_text(update, context, "Процесс запущен")
    else:
        await send_text(update, context, "Процесс остановлен")


app = ApplicationBuilder().token("6914623824:AAG2rJrLgGKSg1RxqklhiwQzMP5E8n4ZlVA").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
app.add_handler(CallbackQueryHandler(hello_button))
app.run_polling()
