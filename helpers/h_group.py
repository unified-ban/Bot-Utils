#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import Languages
from Utils import logger, sql
import inspect

'''
Get group language from config
'''
def get_language(update):
	try:
		#logger.log.info("lang---"+inspect.stack()[1][3])
		db = sql.Database(update)
		group = db.get_groups()
		return getattr(Languages, group[18])
	except Exception as e:
		return Languages.en_US
		logger.exception(e)