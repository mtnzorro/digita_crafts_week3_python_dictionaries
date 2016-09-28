from sys import argv
script, filename = argv


target = open(filename)
text = target.read()
blues = text.replace('.', '').replace('(', '').replace(')', '').lower()
blues = blues.split()
char_dict = {}
temp_word = []
for word in blues:

    #if char == " " or char == "," or char == "!":
    #    word = "".join(temp_word).lower()
    char_dict[word] = char_dict.get(word, 0) + 1
    #    temp_word = []
    #else:
    #    temp_word.append(char)

popular_words = sorted(char_dict, key = char_dict.get, reverse = True)
top_10 = popular_words[:10]
print top_10


target.close()
