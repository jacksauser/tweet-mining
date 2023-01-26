class Award:
    awardName = ""
    winner = ""
    nominees = []



class AwardShow:
    
    showName = ""
    year = ""
    host = ""
    awards = []

    def __init__(self, name, year):
        self.showName = name
        self.year = year

    
