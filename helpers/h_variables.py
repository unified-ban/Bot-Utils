#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''
Set {variables} with values
'''
def define(text, variables):
	for var in variables:
		if var[0] in text:
			text = text.replace(var[0], var[1])
	return text