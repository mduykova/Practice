import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют:\n/values'
    bot.reply_to(message, text)
    
    
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)
    
    
@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        
        if len(values) != 3:
                raise ConvertionException('Неверное количество параметров.')
            
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        a = float(total_base)
        b = float(amount)
        c = a*b
        text = f'Цена {amount} {quote} в {base} - {c}'
        bot.send_message(message.chat.id, text)        
        
bot.polling()
    
