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

l = dataSearch2(regex_best,regex_goes_to)
# print_helper(l)


l2 = []
for i in l:
    l2.append(i[1])

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

print(d1)
print()
print()
print(getDistribution(l3))
print()
print()
print(nameGrabber(l4))
print()
print()

d2 = {}
for key in d1:
    d2[key] = nameGrabber(d1[key])
#     print(key)
#     print(nameGrabber(d1[key]))
#     print(d1[key])
#     print()
#     print()

# print()
# print()
# print(d2.keys())



def voter(l,person=False):
    if person:
        return getDistribution(l,regex_name)
    else:
        return getDistribution(l)

d3 = {}
for key in d2:
    d3[key] = voter(d2[key])

# print()
# print()
# print(d3)
# print()
# print()



# output_top10 = dict(sorted(host_dict.items(), key=lambda item: item[1], reverse=True)[:10])

# print(output_top10)


# output_top = d3

# for i in d3.keys():
#     for j in output_top:
#         if i in j:
#             if isinstance(output_top[j],dict):
#                 output_top[j] = 1
#             else:
#                 output_top[j] += 1

# print(sorted(output_top.items(), key=lambda item: item[1], reverse=True))

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        return(list(a_set & b_set))
    else:
        return([])


d4 = {}
for key in d3:
    d4[key] = key.split(' ')

d5 = {}
award_atlas = {}
for key in d4:
        for key2 in d4:
            if key in award_atlas and award_atlas[key] == key2 and key != key2:
                if key2 in d5:
                    d5[key2] += 3
                else:
                    d5[key2] = 3
            elif len(common_member(d4[key],d4[key2])) >= 4 and key != key2: # if they have more than 4 of the same words
                a = ((len(common_member(d4[key],d4[key2])) - 3) / 4) - .25
                longer_key = key2 if len(d4[key2]) > len(d4[key]) else key
                shorter_key = key if len(d4[key2]) > len(d4[key]) else key2
                if len(common_member(d4[key],d4[key2])) / len(d4[longer_key]) > .8 and longer_key == key2:
                    if shorter_key not in award_atlas:
                        award_atlas[shorter_key] = longer_key
                        if shorter_key in d5 and longer_key in d5:
                            d5[longer_key] += d5[shorter_key]
                        elif shorter_key in d5:
                            d5[longer_key] = d5[shorter_key]
                        elif longer_key in d5:
                            d5[longer_key] += 3
                        else:
                            d5[longer_key] = 3
                    else:
                        if shorter_key in d5 and longer_key in d5:
                            d5[longer_key] += d5[shorter_key]
                        elif shorter_key in d5:
                            d5[longer_key] = d5[shorter_key]
                        elif longer_key in d5:
                            d5[longer_key] += 3
                        else:
                            d5[longer_key] = 3
                else:
                    if key2 in d5:
                        d5[key2] += 1 + a
                    else:
                        d5[key2] = 1 +  a

                


print()
print()
# print(sorted(d5.items(), key=lambda item: item[1], reverse=True))
print()
print()
print(award_atlas)

d6 = d5
for key in award_atlas:
    award = award_atlas[key]
    if award != key:
        d6[award] += d6[key]
        d6.pop(key)

print(d6)
        