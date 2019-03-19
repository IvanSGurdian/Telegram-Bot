from telegram.ext import Updater, CommandHandler
import requests
import re


def GetUrl():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']

    return url

def GetImageUrl():

    # Defines which file extensions to be accepted from API
    allowed_extensions = ['jpg', 'jpeg', 'png']
    file_extension = ''

    while file_extension not in allowed_extensions:
        url = GetUrl()
        file_extension = re.search('([^.]*)$', url).group(1).lower()

    return url

def Bop(bot, update):
    img_url = GetImageUrl()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=img_url)



def Main():
    # Include token in Updater function
    updater = Updater('')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('bop', Bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    Main()
