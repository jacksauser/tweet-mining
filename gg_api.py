'''Version 0.35'''
from helper import *
from main import *
from winners import *
from awardshow import AwardShow, Award



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
    awards = []
    return findAwards()

def get_nominees(year, winners):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''

    if year == 2015:
        dat = OFFICIAL_AWARDS_1819
    else:
        dat = OFFICIAL_AWARDS_1315
    
    nominees = nomineeGetter(dat, winners)
    
    return nominees

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    if year == 2015:
        dat = OFFICIAL_AWARDS_1819
    else:
        dat = OFFICIAL_AWARDS_1315

    return getWinners(dat)

def get_presenters(year, winners, nominees):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    if year == 2015:
        dat = OFFICIAL_AWARDS_1819
    else:
        dat = OFFICIAL_AWARDS_1315
    presenters = presenterGetter(dat, winners, nominees)
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
    hosts = get_hosts(2013)
    awards = get_awards(2013)
    winners = get_winner(2013)
    nominees = get_nominees(2013, winners)
    presenters = get_presenters(2013, winners, nominees)

    gg = awardshow.AwardShow('Golden Globes', 2013)
    for i in hosts:
        gg.addHost(i)
    ind = 0
    for i in OFFICIAL_AWARDS_1315:
        x = awardshow.Award()
        if ind >= len(awards):
            x.awardName = i
        else:
            rat = 0
            name = ''
            for j in awards:
                rat2 = fuzz.ratio(j,i)
                if rat2>rat:
                    rat = rat2
                    name = j
            x.awardName = name
        ind+=1
        x.nominees = nominees[i]
        x.presenters = presenters[i]
        x.winner = winners[i]
        gg.addAward(x)
    
    gg.print_readable()


    return

if __name__ == '__main__':
    main()
