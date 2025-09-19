import telebot

TOKEN = "7939983723:AAEWvDzmKCAmL6-yopq-JHW8h7y5w05hreQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
   bot.reply_to(message, "айоу")

print("бот опущен")
bot.infinity_polling()
