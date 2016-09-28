temp_dict = {
    "jason" : '770-712-5142'
}

print "Electronic Phone Book"
print "====================="
print "1\. Look up an entry \n"
print "2\. Set an entry \n"
print "3\. Delete an entry \n"
print "4\. List all entries \n"
print "5\. Quit \n"
menu_select = int(raw_input("What do you want to do (1-5)? "))

if menu_select == 1:
    name_look_up = raw_input("Name: ").lower()
    name_find = name_look_up in temp_dict
    if name_find:
        tel = temp_dict[name_look_up]
        print "Found entry for %s: %r" % (name_look_up, tel)
    else:
        print "No entry found for %s" %name_look_up
