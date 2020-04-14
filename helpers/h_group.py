#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import Languages
from Utils import sql

'''
Get group language from config
'''
def get_language(update):
	try:
		db = sql.Database(update)
		group = db.get_groups()
		return getattr(Languages, group[18])
	except:
		return Languages.en_US