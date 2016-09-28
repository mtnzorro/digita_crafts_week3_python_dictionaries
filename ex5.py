from sys import argv
script, filename = argv


target = open(filename)
text = target.read()
blues = text.replace('.', '').replace('(', '').replace(')', '').replace(',', '').replace('!', '').lower()
blues = blues.split()
char_dict = {}
#temp_word = []
for word in blues:

    #if char == " " or char == "," or char == "!":
    #    word = "".join(temp_word).lower()
    char_dict[word] = char_dict.get(word, 0) + 1
    #    temp_word = []
    #else:
    #    temp_word.append(char)


for char, count in char_dict.items():
    print "%s : %d" % (char, count)

target.close()
