import time
from telebot import TeleBot

BOT_TOKEN = "PASTE_BOT_TOKEN"
ADMIN_ID = 123456789  # apna telegram id

bot = TeleBot(BOT_TOKEN)

LAST_PC_PING = 0
PC_TIMEOUT = 90

@bot.message_handler(commands=["pc_on"])
def pc_on(message):
    global LAST_PC_PING
    if message.from_user.id == ADMIN_ID:
        LAST_PC_PING = time.time()
        bot.reply_to(message, "🟢 PC ONLINE")

@bot.message_handler(func=lambda m: True)
def auto_reply(message):
    pc_online = (time.time() - LAST_PC_PING) < PC_TIMEOUT
    if pc_online:
        return

    bot.reply_to(
        message,
        "🟡 PC abhi OFF hai\n"
        "🤖 Reply mode active\n"
        "⏳ Checking unavailable"
    )

bot.infinity_polling(skip_pending=True)
