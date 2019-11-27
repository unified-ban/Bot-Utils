#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re
import Params
import base64
from Utils import logger
import unicodedata

'''
Check if user name is RTL
'''
def is_rtl(user):
	try:
		texts = [
			str(user.first_name),
			str(user.last_name)
		]
		for text in texts:
			x = len([None for ch in text if unicodedata.bidirectional(ch) in ('R', 'AL')])/float(len(text))
			if x > 0.5:
				return True
		return False
	except Exception as e:
		logger.exception(e)

'''
Get User_ID between brackets from text
'''
def get_user_id(text):
	return re.search('{{(.*)}}', text).group(1)

'''
Get target User_ID between brackets from text
'''
def get_target_user_id(text):
	for line in text.split("\n"):
		if line.startswith("User_ID:"):
			return line[9:]
	
'''
Get User Name
'''
def get_user_name(update):
	try:
		if hasattr(update, 'message'):
			if update.message.reply_to_message is not None:
				if update.message.reply_to_message.forward_from is not None:
					user = update.message.reply_to_message.forward_from
				else:
					user = update.message.reply_to_message.from_user
			elif 0 < len(update.message.new_chat_members):
				user = update.message.new_chat_members[0]
			elif hasattr(update, 'from_user'):
				user = update.from_user
			else:
				user = update.message.from_user
				
			if user.name is not None:
				return str(user.name)
			else:
				if user.first_name is not None:
					first = user.first_name
				else:
					first = ""
				if user.last_name is not None:
					last = user.last_name
				else:
					last = ""
				return str("{first_name} {last_name}".format(
					first_name = first,
					last_name = last))
		else:
			return ""
	except Exception as e:
		logger.exception(e)
		