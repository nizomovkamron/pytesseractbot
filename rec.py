
from PIL import Image,ImageEnhance, ImageFilter
 
import pytesseract
import telebot
import os
import sys
import locale
import db
import datetime
import time
import cv2
bot = telebot.TeleBot("1700243571:AAFDOlbgHAacwZiU3HJQPHtKDR641niRpnM")
#print(pytesseract.image_to_string(Image.open('txt.png')).encode('latin-1', 'replace'))
t = time.localtime()
now = datetime.datetime.now().strftime("%S")
nowm = datetime.datetime.now().strftime("%M")
@bot.message_handler(func=lambda message: True)
def foo(message):
	if(message.text=='/start'):
		bot.send_message(message.chat.id,'*Ассалому алайкум! Мен расмдаги матнларни одий матнларга айлантира оламан!\nМенга тиниқ матнли расм юборинг!*',parse_mode='markdown')
		db.newuser(message.chat.id)


@bot.message_handler(content_types=['photo'])		
def foo(message):

	if(db.fetchu(message.chat.id)[0][1]<int(message.date)):
		#print(message.photo[0].file_id)
		bot.send_message(message.chat.id,'Бир дақиқа...')
		file_info = bot.get_file(message.photo[0].file_id)

		downloaded_file = bot.download_file(file_info.file_path)
		rn=file_info.file_path
		

		with open(rn, 'wb') as new_file:

			new_file.write(downloaded_file)
			# im = Image.open(rn)
			# im = im.filter(ImageFilter.MedianFilter())
			# enhancer = ImageEnhance.Contrast(im)
			# im = enhancer.enhance(2)
			# im = im.convert('1')
			# im.save(rn)
			
			config_custom=r'--oem 3 --psm 6'
			img=cv2.imread(rn)
			img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
			try:
				bot.send_message(message.chat.id,pytesseract.image_to_string(img,lang="eng+ara+uzb+rus",config=config_custom))
				db.ins(message.chat.id,int(message.date)+5)
			except Exception:
				bot.send_message(message.chat.id,'Расмда ҳеч нима топа олмадим!\nКўп учрайдиган хатолар:\n* Расмнинг хиралиги\n* Расмнинг ўлчами катталиги\n* Расмдаги матннинг шрифти тўғри келмаётгани')
			
		try:
			os.remove(rn)
		except Exception:
			pass	
	else:
		bot.send_message(message.chat.id,'Расмни ҳар 3 секундда юбориш мумкин! Кутиб туринг...')
		#print(db.fetch(),now)	
		
bot.polling()
