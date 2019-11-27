#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

def is_set(update):
	if update.message is not None and update.message.text is not None:
		text = update.message.text.split(" ")
		if len(text) == 1:
			if text[0].startswith("#"):
				return text[0]
	return False