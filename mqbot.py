#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import telegram.bot
from telegram.ext import messagequeue as mq

class MQBot(telegram.bot.Bot):
	
	def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
		super(MQBot, self).__init__(*args, **kwargs)
		self._is_messages_queued_default = is_queued_def
		self._msg_queue = mqueue or mq.MessageQueue()
	
	def __del__(self):
		try:
			self._msg_queue.stop()
		except:
			pass
		super(MQBot, self).__del__()
	
	@mq.queuedmessage
	def send_message(self, *args, **kwargs):
		return super(MQBot, self).send_message(*args, **kwargs)
