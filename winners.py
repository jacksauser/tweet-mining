from helper import *
import re
import Checker
import config

list_of_awards = ['Best Motion Picture(.*)Drama',
                  'Best Actress(.*)Motion Picture(.*)Drama',
                  'Best Actor(.*)Motion Picture(.*)Musical(.*)Comedy',
                  'Best Animated Feature Film',
                  'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Drama',
                  'Best Performance(.*)Actress(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
                  'Best Performance(.*)Actor(.*)(TV|Television) Series(.*)Drama',
                  'Best Actor(.*)Motion Picture(.*)Drama',
                  'Best Director(.*)Motion Picture',
                  'Cecil B. DeMille Award',
                  'Best Supporting Actor(.*)Motion Picture',
                  'Best Mini[\s-]*series(.*)(TV|Television) Film',
                  'Best Supporting Actor(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
                  'Best Performance(.*)Actor(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
                  'Best Motion Picture(.*)Musical(.*)Comedy',
                  'Best Actress(.*)Motion Picture(.*)Musical(.*)Comedy',
                  'Best Screenplay(.*)Motion Picture',
                  'Best Original Score',
                  'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Musical(.*)Comedy',
                  'Best Supporting Actress(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
                  'Best (TV|Television) Series(.*)Drama',
                  'Best Supporting Actress(.*)Motion Picture',
                  'Best Original Song',
                  'Best Foreign Language Film',
                  'Best (TV|Television) Series(.*)Musical(.*)Comedy',
                  'Best Actor(.*)(TV|Television) Series(.*)Musical(.*)Comedy']

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
regex_name = r'[A-Z][a-z]+\s[A-Z][a-z]+'
checker = Checker.checker('Golden Globes', 2013)

known_actors = []
known_movies = {}
def searchForActor(s):
    for a in known_actors:
        if a in s:
            return a
    maybe_names = []
    nltk_output = ne_chunk(pos_tag(word_tokenize(s)))
    for line in nltk_output:
        if type(line) == Tree:
            name = ''
            for nltk_result_leaf in line.leaves():
                name += nltk_result_leaf[0] + ' '
            maybe_names.append(re.sub(r'\s+$','',name))
    
    for n in maybe_names:
        actor = checker.isActor(n)
        if actor and actor != -1 and n != None and re.search(regex_name, n):
            known_actors.append(n)
            return n
        else:
            return -1
    
    return (searchForActorAgain(s))
    
def searchForActorAgain(s):
    list_of_words = s.split(' ')
    for i in range(len(list_of_words)-1):
        name = list_of_words[i] + ' '+list_of_words[i+1]
        actor = checker.isActor(name)
        if actor and actor != -1 and actor == name:
            return name
    

def searchForMovie(key, s):
    if key not in known_movies:
        known_movies[key] = []

    for a in known_movies[key]:
        if a in s:
            return a
    maybe_titles = []
    nltk_output = word_tokenize(s)
    
    nnps = []
    for line in nltk_output:
        if re.search(r'[A-Z][a-z]+',line):
            nnps.append(line)
    
    potential = []
    for i in range(len(nnps)):
        n = nnps[i]
        movie = checker.isMovie(n)
        if movie and movie != -1 and n != None:
            if n == movie.get('title'):
                known_movies[key].append(n)
                return n
            else:
                m = movie.get('title')
                if m not in potential:
                    potential.append(m)
        
        for m in potential:
            if m in s:
                known_movies[key].append(n)
                return n

    nltk = ne_chunk(pos_tag(nltk_output))
    for line in nltk:
        if type(line) == Tree:
            name = ''
            for nltk_result_leaf in line.leaves():
                name += nltk_result_leaf[0] + ' '
            maybe_titles.append(re.sub(r'\s+$','',name))
    
    for n in maybe_titles:
        movie = checker.isMovie(n)
        if movie and movie != -1 and n != None:
            known_movies[key].append(movie.get('title'))
            return movie.get('title')


    nnps = []
    for line in nltk_output:
        if re.search(r'[A-Z][a-z]+\s[A-Z][a-z]+',line):
            nnps.append(line)
    for i in range(len(nnps)):
        n = nnps[i]
        movie = checker.isMovie(n)
        # print()
        # print(movie)
        # print(n)
        # print(n == movie.get('title'))
        # print()
        if movie and movie != -1 and n != None:
            if n == movie:
                known_movies[key].append(n)
                return n
    return -1

def getWinners(l):
    output = {}
    for award in list_of_awards:
        output[award] = dataSearch2(award, ".*")#r"goes\sto|winner|recipent")

    result = {}
    for key in output:
        # print(key)
        names = []
        for line in output[key]:
            text = re.sub(key,'',line[1])
            if re.search(r"(?i)Actor", key) or re.search(r"(?i)Actress", key) or re.search(r"(?i)Director", key) or re.search(r"(?i)DeMille", key):
                r = searchForActor(text)
                if r != -1:
                    names.append(r)
            else:
                r = searchForMovie(key, text)
                if r != -1:
                    names.append(r)
        # print(names)
        if len(names) > 0:
            result[map_of_awards[key]] = next(iter(getDistribution(names)))
        else:
            result[map_of_awards[key]] = "No winner found"
    return result
# print(result)