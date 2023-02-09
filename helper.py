import os
import sys
import json
import nltk
import re
import nameparser
import Checker
import constants as c
import config
from fuzzywuzzy import fuzz



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
stops = ['Oscar', 'Golden', 'Globe', 'Best', 'Actor', 'Award']
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
            # l.append([nltk_output,re.split(regex2,t)]) #!!!Needed for awards and winners
            l.append([nltk_output,t])
            # printTweet(t)
            # for line in nltk_output:                
                # if type(line) == Tree:
                #     name = ''
                #     for nltk_result_leaf in line.leaves():
                #         name += nltk_result_leaf[0] + ' '
                #     l.append(re.sub(r'\s+$','',name))
    return l

def dataSearch3(ls):
    d = {}
    for i in data: 
        t = i['text']
        u = i['user']
        for j in ls:
            if re.search(j, t):
                t = re.sub(regex_remove_rt, '', t)
                t = re.sub(regex_remove_link, '', t)
                t = re.sub(regex_remove_gg, '', t)
                if j in d:
                    d[j].append(t)
                else:
                    d[j] = []
                    d[j].append(t)
    return d

def dataSearchNotSplit(regex1, regex2):
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
            #l.append([nltk_output,re.split(regex2,t)]) #!!!Needed for awards and winners
            l.append([nltk_output,t])
            # printTweet(t)
            # for line in nltk_output:                
                # if type(line) == Tree:
                #     name = ''
                #     for nltk_result_leaf in line.leaves():
                #         name += nltk_result_leaf[0] + ' '
                #     l.append(re.sub(r'\s+$','',name))
    return l


all_names = []

def nameGrabber(l):
    names = []
    for t in l:
        if t in all_names:
           names.append(t)
           continue 
        nltk_output = pos_tag(word_tokenize(t))
        # print(nltk_output)
        if len(nltk_output) == 2 and (nltk_output[0][1] =='NNP' and nltk_output[1][1] =='NNP'):
            names.append(t)
            all_names.append(t)
            continue 
        in_all_names = False
        for n in all_names:
            if n in t:
                names.append(n)
                in_all_names = True
                break
        if in_all_names:
            continue

        name = ""
        for line in nltk_output:
            
            startName = False
            onlyoneNNP = False
            if line[1] == 'NNP':
                # print(line[1],"yooooooooooooooooooo")
                startName = True
                name += line[0]
            if line[1] != 'NNP' and name != "":
                # print("this hits")
                names.append(name)
                all_names.append(name)
                break

                    
    return names



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
            if i != None:
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
    
    if re.search(r"\w+\s+\w",name):
        
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
    if len(values) == 0: return []
    mean_value = sum(values) / len(values)
    return [key for (key, value) in d.items() if value > mean_value]

def actorFilter(d):
    vals = [value for value in d if checker.checkActor(value) and not value in stops]
    return vals

def movieFilter(d):
    vals = [value for value in d if checker.checkMovie(value) and not value in stops]
    return vals


def print_hosts(hosts):
    print()
    print()
    print('Host(s): ' + ', '.join(str(x) for x in hosts))
    print()
    print()


def print_awards(awards):
    for award in awards:
        print_award(award)
    

def print_award(award):
    print("Award: " + award.awardName)
    print("Presenters: " + ', '.join(str(x) for x in award.presenters))
    print("Nominees: " + ', '.join(str(x) for x in award.nominees))
    print("Winner: " + award.winner)
    print()
    print()


