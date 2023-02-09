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
    'Best Mini(.*)series(.*)(TV|Television) Film':'best mini-series or motion picture made for television',
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

awardnamestoregex_jack = {
    'best motion picture - drama':'Best Motion Picture(.*)Drama' ,
    'best performance by an actress in a motion picture - drama':'Best Actress(.*)Motion Picture(.*)Drama',
    'best performance by an actor in a motion picture - comedy or musical':'Best Actor(.*)Motion Picture(.*)Musical(.*)Comedy',
    'best animated feature film':'Best Animated Feature Film',
    'best performance by an actress in a television series - drama':'Best (Performance)?(.*)Actress(.*)(TV|Television) Series(.*)Drama',
    'best performance by an actress in a mini-series or motion picture made for television':'Best(.*)(Performance)?(.*)Actress(.*)(Mini[\s-]*series)?(.*)(Motion Picture|Movie)(.*)(for|made for)?(.*)(TV|Television)',
    'best performance by an actor in a television series - drama':'Best (Performance)?(.*)Actor(.*)(TV|Television) Series(.*)Drama',
    'best performance by an actor in a motion picture - drama':'Best Actor(.*)Motion Picture(.*)Drama',
    'best director - motion picture':'Best Director(.*)Motion Picture',
    'cecil b. demille award':'Cecil B. DeMille Award',
    'best performance by an actor in a supporting role in a motion picture':'Best Supporting Actor(.*)Motion Picture',
    'best mini-series or motion picture made for television':'Best Mini(.*)series(.*)(TV|Television) Film',
    'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television':'Best Supporting Actor(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
    'best performance by an actor in a mini-series or motion picture made for television':'Best (Performance)?(.*)Actor(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
    'best motion picture - comedy or musical':'Best Motion Picture(.*)Musical(.*)Comedy',
    'best performance by an actress in a motion picture - comedy or musical':'Best Actress(.*)Motion Picture(.*)Musical(.*)Comedy',
    'best screenplay - motion picture':'Best Screenplay(.*)Motion Picture',
    'best original score - motion picture':'Best Original Score',
    'best performance by an actress in a television series - comedy or musical':'Best (Performance)?(.*)Actress(.*)(TV|Television) Series(.*)Musical(.*)Comedy',
    'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television':'Best Supporting Actress(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
    'best television series - drama':'Best (TV|Television) Series(.*)Drama',
    'best performance by an actress in a supporting role in a motion picture':'Best Supporting Actress(.*)Motion Picture',
    'best original song - motion picture':'Best Original Song',
    'best foreign language film':'Best Foreign Language Film',
    'best television series - comedy or musical':'Best (TV|Television) Series(.*)Musical(.*)Comedy',
    'best performance by an actor in a television series - comedy or musical':'Best Actor(.*)(TV|Television) Series(.*)Musical(.*)Comedy'
}
#awardnamestoregex_jack = {v: k for k, v in map_of_awards.items()}

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
    tweets = {}
    award_tweet_dict = dataSearch3(regexlist)
    for i in regexlist:
        official = map_of_awards[i]
        if i in award_tweet_dict:
            tweets[official] = award_tweet_dict[i]
        else:
            tweets[official] = []
    return tweets

def get_winner_from_noms(awardnames, tweet_dict):
    award_to_winner = {}
    award_tweet_dict = tweet_dict
    awardnamesreal = awardnames
    for i in awardnamesreal:
        #awardregex = awardnamestoregex_jack[i]
        if i not in award_tweet_dict:
            continue
        tweetlist = award_tweet_dict[i]
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
        award_to_winner[i] = str(final)

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
        if i not in award_tweet_dict:
            continue
        tweetlist = award_tweet_dict[i]
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

def get_presenters_from_awards(awardnames, tweet_dict):
    award_to_presenter = {}
    award_tweet_dict = tweet_dict
    awardnamesreal = awardnames
    for i in awardnamesreal:
        out = {}
        #awardregex = awardnamestoregex_jack[i]
        if i not in award_tweet_dict:
            continue
        tweetlist = award_tweet_dict[i]
        for tw in tweetlist:
            if re.search(c.regex_present,str(tw).lower()):
                names = re.findall(regex_name,str(tw))
                for n in names:
                    if n in out:
                        out[n]+=1
                    else:
                        out[n] = 1
        final = actorFilter(sorted(out, key = out.get, reverse = True)[:5])
        award_to_presenter[i] = final[:2]
    return award_to_presenter

# awardnamesreal = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
# tweetdict = categorize_tweets(awardnamesreal)
# d = get_presenters_from_awards(awardnamesreal,tweetdict)
# for i in awardnamesreal:
#     print(i)
#     print(d[i])
