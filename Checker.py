import imdb

# create an instance of the IMDb class
ia = imdb.IMDb()

# get the string input
actor = input("Enter an actor name: ")
movie = input("Enter movie name: ")

def isActor(name):
    try:
        # search for the actor
        search_results = ia.search_person(name)

        # check if the first result is an actor
        if search_results:
            if isinstance(search_results[0], imdb.Person.Person):
                return search_results[0]
        return False
    except IMDbError as e:
        if str(e) == "timeout":
            return -1

def isMovie(name):
    try:
        search_results = ia.search_movie(name)

        # check if the first result is a movie
        if search_results:
            if isinstance(search_results[0], imdb.Movie.Movie):
                return search_results[0]
        return False
    except IMDbError as e:
        if str(e) == "timeout":
            return -1

a = isActor(actor)
m = isMovie(movie)
if a and a != -1:
    if m and m != -1:
        print(a,"and",m)
    else:
        print(a)
else:
    if m and m != -1:
        print(m)
    else:
        print('None')