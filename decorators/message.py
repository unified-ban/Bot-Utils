#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''
Delete input (user) message after function execution
'''
def delete_input(fn):
	def wrapper(*args,**kwargs):
		bot = args[1].bot
		message = args[0].message
		bot.deleteMessage(message.chat.id, message.message_id)
		return fn(*args,**kwargs)
	return wrapper