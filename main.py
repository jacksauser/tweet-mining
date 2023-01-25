import os
import sys
import json
import nltk
import re


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.metrics import jaccard_distance

# collecting the award show queried and year
award_show = input("What award show? ")
year = input("What year of the "+award_show+"? ")

if not award_show:
    award_show = "Golden Globes"

if not year:
    year = 2013
else:
    year = int(year)



#opening the data
data = json.load(open('gg2013.json'))



regex_host = r'(?i)host'
regex_award  = r'(?i)award for'
regex_presenter = r'(?i)presenter'
regex_nominee = r'(?i)nominee'
regex_winner = r'(?i)winner|won'
regex_remove = r'^RT\s|\sRT|^@\w+\s|(?i)goldenglobes|(?i)golden\sglobes'
regex_best = r'(?i)best'



# can't use
regex_bmp = r'(?i)Best Motion Picture'

host_names_potential = []


for i in data:
    t = i['text']
    u = i['user']
    if re.search(regex_best, t) and re.search(regex_award, t) and u['screen_name'] != 'goldenglobes':
        t = re.sub(regex_remove, '', t)
        nltk_output = ne_chunk(pos_tag(word_tokenize(t)))
        # print(t)
        # print()
        # print('-----------------------------------------------')
        # print()
        for line in nltk_output:
            if type(line) == Tree:
                name = ''
                for nltk_result_leaf in line.leaves():
                    name += nltk_result_leaf[0] + ' '
                host_names_potential.append(re.sub(r'\s+$','',name))
                # print ('Name: ', name)



# counting name freq
host_dict = {}
for i in host_names_potential:
    if re.search(regex_best, i):
        if i in host_dict:
            host_dict[i] += 1
        else:
            host_dict[i] = 1

# output_top10 = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True)[:10])

# print(output_top10)


output_top = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True))

for i in host_names_potential:
    for j in output_top:
        if i in j:
            output_top[j] += 1

print(sorted(output_top.items(), key=lambda item: item[1], reverse=True))





