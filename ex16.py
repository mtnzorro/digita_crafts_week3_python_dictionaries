from sys import argv
script, filename = argv

print "We're going to erase %r" % filename
print "If no, hit ctrl-c"
print "If ok, hit enter"

raw_input ("?")

print "Opening file......."
target = open(filename, 'w')

print "Truncation!  Bye!"
target.truncate()

print "Now I'm asking you for 3 lines:"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally we close it."
target.close()
