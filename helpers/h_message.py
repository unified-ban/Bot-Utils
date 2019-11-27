#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from Utils import logger
import time

'''
Delete bot output
The delay variable defines the number in seconds to 
wait before performing the operation (default is 0).
'''
def delete(update, context, delay=0):
	try:
		bot = context.bot
		
		try:
			message_id = update.message_id
			chat_id = update.chat_id
		except AttributeError as e:
			message_id = update.message.message_id
			chat_id = update.message.chat_id
		if delay > 0:
			time.sleep(delay)
		return bot.deleteMessage(chat_id, message_id)
	except Exception as e:
		logger.exception(e)