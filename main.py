from helper import *
import awardshow
import constants as c

import numpy as np

def cosine_similarity(list1, list2):
    list1 = np.array(list1)
    list2 = np.array(list2)
    dot_product = np.dot(list1, list2)
    norm_list1 = np.linalg.norm(list1)
    norm_list2 = np.linalg.norm(list2)
    return dot_product / (norm_list1 * norm_list2)




# collecting the award show queried and year
# award_show = input("What award show? ")
# year = input("What year of the "+award_show+"? ")


# autofill inputs is not specified 
# if not award_show:
#     award_show = "Golden Globes"
# if not year:
#     year = 2013
# else:
#     year = int(year)

# additional_goals(c.regex_dressed, c.regex_worst_dressed, c.regex_name, c.regex_funniest, c.regex_deserve)




#host = getNames(getDistribution(dataSearch(c.regex_host)))

# awards = getAwards(getDistribution(dataSearch(c.regex_award)))


# potential_winner_list, award_numbers = dataSearchAward(c.regex_winner, awards.keys())
# potential_winners = getNames(getDistribution(potential_winner_list), awards.keys())
# real_awards = award_numbers.keys()


# Gets the outliers of the hosts
# host = getNames(getDistribution(dataSearch(c.regex_host)))
# host_outliers = get_outliers(host)
# print(host_outliers)

def getHost():
    host = getNames(getDistribution(dataSearch(c.regex_host)))
    host_outliers = get_outliers(host)  
    return host_outliers

#print_human_readable(c.regex_host, c.regex_dressed, c.regex_worst_dressed, c.regex_name)


# print(real_awards)
# print()
# print()
# print(potential_winners)


#print_helper(dataSearch2(regex_best,regex_goes_to))






# output_top10 = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True)[:10])

# print(output_top10)


# output_top = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True))

# for i in host_names_potential:
#     for j in output_top:
#         if i in j:
#             output_top[j] += 1

# print(sorted(output_top.items(), key=lambda item: item[1], reverse=True))



        


            
# regex_list = [re.compile(s) for s in award_category]
# nominees = []
# for r in regex_list:
#     thing = dataSearch2(r, r)
#     output = {}
#     for i in thing:
#         tweet = str(i[1])
# #        if re.findall(regex_person, tweet):
#         names = re.findall(regex_name, tweet)
#         for n in names:
#             if n in output:
#                 output[n]+=1
#             else:
#                 output[n] = 1
#         output2 = actorFilter(sorted(output, key = output.get, reverse = True)[:20])
#     print(output2[:5])

#     thing = dataSearch2(r, regex_nominee)
#     output = {}
#     for i in thing:
#         tweet = i[1]
#         if re.findall(regex_person, str(tweet)):
#             name = re.findall(regex_name, str(tweet))
#             for n in name:
#                 if n in output:
#                     output[n] += 1
#                 else:
#                     output[n] = 1
#             output2 = actorFilter(sorted(output, key = output.get, reverse = True)[:20])
#         elif re.findall(regex_film, str(tweet)):
#             name = nameGrabber(tweet)
#             for n in name:
#                 if n in output:
#                     output[n] += 1
#                 else:
#                     output[n] = 1
#             #output2 = movieFilter(sorted(output, key = output.get, reverse = True)[:20])
#             output2 = sorted(output, key = output.get, reverse = True)[:20]
#     #output2 = sorted(output, key = output.get, reverse = True)[:20]
#     print(output2[:5])

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        return(list(a_set & b_set))
    else:
        return([])

def findAwards():   
    l = dataSearch2(c.regex_best,c.regex_goes_to)
    # print_helper(l)


    l2 = []
    for i in l:
        l2.append(re.split(c.regex_goes_to,i[1]))

    # print(l2)
    d1 = {}
    l3 = []
    l4 = []
    for i in l2:
        a = i[0]
        # print(a)
        if a.startswith("best") or a.startswith("Best"):
            # print(a)
            if a in d1:
                l3.append(a)
                d1[a].append(i[1])
                l4.append(i[1])
            else:
                l3.append(a)
                d1[a] = [i[1]]
                l4.append(i[1])

    awards = d1.keys()
    ret = []
    for a in awards:
        split1 = a.split(' ')
        removedWord = False
        for r in ret:
            split2 = r.split(' ')
            common = common_member(split1,split2)
            if len(common) == len(split1):
                removedWord = True
        if not removedWord:
            ret.append(a)
    return(ret)

# TV/television
# Motion Picture/Movie/Film
# 

# Actor
# Actress

# Supporting

from collections import defaultdict
import re

def get_word_distribution(text_list):
    # Step 1: Convert the list of strings into a single string
    text = " ".join(text_list)
    
    # Step 2: Tokenize the string into words
    words = re.findall(r'\b\w+\b', text)
    
    # Step 3: Count the frequency of each word
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word.lower()] += 1
        
    # Step 4: Store the frequency count in a dictionary
    return dict(word_counts)

