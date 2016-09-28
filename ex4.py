from sys import argv
script, filename = argv


target = open(filename)
text = target.read()
text = text.replace('.', '').replace('(', '').replace(')', '')
char_dict = {}
for char in text:
    char_dict[char] = char.get(char, 0) + 1

for char, count in char_dict.items():
    print "%d %s's" % (count, char)
target.close()
