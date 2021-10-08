try:
	import telebot, vk_api, threading, random, vk_captchasolver as vc, time, os
	from telebot import types
	bot = telebot.TeleBot('2049821280:AAEBvrF2tAj1JllbzVC-KrBc5qhqZy5R6gg')

	cl = types.ReplyKeyboardMarkup(resize_keyboard=True)
	u = types.KeyboardButton('Спам 📲')
	cl.add(u)

	cll = types.ReplyKeyboardMarkup(resize_keyboard=True)
	uu = types.KeyboardButton('Назад ↩')
	cll.add(uu)

	def sms(message, smska):
		bot.send_message(message, str(smska))
	nah = 0
	zap = ''
	yes = 0

	def spam(sms, her, rrr):
		akki = ['18a39721b48d43c6218f9251f866a4e6d6be90909021e881eff47b27c962f6387d46482decf3bb3098a1c', 
			'6b9d81a789b3b05a138f564ecbd540b2be842aaa5dcb7d853459c8105c504083866b339e23974ae51144b', 
			'd9d5b9bcfff3080ccfece55601c1ecff12393a62db33841e31075f9b6a0aadd1d310821c47399386a84ed', 
			'77625ee8e87de77bda8fb5b2544fe9de564050c7d894c61563fcf03b7262cea2b7b860e499b99954bd0d5', 
			'262783665ef07bcd2c6b046aa24a76ae2fde709fedd8fb9a03bd3a1b611b1f4651ec4cd64d448075b9c3c',
			'b5835bc57cc448317c26bfacda979e68b135c87f0f76be694c77c468a1304553033ad03cadcd9f1d75769',
			'f934536a613016d78ae189e8ed7cfdd7b83605d13aeeb406d6a9e6b8353296344a2b657f584e911d7d0b3',
			'93d4bc1f6e4faadc655e925d9940ebf86a4f23e158ae35d9918c535c5942dd411b1dd6aa3f6946256f792',
			'38c329815cbf2d0a519bb147bb28a042acea143fb2a0b7a652105286445ce18de19932e2d1daa7910b5fc',
			'a0d80a46a972c837c8b2f5cc7ac1f50d0c8afa9a43f7ce469ec56cda43964356588ed7a9ff5d58196db7d',
			'bf40d67915900770bec151817fa0ae908c135705a5ca43a7f1c635bb43d06d8e722cec5f21e4aff7e8b34',
			'28f658caf7a6abb2f5e92775c5c3087b472c5d6b90edba20b8bfbee1e7826114256037be5b652a45a3254',
			'a740dbb9ec710eb5160e874e8bd9c055ea57c4b68eefbd12389e12938ce580ac84fa297bdebbdd43516f2',
			'f9bb5945076ca42d3e2ef06f9b33a250ad568c84493084c09ebe628c32f20141125ca328df057e275fc3a',
			'470e23d951e72304745ebc975308d8bd2811032424f8b9286e56443bb9bda202ab098843db7c940127868',
			'95687e6a13a1f2e143ae6b16ddb61f373d420a84763f6be846e82d33820a2caae690ac12c818197791f07',
			'4185168f43a7cb59c9105c424b1329fb39bdedd95c3d0767d9d387bd89c1a21ab55da3495bac35c147dfd',
			'0ea777a30749ab9dedebf994fff140b185e11cd47a3469a1d9b48327bc17d73754242f544899cdc497233',
			'2f2e48b220d1731e5afd4f45761674136fd2d9b2f11adc1f623244cdc4fea34c331ac7f9e0dd33d030fb2',
			'082a0f5fc3b33477335bcb2219ea3b783139905f0fbf3845696e788bee609d030bca65ce997ede2b14990',
			'a8dac69b078de1b434af9688ae0a2c40bd192c7c48b29d387239f91f74f5503f972fb6e131d1d8e95c5bc',
			'23fa822424314b2e0c7694f87325ef8e6ea246a74810b21bb9d8b2ff2a9f7a914d5d01b9bd78b45922d3a',
			'a9b197f45b5229ba434fe9858e747e52d12c825f9c2acf8d3ea015a75cfae7b57de182fa30efb6641819c',
			'f903dab8f45a3792efd14402d4e0b322d2e501524feba5e15b0df47fd32dfd1ea17005dfbeb52f7885b65',
			'20be053110b6b8920844331d2d41f73de9aafbeb927ad1ad26b0f96cddb07321e9b959e8a128050972726',
			'bc2b9366b604c392b29795f5a0e07f90050b18272224ef2e61e3baf545cb149983b0500b15a4cd5f2467d',
			'c8898627b49d8e542d9997a0622fad9b381b8a8d6f70455a0ceb97440dc1c938127ea5c8f5dd247f0ff28',
			'bf08c3f05c12cc284bc39766f5bc0b17a4a1bd470457345047a766ae4918107be626a364b2529ae0132e7',
			'30d2c10bb61e130a237ac036443c8de311741af9ececde56c725c1822a418536338b553b7f7c4662f9bd9',
			'b203fd552f3d81a1c5c07cd9c7a52e406284c823cd2cff85e6dc0ec47835f8bde80f3049257491acff37a',
			'c2697c8f98e4d9a2a7a79741bfb268912f077f17365f162c4d0e9efaaf8a43510303189271a2a7dcaa2c4',
			'5bf555a4b2084987fe221a93bc02df1078437adcc82d88729cc0d203ccdf55ad49e7e6c7d813f594b35c3',
			'6798bd38367326fc83ba2aa8a685b6c6cfa95af5d162587967e2226f29808e37138b03620e967e60ca650',
			'0cff6684e7a6e6a4bfb218cb126af53c2cbca8eafe54263fffc3e337c6193ffb05a5aaf103fe1f97e8c06',
			'ea760bd7e6796ea87182cc15871d456ba9d75c5053cee286aa4f4e3d3497d41dd04c97183adb5ae827d38',
			'f842af1e1762599685249851cf9783a8b18bf4b0ead70ea4195d1f4d7a4e4f0c739ddf395233906f87390',
			'5fa074b401b62197066c13d20951503161003a99d9c7201cf2acd00f0bd6dfacbd35c65ef2ce6f6245c0f',
			'5b7216b9b0410a6df680322be4ee376683ce68feca7985590ba5cd0286aba96a3b5767d8c3bc76b2f51b7',
			'd9867fe567cf274db1cb7f08b986a9276e528ab2568b07830d1e63f031f67ad13fc9d7cb3340ade776788',
			'083226a3b6343170a1745ddbf0f9868a6ed573c35cd75d3943b405739a1597bdf33e07b11807564057a3d',
			'b285ced681ea18775d2f183da69976cb3e46b90693af72d1b41543a2ce09a548472821ab5e62df0043ac2',
			'a2e36d010201808dc260bb0cefa2b380a0f6bf33495b02111ebff7d0b9d24766ad0f21eb9f7b96bb3ceac',
			'983aded4c3269a1c70ad05f61c8a3768d3a7c43edc7f32c82c54fb4a07268e7b176473d8a6c75ca0c9a92',
			'f7de9e9642d9b13d3a267c4a71a565a4f6d239140bfa99681ece1f8c4edb1eda74bfe16f6a3124c19968b',
			'32f18fb1e0ddc802809e67675fdd1ec53e85177f43c09871a267d0895a96d47cd9e568203094d3c49433a',
			'23eb25a54b16279a2136f5d399117c9e42e21026e741ba12f0e507dc56ff040a6f54e4ab4eaade596540a',
			'7023f70618aa036d498e3cff4867e3808a970406253d0f9400d8525cd5696d086a60d45d8fe9c87265d88',
			'1a45751a6d140e2be88ece2610bec89b0f9f05774e870cd039767e63e1e9adc837bf81cd6194878fd9888',
			'5a69f741e72344fa6dbc5c46b6d1d6992cffff66b8d5be3c66309c4e0ed9c339a9306db141864b8afbf8a',
			'9f56cde2beb6092120867ce93d22f08d99a17bce37ac494862338ad19d818454da9f246b28c17f02a8653',
			'a0cb440f55c505474acdaa7648cd1b4a84fd0162262d799966715252ae1407e0cf229dcc2cfb01b30c1e0',
			'0a637a0cf0182b4faf17eb71ea534a58b1650c549bc6a1fa3e6c1d1c77aa3da5dd7ed1e75715ee19a2374',
			'f231c0d4466b366c06a4da88f6693c712d4329e3be3cfcea67950b3c708ba3354b01d7f2d079e1e51c3ca']
		global nah
		global yes
		yes = 0
		for i in akki:
			if nah == 3:
				gg = random.choice(sms)
				vk_session = vk_api.VkApi(token=i)
				vk = vk_session.get_api()
				time.sleep(random.randint(2, 7))
				try:
					vk.messages.send(user_id=her, message=str(gg), random_id=0)
					yes +=1
				except vk_api.Captcha:
					cycle = True
					while cycle:
						try:
							vk.messages.send(user_id=her, message=str(gg), random_id=0)
							yes +=1
						except vk_api.Captcha as cptch:
							result_solve_captcha = vc.solve(sid=int(cptch.sid), s=1)
							try:
								cptch.try_again(result_solve_captcha)
								cycle = False
								yes +=1
							except vk_api.Captcha as cptch2:
								pass
						except:
							pass
				except:
					pass
			else:
				bot.send_message(rrr, f'Успешно отправлено: {yes} ✅', reply_markup=cl)
				return
		bot.send_message(rrr, f'Успешно отправлено: {yes} ✅', reply_markup=cl)
		nah = 0

	@bot.message_handler()
	def get_text_messages(message):
	    global nah
	    global zap
	    messages = message.from_user.id
	    mess = message.text.lower()
	    if mess == "/start":
	    	bot.send_message(messages, "Выберите:", reply_markup=cl)
	    elif mess[0:4] == 'спам':
	    	if nah != 3:
		    	bot.send_message(messages, 'Введите СМС через запятую:', reply_markup=cll)
		    	nah = 1
	    	else:
		    	sms(messages, 'Рассылка уже кем-то запущена..')
	    elif mess[0:5] == 'назад':
	    	if nah == 1:
	    		nah = 0
	    	elif nah == 2:
	    		nah = 1
	    	elif nah == 3:
	    		nah = 2
	    	else:
	    		nah = 0
	    	if nah == 0:
	    		bot.send_message(messages, 'Выберите:', reply_markup=cl)
	    	else:
	    		bot.send_message(messages, 'Выберите:', reply_markup=cll)
	    elif nah == 1:
	    	zap = message.text.split(",")
	    	sms(messages, 'Введите ID:')
	    	nah = 2
	    elif nah == 2:
	    	vk_session = vk_api.VkApi(token='18a39721b48d43c6218f9251f866a4e6d6be90909021e881eff47b27c962f6387d46482decf3bb3098a1c')
	    	vk = vk_session.get_api()
	    	ids = str(mess)
	    	prov = vk.users.get(user_ids=ids, fields='can_write_private_message')

	    	her = prov[0]['id']
	    	if prov[0]['can_write_private_message'] == 1:
	    		bot.send_message(messages, 'Спам запущен ✅', reply_markup=cl)
	    		nah = 3
	    		threading.Thread(target=spam, args=(zap, her, messages)).start()
	    	else:
	    		sms(messages, 'СМС закрыты ⛔ \nВведите другой ID.')
	    elif mess == 'stop' or mess == 'стоп':
	    	if nah == 3:
		    	nah = 0
		    	sms(messages, 'Исходное состояние.')
	    	else:
		    	sms(messages, 'Остонавливать нечего.')
	    else:
	    	sms(messages, 'Я тя не понял :/')
	bot.polling(none_stop=True, interval=0)
except:
	os.system('python musor.py')

