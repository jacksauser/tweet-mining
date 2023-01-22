import os
import sys
import json
import nltk
import re

# collecting the award show queried and year
award_show = input("What award show? ")
year = input("What year of the "+award_show+"? ")

if not award_show:
    award_show = "Golden Globes"

if not year:
    year = 2013
else:
    year = int(year)


def word_frew(l):
    



#opening the data
data = json.load(open('gg2013.json'))



regex_host = r'(?i)host'
host_strings = []


for i in data:
    t = i['text']
    u = i['user']
    if re.search(regex_host, t) and u['screen_name'] != 'goldenglobes':
        host_strings.append(t)




