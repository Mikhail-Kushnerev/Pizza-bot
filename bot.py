from sequrity import TOKEN
from telebot import TeleBot
from main import Pizza


bot = TeleBot(TOKEN)
handler = Pizza()


@bot.message_handler()
def answer(message):
    bot.send_message(
        message.chat.id,
        handler.get_response(message.chat.id, message.text)
    )


if __name__ == '__main__':
    bot.polling(none_stop=True)
