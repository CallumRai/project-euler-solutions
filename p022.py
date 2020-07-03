from string import ascii_uppercase

names = open('data\\p022_names.txt','r').read().replace('"','')
names_list = sorted(names.split(','))

alph_dict = {}
for i in range(len(ascii_uppercase)):
    alph_dict[ascii_uppercase[i]] = i+1

scores = []
for i in range(len(names_list)):
    name = names_list[i]

    score = 0
    for c in range(len(name)):
        score += alph_dict[name[c]]

    scores.append(score*(i+1))

print(sum(scores))