def additional_goals(regex_dressed, regex_worst_dressed, regex_name, regex_funniest, regex_deserve):
    thing = dataSearchNotSplit(regex_dressed, regex_name)
    output = {}
    for i in thing:
        tweet = i[1]
        name = re.findall(regex_name, tweet)
        for n in name:
            if n in output:
                output[n] += 1
            else:
                output[n] = 1
    output2 = actorFilter(sorted(output, key = output.get, reverse = True)[:9])
    best_dressed = output2[:5]
    print('Best Dressed: ' + ', '.join(str(x) for x in best_dressed))

    thing = dataSearchNotSplit(regex_worst_dressed, regex_name)
    output3 = {}
    for i in thing:
        tweet = i[1]
        name = re.findall(regex_name, tweet)
        for n in name:
            if n in output3:
                output3[n] += 1
            else:
                output3[n] = 1
    output4 = actorFilter(sorted(output3, key = output3.get, reverse = True)[:9])
    worst_dressed = output4[:5]
    print('Worst Dressed: ' + ', '.join(str(x) for x in worst_dressed))

    output5 = {}
    sum1 = sum(output.values())
    sum3 = sum(output3.values())
    total = sum1 + sum3
    if total > 0:
        best_ratio = sum1/(sum1 + sum3)
        worst_ratio = sum3/(sum1 + sum3)
    else:
        best_ratio = 1
        worst_ratio = 1
    for name in output:
        if name in output5:
            output5[name] += output[name]*worst_ratio
        else:
            output5[name] = output[name]*worst_ratio
    for name in output3:
        if name in output5:
            output5[name] += output3[name]*best_ratio
        else:
            output5[name] = output3[name]*best_ratio
    output6 = actorFilter(sorted(output5, key = output5.get, reverse = True)[:9])
    most_controversially_dressed = output6[:5]
    print('Most Controversially Dressed: ' + ', '.join(str(x) for x in most_controversially_dressed))

    thing = dataSearchNotSplit(regex_funniest, regex_name)
    output = {}
    for i in thing:
        tweet = i[1]
        name = re.findall(regex_name, tweet)
        for n in name:
            if n in output:
                output[n] += 1
            else:
                if "Golden" in n:
                    continue
                output[n] = 1
    output2 = actorFilter(sorted(output, key = output.get, reverse = True)[:9])
    funniest = output2[:5]
    print('Funniest Jokes: ' + ', '.join(str(x) for x in funniest))

    thing = dataSearchNotSplit(regex_deserve, regex_name)
    output = {}
    for i in thing:
        tweet = i[1]
        name = re.findall(regex_name, tweet)
        for n in name:
            if n in output:
                output[n] += 1
            else:
                output[n] = 1
    output2 = actorFilter(sorted(output, key = output.get, reverse = True)[:9])
    most_snubbed = output2[:5]
    print('Snubs and Surprises: ' + ', '.join(str(x) for x in most_snubbed))
    print()
    print()

def nomineeGetter(allawards, winners):
    dat = allawards
    awardtype = {}
    awardUseful = {}
    output = {}
    awardNoms = {}
    stopword = ['best','-','in','a','role','golden','globes','globe','or','by','an','for','made','award']
    for i in dat:
        if 'actor' in i or 'actress' in i or 'director' in i or 'cecil' in i:
            awardtype[i] = 'Person'
        else:
            awardtype[i] = 'Film'
        
    for i in dat:
        ls = [w for w in i.split() if not w in stopword]
        #half = len(ls) // 2 + len(ls) % 2
        regex = ".*(?:{}).*".format("(.*)".join(ls))
        #regex = re.compile("&".join(ls))
        awardUseful[i] = regex

    for i in dat:
        #if awardtype[i].equals('Person'):
        regex_curr = awardUseful[i]
        #print(regex_curr)
        tw = dataSearch2(regex_curr, regex_curr)
        for j in tw:
            tweet = str(j)
            names = re.findall(c.regex_name, tweet)
            for n in names:
                if n in output:
                    output[n] += 1
                else:
                    if n == winners[i]: continue
                    output[n] = 1
        if awardtype[i] == 'Person':
            output2 = actorFilter(sorted(output, key = output.get, reverse = True)[:20])
        else:
            output2 = movieFilter(sorted(output, key = output.get, reverse = True)[:20])
        final = output2[:4]
        awardNoms[i] = final
        #print(final)
    return awardNoms
        
        
def presenterGetter(allawards, winners, nominees):
    dat = allawards
    awardUseful = {}
    output = {}
    awardPresenters = {}
    stopword = ['best','-','in','a','role','golden','globes','globe','or','by','an','for','made']
    alreadyPresented = []
        
    for i in dat:
        ls = [w for w in i.split() if not w in stopword]
        regex = ".*(?:{}).*".format("|".join(ls))
        awardUseful[i] = regex

    for i in dat:
        regex_curr = awardUseful[i]
        tw = dataSearch2(c.regex_presenter, regex_curr)
        for j in tw:
            tweet = str(j)
            names = re.findall(c.regex_name, tweet)
            for n in names:
                if n in output:
                    output[n] += 1
                else:
                    output[n] = 1
        output2 = sorted(output, key = output.get, reverse = True)[:50]
        final = []
        ind = 0
        for k in output2:
            if ind >= 2:
                break
            if k in alreadyPresented or k in winners[i] or k in nominees[i]:
                continue
            final.append(k)
            alreadyPresented.append(k)
            ind += 1
        awardPresenters[i] = final
        #print(final)
    return awardPresenters

