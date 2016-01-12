#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>JPY to NTD</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>wwwins</bitbar.author>
# <bitbar.author.github>wwwins</bitbar.author.github>
# <bitbar.desc>Japanese Yen to Taiwan New Dollar Rate</bitbar.desc>
# <bitbar.image></bitbar.image>

import time
import requests
from lxml import html

# Setting your currency buying/selling rate
BUY_RATE = 0.270
color = "cadetblue"

if (int(time.strftime("%H")) > 17):
	print ('🈚️')
	exit()

if (int(time.strftime("%H")) < 9):
	print ('🈚️')
	exit()

r = requests.get("http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm")
doc = html.fromstring(r.text)
content = doc.cssselect("div.entry-content")
jpy = content[0][1][9][2].text
if (float(jpy) < BUY_RATE):
	color = "red"

print ('JPY:'+jpy+'| color='+color)
