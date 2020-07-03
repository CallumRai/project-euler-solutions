from string import ascii_uppercase

words = open('data\\p042_words.txt','r').read().replace('"','')
words_list = sorted(words.split(','))

alph_dict = {}
for i in range(len(ascii_uppercase)):
    alph_dict[ascii_uppercase[i]] = i+1

triangle_dict = {}
for i in range(1,5000):
    triangle_dict[i*(i+1)*0.5] = True

for i in range(1,1000000):
    if triangle_dict.get(i) is not True:
        triangle_dict[i] = False

def get_score(word):
    score = 0
    for i in range(len(word)):
        score += alph_dict[word[i]]

    return score

tri_word = 0
for word in words_list:
    if triangle_dict[get_score(word)]:
        tri_word += 1

print(tri_word)