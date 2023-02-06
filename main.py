from helper import *
import awardshow
import constants as c

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





# awards = getAwards(getDistribution(dataSearch(c.regex_award)))


# potential_winner_list, award_numbers = dataSearchAward(c.regex_winner, awards.keys())
# potential_winners = getNames(getDistribution(potential_winner_list), awards.keys())
# real_awards = award_numbers.keys()


# Gets the outliers of the hosts
host = getNames(getDistribution(dataSearch(c.regex_host)))
host_outliers = get_outliers(host)
print(host_outliers)

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


# award_category = ['Best Motion Picture(.*)Drama',
# 'Best Actress(.*)Motion Picture(.*)Drama',
# 'Best Actor(.*)Motion Picture(.*)Musical(.*)Comedy',
# 'Best Animated Feature Film',
# 'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Drama',
# 'Best Performance(.*)Actress(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
# 'Best Performance(.*)Actor(.*)(TV|Television) Series(.*)Drama',
# 'Best Actor(.*)Motion Picture(.*)Drama',
# 'Best Director(.*)Motion Picture',
# 'Cecil B. DeMille Award',
# 'Best Supporting Actor(.*)Motion Picture',
# 'Best Mini[\s-]*series(.*)(TV|Television) Film',
# 'Best Supporting Actor(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
# 'Best Performance(.*)Actor(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
# 'Best Motion Picture(.*)Musical(.*)Comedy',
# 'Best Actress(.*)Motion Picture(.*)Musical(.*)Comedy',
# 'Best Screenplay(.*)Motion Picture',
# 'Best Original Score',
# 'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Musical(.*)Comedy',
# 'Best Supporting Actress(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
# 'Best (TV|Television) Series(.*)Drama',
# 'Best Supporting Actress(.*)Motion Picture',
# 'Best Original Song',
# 'Best Foreign Language Film',
# 'Best (TV|Television) Series(.*)Musical(.*)Comedy',
# 'Best Actor(.*)(TV|Television) Series(.*)Musical(.*)Comedy']

# award_category = [r'\bbest\b(?=.*\bmotion\b)(?=.*\bpicture\b)(?=.*\bdrama\b)',
# r'\bactress\b(?=.*\bmotion\spicture\b)(?=.*\bdrama\b)',
# r'\bactor\b(?=.*\bmotion\spicture\b)(?=.*\bmusical\b)(?=.*\bcomedy\b)'
# ]
# 'Best Actor(.*)Motion Picture(.*)Musical(.*)Comedy',
# 'Best Animated Feature Film',
# 'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Drama',
# 'Best Performance(.*)Actress(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
# 'Best Performance(.*)Actor(.*)(TV|Television) Series(.*)Drama',
# 'Best Actor(.*)Motion Picture(.*)Drama',
# 'Best Director(.*)Motion Picture',
# 'Cecil B. DeMille Award',
# 'Best Supporting Actor(.*)Motion Picture',
# 'Best Mini[\s-]*series(.*)(TV|Television) Film',
# 'Best Supporting Actor(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
# 'Best Performance(.*)Actor(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
# 'Best Motion Picture(.*)Musical(.*)Comedy',
# 'Best Actress(.*)Motion Picture(.*)Musical(.*)Comedy',
# 'Best Screenplay(.*)Motion Picture',
# 'Best Original Score',
# 'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Musical(.*)Comedy',
# 'Best Supporting Actress(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
# 'Best (TV|Television) Series(.*)Drama',
# 'Best Supporting Actress(.*)Motion Picture',
# 'Best Original Song',
# 'Best Foreign Language Film',
# 'Best (TV|Television) Series(.*)Musical(.*)Comedy',
# 'Best Actor(.*)(TV|Television) Series(.*)Musical(.*)Comedy']

#pattern = re.compile(r"\bactress\b(?=.*\bmotion\spicture\b)(?=.*\bdrama\b)")
# dat = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
# awardtype = {}
# awardUseful = {}
# output = {}
# for i in dat:
#     if 'actor' in i or 'actress' in i or 'director' in i or 'cecil' in i:
#         awardtype[i] = 'Person'
#     else:
#         awardtype[i] = 'Film'
    
# for i in dat:
#     awardUseful[i] = [w for w in i.split()]

# for i in dat:
#     #if awardtype[i].equals('Person'):
#     regex_curr = re.compile(i)
#     tw = dataSearch2(regex_curr, regex_curr)
#     for j in tw:
#         tweet = str(j)
#         names = re.findall(regex_name, tweet)
#         for n in names:
#             if n in output:
#                 output[n] += 1
#             else:
#                 output[n] = 1
#     output2 = sorted(output, key = output.get, reverse = True)[:20]
#     print(output2)
        


            
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
