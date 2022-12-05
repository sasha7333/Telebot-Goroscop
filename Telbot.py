import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
bot = telebot.TeleBot('')

x = ['gemini', 'aries', 'taurus', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
content = []
for i in x:
    zapros = requests.get(f'https://horo.mail.ru/prediction/{i}/today/')
    zapros.encoding = 'utf-8'
    if zapros.status_code != 404:
        soup = BeautifulSoup(zapros.text, 'html.parser')
        text = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
        for k in text:
            content.append((i, k.getText()))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "/start":
     bot.send_message(message.from_user.id, "Привет,{0.first_name}!\nCейчас я расскажу тебе гороскоп на сегодня.".format(message.from_user))
     kb = types.InlineKeyboardMarkup()
     kb_oven = types.InlineKeyboardButton(text='♈ Овен', callback_data='gemini')
     kb_telets = types.InlineKeyboardButton(text='♉ Телец', callback_data='aries')
     kb_bliznetsy = types.InlineKeyboardButton(text='♊ Близнецы', callback_data='taurus')
     kb_rac = types.InlineKeyboardButton(text='♋ Рак', callback_data='cancer')
     kb_lev = types.InlineKeyboardButton(text='♌ Лев', callback_data='leo')
     kb_deva = types.InlineKeyboardButton(text='♍ Дева', callback_data='virgo')
     kb_vesy= types.InlineKeyboardButton(text='♎ Весы', callback_data='libra')
     kb_scorpion = types.InlineKeyboardButton(text='♏ Скорпион', callback_data='scorpio')
     kb_strelets = types.InlineKeyboardButton(text='♐ Стрелец', callback_data='sagittarius')
     kb_koserog = types.InlineKeyboardButton(text='♑ Козерог', callback_data='capricorn')
     kb_vodoley = types.InlineKeyboardButton(text='♒ Водолей', callback_data='aquarius')
     kb_riby = types.InlineKeyboardButton(text='♓ Рыбы', callback_data='pisces')
     kb.add(kb_oven, kb_telets, kb_bliznetsy, kb_rac, kb_lev, kb_deva, kb_vesy, kb_scorpion, kb_strelets,kb_vodoley, kb_riby)
     bot.send_message(message.from_user.id, text="Выбери свой знак зодиака", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
   for m in content:
      if call.data == m[0]:
          msg = m[1]
          if call.data == 'gemini':
           kb_oven = types.InlineKeyboardMarkup()
           kb_o_oven = types.InlineKeyboardButton(text='♈ OBEH', callback_data='o_oven')
           kb_oven.add(kb_o_oven)
           bot.send_message(call.message.chat.id,msg, reply_markup=kb_oven)
          if call.data == 'aries':
           kb_telets = types.InlineKeyboardMarkup()
           kb_o_telets = types.InlineKeyboardButton(text='♉ ТЕЛЕЦ', callback_data='o_telets')
           kb_telets.add(kb_o_telets)
           bot.send_message(call.message.chat.id,msg, reply_markup=kb_telets)
          if call.data == 'taurus':
           kb_bliznetsy = types.InlineKeyboardMarkup()
           kb_o_bliznetsy = types.InlineKeyboardButton(text='♊ БЛИЗНЕЦЫ', callback_data='o_bliznetsy')
           kb_bliznetsy.add(kb_o_bliznetsy)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_bliznetsy)
          if call.data == 'cancer':
           kb_rac = types.InlineKeyboardMarkup()
           kb_o_rac = types.InlineKeyboardButton(text='♋ РАК', callback_data='o_rac')
           kb_rac.add(kb_o_rac)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_rac)
          if call.data == 'leo':
           kb_lev = types.InlineKeyboardMarkup()
           kb_o_lev = types.InlineKeyboardButton(text='♌ ЛЕВ', callback_data='o_lev')
           kb_lev.add(kb_o_lev)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_lev)
          if call.data == 'virgo':
           kb_deva = types.InlineKeyboardMarkup()
           kb_o_deva = types.InlineKeyboardButton(text='♍ ДЕВА', callback_data='o_deva')
           kb_deva.add(kb_o_deva)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_deva)
          if call.data == 'libra':
           kb_vesy = types.InlineKeyboardMarkup()
           kb_o_vesy = types.InlineKeyboardButton(text='♎ ВЕСЫ', callback_data='o_vesy')
           kb_vesy.add(kb_o_vesy)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_vesy)
          if call.data == 'scorpio':
           kb_scorpion = types.InlineKeyboardMarkup()
           kb_o_scorpion = types.InlineKeyboardButton(text='♏ СКОРПИОН', callback_data='o_scorpion')
           kb_scorpion.add(kb_o_scorpion)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_scorpion)
          if call.data =='sagittarius':
           kb_strelets = types.InlineKeyboardMarkup()
           kb_o_strelets = types.InlineKeyboardButton(text='♐ СТРЕЛЕЦ', callback_data='o_strelets')
           kb_strelets.add(kb_o_strelets)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_strelets)
          if call.data =='capricorn':
           kb_koserog = types.InlineKeyboardMarkup()
           kb_o_koserog = types.InlineKeyboardButton(text='♑ КОЗЕРОГ', callback_data='o_koserog')
           kb_koserog.add(kb_o_koserog)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_koserog)
          if call.data =='aquarius':
           kb_vodoley = types.InlineKeyboardMarkup()
           kb_o_vodoley = types.InlineKeyboardButton(text='♒ ВОДОЛЕЙ', callback_data='o_vodoley')
           kb_vodoley.add(kb_o_vodoley)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_vodoley)
          if call.data =='pisces':
           kb_riby = types.InlineKeyboardMarkup()
           kb_o_riby = types.InlineKeyboardButton(text='♓ РЫБЫ', callback_data='o_riby')
           kb_riby.add(kb_o_riby)
           bot.send_message(call.message.chat.id,msg,reply_markup=kb_riby)

bot.polling(none_stop=True,interval=0)
