from helper import *
import config as cfg
from winners import *

map_of_awards = {
    'Best Motion Picture(.*)Drama' : 'best motion picture - drama',
    'Best Actress(.*)Motion Picture(.*)Drama' : 'best performance by an actress in a motion picture - drama',
    'Best Actor(.*)Motion Picture(.*)Musical(.*)Comedy':'best performance by an actor in a motion picture - comedy or musical',
    'Best Animated Feature Film':'best animated feature film',
    'Best (Performance)?(.*)Actress(.*)(TV|Television) Series(.*)Drama':'best performance by an actress in a television series - drama',
    'Best(.*)(Performance)?(.*)Actress(.*)(Mini[\s-]*series)?(.*)(Motion Picture|Movie)(.*)(for|made for)?(.*)(TV|Television)':'best performance by an actress in a mini-series or motion picture made for television',
    'Best (Performance)?(.*)Actor(.*)(TV|Television) Series(.*)Drama':'best performance by an actor in a television series - drama',
    'Best Actor(.*)Motion Picture(.*)Drama':'best performance by an actor in a motion picture - drama',
    'Best Director(.*)Motion Picture':'best director - motion picture',
    'Cecil B. DeMille Award' : 'cecil b. demille award',
    'Best Supporting Actor(.*)Motion Picture':'best performance by an actor in a supporting role in a motion picture',
    'Best Mini[\s-]*series(.*)(TV|Television) Film':'best mini-series or motion picture made for television',
    'Best Supporting Actor(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)':'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television',
    'Best (Performance)?(.*)Actor(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)':'best performance by an actor in a mini-series or motion picture made for television',
    'Best Motion Picture(.*)Musical(.*)Comedy':'best motion picture - comedy or musical',
    'Best Actress(.*)Motion Picture(.*)Musical(.*)Comedy':'best performance by an actress in a motion picture - comedy or musical',
    'Best Screenplay(.*)Motion Picture':'best screenplay - motion picture',
    'Best Original Score':'best original score - motion picture',
    'Best (Performance)?(.*)Actress(.*)(TV|Television) Series(.*)Musical(.*)Comedy':'best performance by an actress in a television series - comedy or musical',
    'Best Supporting Actress(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)':'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television',
    'Best (TV|Television) Series(.*)Drama':'best television series - drama',
    'Best Supporting Actress(.*)Motion Picture':'best performance by an actress in a supporting role in a motion picture',
    'Best Original Song':'best original song - motion picture',
    'Best Foreign Language Film':'best foreign language film',
    'Best (TV|Television) Series(.*)Musical(.*)Comedy':'best television series - comedy or musical',
    'Best Actor(.*)(TV|Television) Series(.*)Musical(.*)Comedy':'best performance by an actor in a television series - comedy or musical'
}
awardnamestoregex_jack = {v: k for k, v in map_of_awards.items()}
print(awardnamestoregex_jack)

data = json.load(open('gg2013.json'))
regex_remove = r'^RT\s|\sRT|(?i)goldenglobes|(?i)golden\sglobes'
regex_remove_rt = '^RT @\w+: '
regex_remove_link = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
regex_remove_gg = '#GoldenGlobes'

def categorize_tweets(awards):
    regexlist = []
    awardnamesreal = awards
    for i in awardnamesreal:
        regexlist.append(awardnamestoregex_jack[i])

    award_tweet_dict = dataSearch3(regexlist)
    return award_tweet_dict

def get_winner_from_noms(awardnames, tweet_dict):
    award_to_winner = {}
    award_tweet_dict = tweet_dict
    awardnamesreal = awardnames
    for i in awardnamesreal:
        awardregex = awardnamestoregex_jack[i]
        if awardregex not in award_tweet_dict:
            continue
        tweetlist = award_tweet_dict[awardregex]
        nominees = cfg.nominees_dict[i]
        nomineeCount = {}
        for tw in tweetlist:
            for n in nominees:
                names = re.findall(n,str(tw).lower())
                if n in names:
                    if n in nomineeCount:
                        nomineeCount[n] += 1
                    else:
                        nomineeCount[n] = 1
        final = sorted(nomineeCount, key = nomineeCount.get, reverse = True)[:1]
        award_to_winner[i] = final

    return award_to_winner

