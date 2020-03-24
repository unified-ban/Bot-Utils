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
Define a function that requires operator permissions.
'''
def is_operator(scope):
	def decorator(fn):
		def wrapper(*args,**kwargs):
			user = args[0].message.from_user
			if user.id in Params.operators.users:
				return fn(*args,**kwargs)
			else:
				return False
		return wrapper
	return decorator


'''
Define a function that requires privileged operator permissions.
'''
def is_privileged_operator(scope):
	def decorator(fn):
		def wrapper(*args,**kwargs):
			user = args[0].message.from_user
			if user.id in Params.operators.privileged_users:
				return fn(*args,**kwargs)
			else:
				logger.log.warning(lang.no_permissions % (user, 'privileged_operator', scope))
				return False
		return wrapper
	return decorator


'''
Define a function that requires admin permissions.
Operators are recognized as admin by the bot.
'''
def is_admin(scope):
	def decorator(fn):
		def wrapper(*args,**kwargs):
			bot = args[1].bot
			user = args[0].message.from_user
			chat_id = args[0].message.chat_id
			if bot.get_chat_member(chat_id, user.id).status in ["creator", "administrator"] or user.id in Params.operators.users:
				return fn(*args,**kwargs)
			else:
				logger.log.warning(lang.no_permissions % (user, 'admin', scope))
				return False
		return wrapper
	return decorator