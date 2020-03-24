#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import Params
from Utils import logger, file

'''
Check if link is phishing
'''
def is_phishing(text):
	try:
		data = open(Params.path.dataset_phishing).read().splitlines()
		if text:
			rows = text.split(" ")
			if rows is not None:
				for row in rows:
					if row in data:
						# logger.log.info(data.index(row))
						return row
			return False
		return False
	except Exception as e:
		logger.exception(e)
