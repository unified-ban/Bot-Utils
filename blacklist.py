#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from . import sql, logger
from telegram.error import TelegramError

'''
Synchronize the chat with the blacklist
'''
def sync(update, context):
	try:
		bot = context.bot
		
		db = sql.Database(update)
		blacklist = db.get_blacklist()
		chat_id = update.message.chat_id
		counter = 0
		
		for user in blacklist:
			counter+=1
			if counter % 10 == 0:
				time.sleep(2)
			try:
				bot.kick_chat_member(chat_id, user[0])
			except Exception as e:
				pass
		return counter
	except Exception as e:
		logger.exception(e)
