#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''
Add a new line at the file beginning.
'''
def add_line(filename, line):
	with open(filename, 'r+') as f:
		content = f.read()
		f.seek(0, 0)
		return f.write(line.rstrip('\r\n') + '\n' + content)

'''
Get content from file as list
'''
def list_file(path):
	with open(path) as f:
		data = f.readlines()
		data = [x.strip() for x in data] 
		return data
	
