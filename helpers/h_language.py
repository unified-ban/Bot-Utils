#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from Utils import logger
import unicodedata

'''
Check for non-west characters in text
Credits: tzot, John Machin
<https://stackoverflow.com/a/3308844>
'''

latin_chars = {}

def is_latin(uchr):
	try: return latin_chars[uchr]
	except KeyError:
		return latin_chars.setdefault(uchr, 'LATIN' in unicodedata.name(uchr))

def only_roman_chars(unistr):
	try:
		return all(is_latin(uchr)
			for uchr in unistr
			if uchr.isalpha())
	except Exception as e:
		logger.exception(e)