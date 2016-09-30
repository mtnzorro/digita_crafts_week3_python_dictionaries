import pickle
from os.path import exists

if exists('telephone_book.pickle'):
    myfile = open('telephone_book.pickle', 'r')
    temp_dict = pickle.load(myfile)

else:
    temp_dict = {}

def phone_book_program():

    #Functions:


    def name_search():
        name_look_up = raw_input("Name: ").lower().title()
        name_find = name_look_up in temp_dict
        if name_find:
            tel = temp_dict[name_look_up]
            name_look_up = name_look_up.title()
            print "Found entry for %s: %r" % (name_look_up, tel)
        else:
            print "No entry found for %s" % name_look_up


    def entry_set():
        name_set = raw_input("Name: ").lower().title()
        which_number =  raw_input("Work, Cell, or Home number? ").lower()
        if name_set in temp_dict:
            if "work" in temp_dict[name_set]:
                pass
            elif "cell" in temp_dict[name_set]:
                pass
            else:
                "home" in temp_dict[name_set]

        else:
            temp_dict[name_set] = {}

        if which_number == "cell":
            cell_number = raw_input("Enter cell number: ")
            temp_dict[name_set]['cell'] = cell_number
        elif which_number == "work":
            work_number = raw_input("Enter work number: ")
            temp_dict[name_set]['work'] = work_number
        elif which_number == "home":
            home_number = raw_input("Enter home number: ")
            temp_dict[name_set]['home'] = home_number
        else:
            pass
        name_set = name_set.title()
        print "Entry stored for %s" % name_set


    def entry_delete():
        name_look_up = raw_input("Name: ").lower()
        name_find = name_look_up in temp_dict
        if name_find:
            del temp_dict[name_look_up]
            print "Deleted entry for %s" % name_look_up
        else:
            print "No entry found for %s" %name_look_up


    def entry_print_list():
        for names, tels in temp_dict.iteritems():
            cell_number = tels.get("cell", "N/A")
            home_number = tels.get("home", "N/A")
            work_number = tels.get("work", "N/A")
            print "Found entry for %s : Cell number: %s, Home number: %s, Work number: %s" % (names, cell_number, home_number, work_number)


    def entry_save():
        myfile = open('telephone_book.pickle', 'w')
        pickle.dump(temp_dict, myfile)
        myfile.close()
        print "Phone book saved."

    def quit_the_program():
        return False

    def menu_option_enter():
        x = True
        while x == True:
            print "Electronic Phone Book"
            print "====================="
            print "1\. Look up an entry \n"
            print "2\. Set an entry \n"
            print "3\. Delete an entry \n"
            print "4\. List all entries \n"
            print "5\. Save entries \n"
            print "6\. Quit \n"
            a = int(raw_input("What do you want to do (1-6)? "))

            if a == 1:
                name_search()
            elif a == 2:
                entry_set()
            elif a == 3:
                entry_delete()
            elif a == 4:
                entry_print_list()
            elif a == 5:
                entry_save()
            elif a == 6:
                print "Bye!"
                x = False
            else:
                print "Invalid option."






    menu_option_enter()



phone_book_program()
