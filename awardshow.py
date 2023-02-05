class Award:
    awardName = ""
    winner = ""
    nominees = []



class AwardShow:
    
    showName = ""
    year = ""
    host = []
    awards = []

    def __init__(self, name, year):
        self.showName = name
        self.year = year

    def print_readable(self):
        print()

    def print_json(self):
        print()

    def addHost(self, s):
        self.host.append(s)
    
    def addAward(self, a):
        if isinstance(a, Award):
            self.awards.append(a)
