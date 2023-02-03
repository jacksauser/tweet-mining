import imdb
from fuzzywuzzy import fuzz

# create an instance of the IMDb class


# get the string input
#actor = input("Enter an actor name: ")
#movie = input("Enter movie name: ")

class checker:
    
    actorDict = {}
    movieDict = {}

    ia = imdb.IMDb()

    def __init__(self, name, year):
        self.showName = name
        self.year = year

    def isActor(self, name):
        try:
            # search for the actor
            search_results = self.ia.search_person(name)

            # check if the first result is an actor
            if search_results:
                if isinstance(search_results[0], imdb.Person.Person):
                    return search_results[0]
            return False
        except IMDbError as e:
            if str(e) == "timeout":
                return -1

    def isMovie(self, name):
        try:
            search_results = self.ia.search_movie(name)

            # check if the first result is a movie
            if search_results:
                if isinstance(search_results[0], imdb.Movie.Movie):
                    return search_results[0]
            return False
        except IMDbError as e:
            if str(e) == "timeout":
                return -1

    def checkDict(self, input):
        a = self.actorDict.get(input, -1)
        m = self.movieDict.get(input, -1)
        
        # If an actor or a movie is not in the dictionary and is close enough to
        # the IMDb name, it gets added to the dictionary with the name as the value.
        # Otherwise, it gets a 0, meaning no match or too broad
        if a == -1:
            act = self.isActor(input)
            if act and act != -1:
                rat = fuzz.ratio(input, act)
                if rat<=5:
                    self.actorDict[input] = act
            else:
                self.actorDict[input] = 0
        
        if m == -1:
            mov = self.isMovie(input)
            if mov and mov != -1:
                rat = fuzz.ratio(input, mov)
                if rat<=5:
                    self.movieDict[input] = mov
            else:
                self.movieDict[input] = 0

        # 1 is if the actor/movie is valid
        # 0 is if there was no match/too broad of a search
        # -1 is if the key is not in the dictionary yet
        
        a2 = self.actorDict.get(input, -1)
        m2 = self.movieDict.get(input, -1)

        if a2 != 0 and a2 != -1:
            return a2
        elif m2 != 0 and m2 != -1:
            return m2
        elif a2 == 0 and m2 == 0:
                return False


actor = input("Enter an actor name: ")
check = checker('gg',2018)
a = check.checkDict(actor)
#a = check.isActor(actor)
print(a)


# a = isActor(actor)
# m = isMovie(movie)
# if a and a != -1:
#     if m and m != -1:
#         print(a,"and",m)
#     else:
#         print(a)
# else:
#     if m and m != -1:
#         print(m)
#     else:
#         print('None')