def get_noms_from_awards(awardnames, tweet_dict):
    award_to_noms = {}
    award_tweet_dict = tweet_dict
    awardnamesreal = awardnames
    for i in awardnamesreal:
        if 'actor' in i or 'actress' in i or 'director' in i or 'cecil' in i:
            awardtype = 'Person'
        else:
            awardtype = 'Film'
        awardregex = awardnamestoregex_jack[i]
        if awardregex not in award_tweet_dict:
            continue
        tweetlist = award_tweet_dict[awardregex]
        names = []
        for tw in tweetlist:
            text = re.sub(awardregex,'',tw)
            if awardtype == 'Person':
                r = searchForActor(text)
                if r != -1:
                    names.append(r)
            else:
                r = searchForMovie(i, text)
                if r != -1:
                    names.append(r)
        if len(names) > 0:
            ls = []
            if len(set(names))<5:
                award_to_noms[i] = list(set(names))
            else:
                for j in range(5):
                    curr = next(iter(getDistribution(names)))
                    ls.append(curr)
                    names.remove(curr)
                award_to_noms[i] = ls
        else:
            award_to_noms[i] = "No winner found"

    return award_to_noms

awardnamesreal = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
tweetdict = categorize_tweets(awardnamesreal)
#d = get_noms_from_awards(awardnamesreal,tweetdict)
for i in awardnamesreal:
    print(i)

    print(len(tweetdict[awardnamestoregex_jack[i]]))


        #     for n in nominees:
        #         names = re.findall(n,str(tw).lower())
        #         if n in names:
        #             if n in nomineeCount:
        #                 nomineeCount[n] += 1
        #             else:
        #                 nomineeCount[n] = 1
        # final = sorted(nomineeCount, key = nomineeCount.get, reverse = True)[:1]
        # award_to_noms[i] = final

#         # print(names)

#     return result
    
    
# #     output = {}
# #     for award in list_of_awards:
# #         output[award] = dataSearch2(award, ".*")#r"goes\sto|winner|recipent")




#     result = {}
#     for key in output:
#         # print(key)
#         names = []
#         for line in output[key]:
#             text = re.sub(key,'',line[1])
#             if re.search(r"(?i)Actor", key) or re.search(r"(?i)Actress", key) or re.search(r"(?i)Director", key) or re.search(r"(?i)DeMille", key):
#                 r = searchForActor(text)
#                 if r != -1:
#                     names.append(r)
#             else:
#                 r = searchForMovie(key, text)
#                 if r != -1:
#                     names.append(r)
#         # print(names)
#         if len(names) > 0:
#             result[map_of_awards[key]] = next(iter(getDistribution(names)))
#         else:
#             result[map_of_awards[key]] = "No winner found"
#     return result
# # for i in awardnamesreal:
# #     print(cfg.nominees_dict[i])
# for i in awardnamesreal:
#     result = []
#     prev = ""
#     words = i.split()
#     for word in words:
#         if word.lower() in stopwords:
#             if prev != "(.*)":
#                 result.append("(.*)")
#                 prev = "(.*)"
#         elif word.lower() == 'television': 
#             result.append("(TV|Television)")       
#         else:
#             result.append(word)
#             prev = word
#     final = " ".join(result)
#     #final = re.sub(" (.*) ","(.*)",final)
#     awardnamestoregex[i] = final
#     #print(awardnamestoregex[i])

#     for w in personwords:
#         if w in i:
#             awardtype[i] = 'Person'
#         else:
#             awardtype[i] = 'Film'
# for i in awardnamesreal:
#     awardnames_to_tweets[i] = []

# for d in data:
#     for i in awardnamesreal:
#         regex_curr = awardnamestoregex_jack[i]
#         if re.search(regex_curr,d['text']):
#             t = d['text']
#             t = re.sub(regex_remove_rt, '', t)
#             t = re.sub(regex_remove_link, '', t)
#             t = re.sub(regex_remove_gg, '', t)
#             awardnames_to_tweets[i].append(t)


# stopwords = ['-', 'in', 'a', 'performance', 'by', 'an', 'or','made','role']
# personwords = ['actor', 'director', 'actress', 'cecil']
# awardtype = {}

# awardnamestoregex = {}
# awardnames_to_tweets = {}
# 
