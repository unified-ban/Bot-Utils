#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

class Colors():
	title = '\033[95m'
	info = '\033[94m'
	ok = '\033[92m'
	warn = '\033[93m'
	fail = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	endc = '\033[0m'
	
	def remove(self, text):
		ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
		return ansi_escape.sub('', text)