def bag_of_words_pre(d):
    stopwords = ['best', 'in', 'a', 'by', 'an', 'or','made','role', 'in', 'a', 'by', 'an', 'role', 'or', 'for', 'etc', 'award', 'turtle', 'best', 'on', 'my', 'list','and', 'the', 'golden', 'globe', 'to', 'goldenglobes', 'role', 'tonight', 'use', 'of', 'large', 'doily', 'swallowed', 'rooster', 'so', 'far', 'night', 'at', 'outfit', 'made', 'real', 'life', 'accessory', 'comedic', 'combo', 'ever', 'show', 'handjob', 'in', 'a', 'hug', 'pageboy', 'i', 'm', 'bi', 'polar', 'cia', 'agent', 'who', 'just', 'had', 'baby', 'real', 'life', 'month', 'ago', 'amp', 'am', 'rocking', 'this', 'red', 'non', 'sequiturs', 'is', 'yet', 'analysis','golden','globe','for']
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    output1 = {}
    output2 = []
    for word in d:
        if word not in stopwords:
            if word.lower() in output1:
                output1[word.lower()] += d[word]
            else:
                output1[word.lower()] = d[word]
            output2.append(word.lower())
    # print(output2)
    return output1

def word_weighter(w):
    if w.lower() in ['supporting']:
        return 3
    elif w.lower() in ['actor','actress','director', 'movie','motion','supporting', 'mini','miniseries','musical']:
        return 2
    return 1


def bag_of_words(vectorized, awards):
    vector_pos = {}
    index = 0
    for word in vectorized:
        vector_pos[word.lower()] = index

        index += 1 * vectorized[word.lower()]
    
    ret = {}

    for a in awards:
        l = [0] * index
        award_words = word_tokenize(a)
        for word in award_words:
            if word.lower() in vector_pos:
                l[vector_pos[word.lower()]] += 1
        ret[a] = l
    
    first = next(iter(ret))
    first_v = ret[first]

    ret2 = {}
    for a in ret:
        ret2[a] = cosine_similarity(first_v,ret[a])
    return dict(sorted(ret2.items(), key=lambda item: item[1], reverse=True))
    
flag_key = {
    'movie' : 0,
    'actor' : 1,
    'actress' : 2,
    'supporting' : 3,
    'drama' : 4,
    'comedy' : 5,
    'tv series' : 6,
    'musical' : 7,
    'animated' : 8,
    'performance' : 9,
    'foreign' : 10,
    'director' : 11,
    'screenplay' : 12,
    'score' : 13,
    'song' : 14,
    'tv' : 15,
    'mini-series' : 16,
    'other' : 17
}
def create_flags(s):
    ret = [0] * 18
    if ('motion picture' in s.lower() or 'movie' in s.lower()) and 'tv movie' not in s.lower():
        ret[0] = 1
    if 'actor' in s.lower():
        ret[1] = 1
    if 'actress'in s.lower():
        ret[2] = 1
    if 'supporting' in s.lower():
        ret[3] = 1
    if 'tv' in s.lower() or 'television' in s.lower():
        ret[4] = 1
    if 'drama' in s.lower():
        ret[5] = 1
    if 'comedy' in s.lower():
        ret[6] = 1
    if 'tv series' in s.lower() or 'television series' in s.lower():
        ret[7] = 1
    if 'musical' in s.lower():
        ret[8] = 1
    if 'animat' in s.lower():
        ret[9] = 1
    if 'performance' in s.lower():
        ret[10] = 1
    if 'foreign' in s.lower():
        ret[11] = 1
    if 'director' in s.lower():
        ret[12] = 1
    if 'screenplay' in s.lower():
        ret[13] = 1
    if 'score' in s.lower():
        ret[14] = 1
    if 'song' in s.lower():
        ret[15] = 1
    if 'mini-series' in s.lower() or 'mini series' in s.lower() or 'miniseries' in s.lower():
        ret[16] = 1
    if sum(ret) == 0:
        ret[17] = 1
    return ret

def compileAwards():
    pot_awards = findAwards()
    # print(bag_of_words(bag_of_words_pre(get_word_distribution(pot_awards)),pot_awards))
    test = {}
    for i in pot_awards:
        s = 0
        flags = create_flags(i)
        for e in flags:
            s = s*10 + e
        
        if s in test:
            test[s].append([i,flags])
        else:
            test[s] = [[i,flags]]

    ret = []
    for key in test:
        # print('-------------------------------------------------------')
        ret1 = test[key][0][0] if test[key][0][1].count(1) > 1 else -1
        if ret1 != -1:
            ret.append(ret1)
        # print(ret1) if test[key][0][1].count(1) > 1 else ''
        # print('-------------------------------------------------------')
        
    return ret