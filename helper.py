import os
import sys
import json
import nltk
import re
import nameparser
import Checker



from nameparser import HumanName


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.metrics import jaccard_distance


data = json.load(open('gg2013.json'))
regex_remove = r'^RT\s|\sRT|(?i)goldenglobes|(?i)golden\sglobes'
regex_remove_rt = '^RT @\w+: '
regex_remove_link = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
regex_remove_gg = '#GoldenGlobes'
checker = Checker.checker('Golden Globes', 2013)

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


def dataSearch2(regex1, regex2):
    l = []

    for i in data:
        t = i['text']
        u = i['user']
        if re.search(regex1, t) and re.search(regex2, t) and u['screen_name'] != 'goldenglobes':
            t = re.sub(regex_remove_rt, '', t)
            t = re.sub(regex_remove_link, '', t)
            t = re.sub(regex_remove_gg, '', t)
            nltk_output = pos_tag(word_tokenize(t))
            # print(nltk_output)
            # l.append([nltk_output,re.split(regex2,t)])
            l.append([nltk_output,t])
            # printTweet(t)
            # for line in nltk_output:                
                # if type(line) == Tree:
                #     name = ''
                #     for nltk_result_leaf in line.leaves():
                #         name += nltk_result_leaf[0] + ' '
                #     l.append(re.sub(r'\s+$','',name))
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


def print_helper(l):
    for i in l:
        print()
        # for j in i:
        #     print(j)
        print(i[1])
        print()

def get_outliers(d):
    values = list(d.values())
    mean_value = sum(values) / len(values)
    return {key:value for (key, value) in d.items() if value > mean_value}

def actorFilter(d):
    vals = [value for value in d if checker.checkActor(value)]
    return vals

def movieFilter(d):
    vals = {key:value for (key, value) in d.items() if checker.checkMovie(key)}
    return vals