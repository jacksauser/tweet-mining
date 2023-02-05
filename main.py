from helper import *


# collecting the award show queried and year
award_show = input("What award show? ")
year = input("What year of the "+award_show+"? ")


# autofill inputs is not specified 
if not award_show:
    award_show = "Golden Globes"
if not year:
    year = 2013
else:
    year = int(year)


#opening the data



# regex list 
regex_host = r'(?i)the\shosts'
regex_award  = r'(?i)award for'
regex_presenter = r'(?i)presenter'
regex_nominee = r'(?i)nominee for'
regex_winner = r'(?i)winner|won'
regex_remove = r'^RT\s|\sRT|(?i)goldenglobes|(?i)golden\sglobes'
regex_best = r'(?i)best'
regex_goes_to = r'(?i)goes\sto'
regex_should = r'(?i)should\shave\swon|should\'ve\swon'
regex_funniest = r'(?i)funniest|funny|hilarious'
regex_deserve = r'(?i)deserve'
regex_dressed = r'(?i)best\sdressed|beautiful|handsome|sexy|stunning|pretty|hot|looking\sgood'
regex_name = r'[A-Z][a-z]+\s[A-Z][a-z]+'

regex_award_exact = r'(?i)best\sperformances\sby\san\sactor\sin\sa\ssupporting\srole\sin\sa\smotion\spicture'


# host = getNames(getDistribution(dataSearch(regex_host)))




# awards = getAwards(getDistribution(dataSearch(regex_award)))


# potential_winner_list, award_numbers = dataSearchAward(regex_winner, awards.keys())
# potential_winners = getNames(getDistribution(potential_winner_list), awards.keys())
# real_awards = award_numbers.keys()






# print()
# print()
# print(host)
# print()
# print()
# print(real_awards)
# print()
# print()
# print(potential_winners)


#print_helper(dataSearch2(regex_best,regex_goes_to))

# # This outputs best dressed:
# thing = dataSearch2(regex_dressed, regex_name)
# output = {}
# for i in thing:
#     tweet = i[1]
#     name = re.findall(regex_name, tweet)
#     for n in name:
#         if n in output:
#             output[n] += 1
#         else:
#             output[n] = 1
# output2 = actorFilter(sorted(output, key = output.get, reverse = True)[:9])
# print(output2[:5])










# output_top10 = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True)[:10])

# print(output_top10)


# output_top = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True))

# for i in host_names_potential:
#     for j in output_top:
#         if i in j:
#             output_top[j] += 1

# print(sorted(output_top.items(), key=lambda item: item[1], reverse=True))




