#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import Params
from telegram import ParseMode
from Utils import file
import logging, os, shutil, datetime, sys, traceback

'''
Create a timestamp from the current datetime 
to be used in the log file.
'''
current_datetime = datetime.datetime.now().strftime("%B-%d-%Y--%I:%M%p")


'''
Load language from settings.
Choose your preferred language in Params.settings.
'''
lang = Params.settings.language


'''
Create new logging handler.
'''
log = logging.getLogger(Params.common.log_name)
hdlr = logging.FileHandler(Params.path.log)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
log.addHandler(hdlr)
log.setLevel(logging.INFO)


'''
Move the old log file to the Logs folder with 
current_datetime as the name. Create the new 
log file for the instance and set header 
from the language file.
'''
def start():
	shutil.move(Params.path.log, (Params.path.log_backup % current_datetime))
	os.mknod(Params.path.log)
	return file.add_line(Params.path.log, (lang.log_file_header % current_datetime))


def extract_function_name():
	tb = sys.exc_info()[-1]
	stk = traceback.extract_tb(tb, 1)
	fname = stk[0][3]
	return fname


def exception(e):
	exc_type, exc_obj, exc_tb = sys.exc_info()
	file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	log.error(
	"File: {file} Line: {line}\n\
'------> Function: [{function_name}] raised {exception_class} ({exception_docstring}): {exception_message}".format(
		line = exc_tb.tb_lineno,
		file = file_name,
		function_name = extract_function_name(),
		exception_class = e.__class__,
		exception_docstring = e.__doc__,
		exception_message = e)
	)


'''
Submit a new report to the channel. Configure the 
channel ID in Params.telegram.ReportChannel.id.
User Reports are sent on the channel specified in 
the group settings.
'''
def report(update, context, text):
	bot = context.bot

	hash_code = '#UB' + str(update.message.chat_id)[1:]
	bot.send_message(Params.telegram.ReportChannel.id, lang.report % (text, hash_code), parse_mode=ParseMode.HTML)


'''
Submit a new report to the operatos group.
'''
def report_operators(update, context, text):
	bot = context.bot
	
	hash_code = '#UB' + str(update.message.chat_id)[1:]
	bot.send_message(Params.telegram.OperatorsGroup.id, lang.report_operators % (text, hash_code), parse_mode=ParseMode.HTML)