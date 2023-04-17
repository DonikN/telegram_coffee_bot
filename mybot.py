import telebot

TOKEN = "YOUR_BOT_API_TOKEN"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.from_user.username == "coffeeusesbot" and "повтори" in message.text.lower())
def delete_example_messages(message):
    bot.delete_message(message.chat.id, message.message_id)

bot.polling()
