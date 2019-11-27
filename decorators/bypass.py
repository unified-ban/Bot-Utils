#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import Params
from Utils import logger

'''
Load language from settings.
Choose your preferred language in Params.settings.
'''
lang = Params.settings.language


'''
Define a function that admin and operators can bypass
'''
def has_privileges(fn):
	def wrapper(*args,**kwargs):
		try:
			user = args[0].message.from_user
			message = args[0].message
			chat_id = message.chat.id
			bot = args[1].bot
			user_status = bot.get_chat_member(chat_id, user.id).status
			if user_status in ["creator", "administrator"] or user.id in Params.operators.users or user.id == Params.telegram.Telegram.id:
				return False
			else:
				return fn(*args,**kwargs)
		except Exception as e:
			logger.exception(e)
	return wrapper