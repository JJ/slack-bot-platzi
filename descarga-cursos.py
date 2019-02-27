#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pprint
import json
import re

pp = pprint.PrettyPrinter(indent=4)
page = urlopen('http://platzi.com/agenda').read()
soup = BeautifulSoup( page, "lxml" )
agenda = soup.find_all('script')[25].text

schedule = re.findall( r'scheduleItems: (.+?),\n', agenda )
datos = json.loads(schedule[0])
print(json.dumps(datos))
