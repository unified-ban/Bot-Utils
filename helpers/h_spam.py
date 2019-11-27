#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time, re, datetime, os, requests, imagehash
from urllib import request
from urlextract import URLExtract
from telegram.error import TelegramError
from Utils import logger, sql
from Utils.helpers import h_message
from PIL import Image
from io import BytesIO
import Params

'''
Perform group defined spam action
'''
def perform_group_spam_action(update, context, actions):
	logger.log.info("perform_group_spam_action")
	try:
		bot = context.bot

		message = update.message
		user = update.message.from_user
		
		# limit
		if actions[0] == 1:
			bot.restrict_chat_member(
				message.chat_id, 
				user.id,
				datetime.datetime.now() + datetime.timedelta(days=1)
			)
		# ban
		if actions[1] == 1:
			bot.kick_chat_member(message.chat_id, user.id)
		# delete
		if actions[2] == 1:
			h_message.delete(update, context)
	except Exception as e:
		logger.exception(e)

'''
Set new user as update author
'''
def set_correct_user(update):
	try:
		for new in update.message.new_chat_members:
			update.message.from_user.id = new.id
			update.message.from_user.name = str(new.username)
			update.message.from_user.first_name = str(new.first_name)
			update.message.from_user.last_name = str(new.last_name)
		return update
	except Exception as e:
		# logger.exception(e)
		pass

'''
Get Telegram domains from text
'''
def get_telegram_domains(update, username=False):
	try:
		extractor = URLExtract()
		extractor.update()
		if username:
			new = ""
			for new in update.message.new_chat_members:
				new = '{name} {surname}'.format(
					name = str(new.first_name),
					surname = str(new.last_name)
				)
			text = '{message} {name} {surname} {new}'.format(
				message = update.message.text,
				name = str(update.message.from_user.first_name),
				surname = str(update.message.from_user.last_name),
				new = new
			)
		else:
			text = update.message.text
		if text is not None and text is not "":
			domains = re.findall("[@]\w+", text)
			domains = ['https://t.me/{0}'.format(domain[1:]) for domain in domains]
			domains = domains + extractor.find_urls(text)
			for i, domain in enumerate(domains):
				if not domain.startswith('http'):
					domains[i] = "http://{0}".format(domain)
			return domains
		else:
			return []
	except Exception as e:
		logger.exception(e)

'''
Check if text is Telegram domain
'''
def is_telegram_domain(text):
	try:
		try:
			data = request.urlopen(text) 
		except:
			return False
		source = ""
		for row in data: 
			source = source+str(row)
		if 'tgme_page_extra' in source and 'members' in source:
			return True
		else:
			return False
	except Exception as e:
		logger.exception(e)

'''
Spam Logics
'''
'''
Text contains words
'''
def logic_containsWords(update, params):
	try:
		params = params.split(",")
		texts = ""
		
		if update.message.text is not None:
			texts = texts + " " + str(update.message.text).lower()
		
		count = len(params)
		p_count = 0
		
		for p in params:
			if p in texts:
				p_count += 1
		
		if count == p_count:
			return True
		else:
			return False
		
		return False
	except Exception as e:
		# logger.exception(e)
		pass

'''
Compare image hash with source hash
'''
def logic_imageComparison(update, context, sources):
	try:
		bot = context.bot

		if update.message is not None and update.message.photo is not None:
			for source in sources.split(","):
				source = Params.path.dataset_spamlogics_images + source
				file_id = update.message.photo[0].file_id
				image = requests.get(bot.get_file(file_id).file_path)
				
				image_hash = imagehash.average_hash(Image.open(BytesIO(image.content)))
				source_hash = imagehash.average_hash(Image.open(source))
				
				if source_hash - image_hash <= 3:
					return True
		
		return False
	except Exception as e:
		logger.exception(e)
		pass
