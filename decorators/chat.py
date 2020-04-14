#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''
Binds a function to private chats only
'''
def only_private(fn):
	def wrapper(*args,**kwargs):
		message = args[0].message
		if message.chat.type == 'private':
			return fn(*args,**kwargs)
		else:
			return False
	return wrapper

'''
Binds a function to groups only
'''
def only_groups(fn):
	def wrapper(*args,**kwargs):
		message = args[0].message
		if message.chat.type != 'private':
			return fn(*args,**kwargs)
		else:
			return False
	return wrapper