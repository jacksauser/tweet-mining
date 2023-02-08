
from helper import *
import config as cfg

map_of_awards = {
    'Best Motion Picture(.*)Drama' : 'best motion picture - drama',
    'Best Actress(.*)Motion Picture(.*)Drama' : 'best performance by an actress in a motion picture - drama',
    'Best Actor(.*)Motion Picture(.*)Musical(.*)Comedy':'best performance by an actor in a motion picture - comedy or musical',
    'Best Animated Feature Film':'best animated feature film',
    'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Drama':'best performance by an actress in a television series - drama',
    'Best Performance(.*)Actress(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)':'best performance by an actress in a mini-series or motion picture made for television',
    'Best Performance(.*)Actor(.*)(TV|Television) Series(.*)Drama':'best performance by an actor in a television series - drama',
    'Best Actor(.*)Motion Picture(.*)Drama':'best performance by an actor in a motion picture - drama',
    'Best Director(.*)Motion Picture':'best director - motion picture',
    'Cecil B. DeMille Award' : 'cecil b. demille award',
    'Best Supporting Actor(.*)Motion Picture':'best performance by an actor in a supporting role in a motion picture',
    'Best Mini[\s-]*series(.*)(TV|Television) Film':'best mini-series or motion picture made for television',
    'Best Supporting Actor(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)':'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television',
    'Best Performance(.*)Actor(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)':'best performance by an actor in a mini-series or motion picture made for television',
    'Best Motion Picture(.*)Musical(.*)Comedy':'best motion picture - comedy or musical',
    'Best Actress(.*)Motion Picture(.*)Musical(.*)Comedy':'best performance by an actress in a motion picture - comedy or musical',
    'Best Screenplay(.*)Motion Picture':'best screenplay - motion picture',
    'Best Original Score':'best original score - motion picture',
    'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Musical(.*)Comedy':'best performance by an actress in a television series - comedy or musical',
    'Best Supporting Actress(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)':'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television',
    'Best (TV|Television) Series(.*)Drama':'best television series - drama',
    'Best Supporting Actress(.*)Motion Picture':'best performance by an actress in a supporting role in a motion picture',
    'Best Original Song':'best original song - motion picture',
    'Best Foreign Language Film':'best foreign language film',
    'Best (TV|Television) Series(.*)Musical(.*)Comedy':'best television series - comedy or musical',
    'Best Actor(.*)(TV|Television) Series(.*)Musical(.*)Comedy':'best performance by an actor in a television series - comedy or musical'
}
awardnamestoregex_jack = {v: k for k, v in map_of_awards.items()}
stopwords = ['-', 'in', 'a', 'performance', 'by', 'an', 'or','made','role']
personwords = ['actor', 'director', 'actress', 'cecil']
awardtype = {}
awardnamesreal = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
awardnamestoregex = {}
awardnames_to_tweets = {}
award_to_winner = {}

data = json.load(open('gg2013.json'))
regex_remove = r'^RT\s|\sRT|(?i)goldenglobes|(?i)golden\sglobes'
regex_remove_rt = '^RT @\w+: '
regex_remove_link = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
regex_remove_gg = '#GoldenGlobes'

for i in awardnamesreal:
    result = []
    prev = ""
    words = i.split()
    for word in words:
        if word.lower() in stopwords:
            if prev != "(.*)":
                result.append("(.*)")
                prev = "(.*)"
        elif word.lower() == 'television': 
            result.append("(TV|Television)")       
        else:
            result.append(word)
            prev = word
    final = " ".join(result)
    #final = re.sub(" (.*) ","(.*)",final)
    awardnamestoregex[i] = final
    #print(awardnamestoregex[i])

    for w in personwords:
        if w in i:
            awardtype[i] = 'Person'
        else:
            awardtype[i] = 'Film'
for i in awardnamesreal:
    awardnames_to_tweets[i] = []

for d in data:
    for i in awardnamesreal:
        regex_curr = awardnamestoregex_jack[i]
        if re.search(regex_curr,d['text']):
            t = d['text']
            t = re.sub(regex_remove_rt, '', t)
            t = re.sub(regex_remove_link, '', t)
            t = re.sub(regex_remove_gg, '', t)
            awardnames_to_tweets[i].append(t)

for i in awardnamesreal:
    tweets = awardnames_to_tweets[i]
    nominees = cfg.nominees_dict[i]
    nomineeCount = {}
    for tw in tweets:
        #print(tw)
        for n in nominees:
            #print(n)
            names = re.findall(n,str(tw))
            if n in names:
                if n in nomineeCount:
                    nomineeCount[n] += 1
                else:
                    nomineeCount[n] = 1
    final = sorted(nomineeCount, key = nomineeCount.get, reverse = True)[:1]
    award_to_winner[i] = final
    #print(i)
    #print(final)

for i in awardnamesreal:
    print(cfg.nominees_dict[i])
