#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''
Check if chat is private
'''
def is_private(update):
	if update.message.chat.type == 'private':
		return True
	else:
		return False

'''
Check if chat group is private
'''
def is_private_group(update):
	if update.message.chat.username is None:
		return True
	else:
		return False