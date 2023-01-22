import os
import sys


# collecting the award show queried and year
award_show = input("What award show? ")
year = input("What year of the "+award_show+"? ")

if not award_show:
    award_show = "Golden Globes"

if not year:
    year = 2013
else:
    year = int(year)

