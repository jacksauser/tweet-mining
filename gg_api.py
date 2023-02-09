'''Version 0.35'''
from helper import *
from main import *
from winners import *
from awardshow import AwardShow, Award
from megasearch import *



OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']


def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    hosts = getHost()
    return hosts

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    awards = compileAwards()
    return awards

def get_nominees(year, tweetdict):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''

    if year == 2015:
        dat = OFFICIAL_AWARDS_1819
    else:
        dat = OFFICIAL_AWARDS_1315
    
    #nominees = nomineeGetter(dat, winners)
    nominees = get_noms_from_awards(dat, tweetdict)

    return nominees

def get_winner(year, tweetdict):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    if year == 2015:
        dat = OFFICIAL_AWARDS_1819
    else:
        dat = OFFICIAL_AWARDS_1315

    return get_winner_from_noms(dat, tweetdict)

def get_presenters(year, tweetdict):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    if year == 2015:
        dat = OFFICIAL_AWARDS_1819
    else:
        dat = OFFICIAL_AWARDS_1315
    presenters = get_presenters_from_awards(dat, tweetdict)
    return presenters

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    print("Pre-ceremony processing complete.")
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    tweetdict = categorize_tweets(OFFICIAL_AWARDS_1315)
    hosts = get_hosts(2013)
    awards = get_awards(2013)
    winners = get_winner(2013, tweetdict)
    nominees = get_nominees(2013, tweetdict)
    presenters = get_presenters(2013, tweetdict)

    gg = awardshow.AwardShow('Golden Globes', 2013)
    for i in hosts:
        gg.addHost(i)
    # ind = 0
    for i in OFFICIAL_AWARDS_1315:
        x = awardshow.Award()
        # if ind >= len(awards):
        #     x.awardName = i
        # else:
        #     rat = 0
        #     name = ''
        #     for j in awards:
        #         rat2 = fuzz.ratio(j,i)
        #         if rat2>rat:
        #             rat = rat2
        #             name = j
        x.awardName = i
        # ind+=1
        if i in nominees:
            x.nominees = nominees[i]
        else:
            x.nominees = []
        if i in presenters:
            x.presenters = presenters[i]
        else:
            x.presenters = []
        if i in winners:
            x.winner = winners[i]
        else:
            x.winner = ""
        gg.addAward(x)
    
    gg.print_readable()
    gg.make_json

    return

if __name__ == '__main__':
    main()
