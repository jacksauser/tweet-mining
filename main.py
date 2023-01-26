import os
import sys
import json
import nltk
import re
import nameparser


from nameparser import HumanName


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.metrics import jaccard_distance



def dataSearch(regex):
    l = []

    for i in data:
        t = i['text']
        u = i['user']
        if re.search(regex, t) and u['screen_name'] != 'goldenglobes':
            t = re.sub(regex_remove, '', t)
            nltk_output = ne_chunk(pos_tag(word_tokenize(t)))
            # printTweet(t)
            for line in nltk_output:
                if type(line) == Tree:
                    name = ''
                    for nltk_result_leaf in line.leaves():
                        name += nltk_result_leaf[0] + ' '
                    l.append(re.sub(r'\s+$','',name))
    return l

def dataSearchAward(regex, l):

    if type(l) != list:
        ValueError("Data Search with award - Second argument must be a list")
    
    retA = []
    retB = {}
    
    for i in data:
        t = i['text']
        u = i['user']
        
        if re.search(regex, t) and u['screen_name'] != 'goldenglobes':
            for j in l:
                award = "(?i)" + j.replace(' ','\s')
                if re.search(award.encode().decode('unicode_escape'), t):
                    t = re.sub(regex_remove, '', t)
                    nltk_output = ne_chunk(pos_tag(word_tokenize(t)))
                    # printTweet(t)
                    for line in nltk_output:
                        if type(line) == Tree:
                            name = ''
                            for nltk_result_leaf in line.leaves():
                                name += nltk_result_leaf[0] + ' '
                            retA.append((re.sub(r'\s+$','',name),j))
                            
                            if j in retB:
                                retB[j] += 1
                            else:
                                retB[j] = 1
    return retA, retB

def getDistribution(l, regex = ".*"):
    dict_ = {}
    for i in l:
        if type(i) == tuple:
            s = i[0] + " -- "+i[1]
            if re.search(regex, s):
                if s in dict_:
                    dict_[s] += 1
                else:
                    dict_[s] = 1
        else:
            if re.search(regex, i):
                if i in dict_:
                    dict_[i] += 1
                else:
                    dict_[i] = 1
    ret = dict(sorted(dict_.items(), key=lambda item: item[1], reverse=True))
    return ret


def printTweets(t):
    print(t)
    print()
    print('-----------------------------------------------')
    print()


def isFullName(s, l = []):
    # human_name = HumanName(s)
    # if human_name.first and human_name.last:

    name = s.split(" -- ")[0]
    if re.search("\w+\s+\w+",name) and name not in l:
        # print(s)
        return True
    else:
        return False

def getNames(d, l = []):
    new_d = {}
    for i in d.keys():
        if isFullName(i, l):
            new_d[i] = d[i]
    return new_d

def isBest(s):
    if re.search(r'(?i)best\s',s):
        # print(s)
        return True
    else:
        return False

def getAwards(d):
    new_d = {}
    for i in d.keys():
        if isBest(i):
            new_d[i] = d[i]
    return new_d

# collecting the award show queried and year
award_show = input("What award show? ")
year = input("What year of the "+award_show+"? ")


# autofill inputs is not specified 
if not award_show:
    award_show = "Golden Globes"
if not year:
    year = 2013
else:
    year = int(year)


#opening the data
data = json.load(open('gg2013.json'))


# regex list 
regex_host = r'(?i)the\shosts'
regex_award  = r'(?i)award for'
regex_presenter = r'(?i)presenter'
regex_nominee = r'(?i)nominee for'
regex_winner = r'(?i)winner|won'
regex_remove = r'^RT\s|\sRT|(?i)goldenglobes|(?i)golden\sglobes'
regex_best = r'(?i)best'
regex_should = r'(?i)should\shave\swon|should\'ve\swon'



host = getNames(getDistribution(dataSearch(regex_host)))

awards = getAwards(getDistribution(dataSearch(regex_award)))


potential_winner_list, award_numbers = dataSearchAward(regex_winner, awards.keys())
potential_winners = getNames(getDistribution(potential_winner_list), awards.keys())
real_awards = award_numbers.keys()






print()
print()
print(host)
print()
print()
print(real_awards)
print()
print()
print(potential_winners)









# output_top10 = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True)[:10])

# print(output_top10)


# output_top = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True))

# for i in host_names_potential:
#     for j in output_top:
#         if i in j:
#             output_top[j] += 1

# print(sorted(output_top.items(), key=lambda item: item[1], reverse=True))




