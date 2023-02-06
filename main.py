from helper import *
import awardshow

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

additional_goals(c.regex_dressed, c.regex_worst_dressed, c.regex_name, c.regex_funniest, c.regex_deserve)





# awards = getAwards(getDistribution(dataSearch(c.regex_award)))


# potential_winner_list, award_numbers = dataSearchAward(c.regex_winner, awards.keys())
# potential_winners = getNames(getDistribution(potential_winner_list), awards.keys())
# real_awards = award_numbers.keys()




#print_human_readable(c.regex_host, c.regex_dressed, c.regex_worst_dressed, c.regex_name)


# print(real_awards)
# print()
# print()
# print(potential_winners)


#print_helper(dataSearch2(regex_best,regex_goes_to))






# output_top10 = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True)[:10])

# print(output_top10)


# output_top = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True))

# for i in host_names_potential:
#     for j in output_top:
#         if i in j:
#             output_top[j] += 1

# print(sorted(output_top.items(), key=lambda item: item[1], reverse=True))




