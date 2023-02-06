from helper import *
import awardshow
import constants as c

# collecting the award show queried and year
# award_show = input("What award show? ")
# year = input("What year of the "+award_show+"? ")


# autofill inputs is not specified 
# if not award_show:
#     award_show = "Golden Globes"
# if not year:
#     year = 2013
# else:
#     year = int(year)

# additional_goals(c.regex_dressed, c.regex_worst_dressed, c.regex_name, c.regex_funniest, c.regex_deserve)




#host = getNames(getDistribution(dataSearch(c.regex_host)))

# awards = getAwards(getDistribution(dataSearch(c.regex_award)))


# potential_winner_list, award_numbers = dataSearchAward(c.regex_winner, awards.keys())
# potential_winners = getNames(getDistribution(potential_winner_list), awards.keys())
# real_awards = award_numbers.keys()


# Gets the outliers of the hosts
# host = getNames(getDistribution(dataSearch(c.regex_host)))
# host_outliers = get_outliers(host)
# print(host_outliers)

def getHost():
    host = getNames(getDistribution(dataSearch(c.regex_host)))
    host_outliers = get_outliers(host)  
    return host_outliers

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



        


            
# regex_list = [re.compile(s) for s in award_category]
# nominees = []
# for r in regex_list:
#     thing = dataSearch2(r, r)
#     output = {}
#     for i in thing:
#         tweet = str(i[1])
# #        if re.findall(regex_person, tweet):
#         names = re.findall(regex_name, tweet)
#         for n in names:
#             if n in output:
#                 output[n]+=1
#             else:
#                 output[n] = 1
#         output2 = actorFilter(sorted(output, key = output.get, reverse = True)[:20])
#     print(output2[:5])

#     thing = dataSearch2(r, regex_nominee)
#     output = {}
#     for i in thing:
#         tweet = i[1]
#         if re.findall(regex_person, str(tweet)):
#             name = re.findall(regex_name, str(tweet))
#             for n in name:
#                 if n in output:
#                     output[n] += 1
#                 else:
#                     output[n] = 1
#             output2 = actorFilter(sorted(output, key = output.get, reverse = True)[:20])
#         elif re.findall(regex_film, str(tweet)):
#             name = nameGrabber(tweet)
#             for n in name:
#                 if n in output:
#                     output[n] += 1
#                 else:
#                     output[n] = 1
#             #output2 = movieFilter(sorted(output, key = output.get, reverse = True)[:20])
#             output2 = sorted(output, key = output.get, reverse = True)[:20]
#     #output2 = sorted(output, key = output.get, reverse = True)[:20]
#     print(output2[:5])

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        return(list(a_set & b_set))
    else:
        return([])

def findAwards():   
    l = dataSearch2(c.regex_best,c.regex_goes_to)
    # print_helper(l)


    l2 = []
    for i in l:
        l2.append(re.split(c.regex_goes_to,i[1]))

    # print(l2)
    d1 = {}
    l3 = []
    l4 = []
    for i in l2:
        a = i[0]
        # print(a)
        if a.startswith("best") or a.startswith("Best"):
            # print(a)
            if a in d1:
                l3.append(a)
                d1[a].append(i[1])
                l4.append(i[1])
            else:
                l3.append(a)
                d1[a] = [i[1]]
                l4.append(i[1])

    awards = d1.keys()
    ret = []
    for a in awards:
        split1 = a.split(' ')
        removedWord = False
        for r in ret:
            split2 = r.split(' ')
            common = common_member(split1,split2)
            if len(common) == len(split1):
                removedWord = True
        if not removedWord:
            ret.append(a)
    return(ret)
# print()
# print()
# print(getDistribution(l3))
# print()
# print()
# print(nameGrabber(l4))
# print()
# print()

# d2 = {}
# for key in d1:
#     d2[key] = nameGrabber(d1[key])
#     print(key)
#     print(nameGrabber(d1[key]))
#     print(d1[key])
#     print()
#     print()

# print()
# print()
# print(d2)