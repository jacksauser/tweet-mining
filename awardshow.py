from helper import *

class Award:
    awardName = ""
    winner = ""
    nominees = []
    presenters = []


class AwardShow:
    
    showName = ""
    year = ""
    host = []
    awards = []

    def __init__(self, name, year):
        self.showName = name
        self.year = year

    def print_readable(self):
        print_hosts(self.host)
        print_awards(self.awards)
        additional_goals(c.regex_dressed, c.regex_worst_dressed, c.regex_name, c.regex_funniest, c.regex_deserve)

    def make_json(self):
        award_dict = {award.awardName: {"nominees": award.nominees, "presenters": award.presenters, "winner": award.winner} for award in self.awards}
        x = {"hosts": self.host, "award_data": award_dict}
        jsonString = json.dumps(x)
        with open('goldenglobes%s.json' % self.year, 'w', encoding='utf8') as jsonFile:
            jsonFile.write(jsonString)
            jsonFile.close()
        return jsonFile

    def addHost(self, s):
        self.host.append(s)
    
    def addAward(self, a):
        if isinstance(a, Award):
            self.awards.append(a)

# a = AwardShow
# a.showName = "Golden Globes 2013"
# a.year = 7357
# a.host = ["Tina Fey", "Amy Poehler"]

# b = Award
# b.awardName = "best screenplay - motion picture"
# b.winner = "Django Unchained"
# b.nominees = ["zero dark thirty", "lincoln", "silver linings playbook", "argo"]
# b.presenters = ["robert pattinson", "amanda seyfried"]

# c = Award
# c.awardName = "best director - motion picture"
# c.winner = "ben affleck"
# c.nominees = ["kathryn bigelow", "ang lee", "steven spielberg", "quentin tarantino"]
# c.presenters = ["halle berry"]

# a.awards = [b, c]

# print(a.make_json(a))