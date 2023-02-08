import imdb
from fuzzywuzzy import fuzz

# get the string input
#actor = input("Enter an actor name: ")
#movie = input("Enter movie name: ")

class checker:
    
    # Create dictionaries for movies and actors
    actorDict = {}
    movieDict = {}
    
    # create an instance of the IMDb class
    ia = imdb.IMDb()

    # Initialize
    def __init__(self, name, year):
        self.showName = name
        self.year = year

    # Checks if a name is an actor by accessing IMDb
    # Returns the IMDb matched name if found, 0 if no match, and -1 if there is a timeout
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

    # Same as isActor above, but for movies
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

    # Checks the dictionaries to see if a name exists
    # If found, returns the value which is the name or a 0
    # If not found, uses isActor and isMovie to find nearest match and compares string similarity
    # If input string and IMDb string are similar enough, updates value with the official name (typo checker)
    # After adding new elements to the dictionary, checks again for initial string and returns the value
    # This function will either output the official name of an actor/movie or a 0
    def checkDict(self, input):
        a = self.actorDict.get(input, -1)
        m = self.movieDict.get(input, -1)
        
        # If an actor or a movie is not in the dictionary and is close enough to
        # the IMDb name, it gets added to the dictionary with the name as the value.
        # Otherwise, it gets a 0, meaning no match or too broad
        # This uses Levenshtein distance and accepts anything above a 70% similarity
        if a == -1:
            act = self.isActor(input)
            if act and act != -1:
                rat = fuzz.ratio(input, act)
                if rat>=70:
                    self.actorDict[input] = act
            else:
                self.actorDict[input] = 0
        
        if m == -1:
            mov = self.isMovie(input)
            if mov and mov != -1:
                rat = fuzz.ratio(input, mov)
                if rat>=70:
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
        else:
            return 0

    def checkActor(self, input):
        a = self.actorDict.get(input, -1)
        
        if a == -1:
            act = self.isActor(input)
            if act and act != -1:
                rat = fuzz.ratio(input, act)
                if rat>=80:
                    self.actorDict[input] = act
            else:
                self.actorDict[input] = 0
        
        a2 = self.actorDict.get(input, -1)

        if a2 != 0 and a2 != -1:
            return a2
        else:
            return 0

    def checkMovie(self, input):

        m = self.movieDict.get(input, -1)
        
        if m == -1:
            mov = self.isMovie(input)
            if mov and mov != -1:
                rat = fuzz.ratio(input, mov)
                if rat>80:
                    self.movieDict[input] = mov
            else:
                self.movieDict[input] = 0

        m2 = self.movieDict.get(input, -1)

        if m2 != 0 and m2 != -1:
            return m2
        else:
            return 0
        
# Quick testing function
# actor = input("Enter a name: ")
# check = checker('Golden Globes',2013)
# a = check.isMovie(actor)
# print(a)
