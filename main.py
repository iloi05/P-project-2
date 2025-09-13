# Name: Ivy Loi
# Date: 9/11/25
# Purpose: Implementing functions from contacts.py in this file

from contacts import *

contacts = None
choices = ["1", "2", "3", "4", "5", "6", "7"]

while True:
    print("       *** EMPLOYEE CONTACT MAIN MENU      ")
    print()
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit the program")
    print()
    prompt = input("Enter menu choice: ")
    if prompt == "1":
        print_list(contacts)
    elif prompt == "2":
        add_contact(contacts)
    elif prompt == "3":
        modify_contact(contacts)
    elif prompt == "4":
        delete_contact(contacts)
    elif prompt == "5":
        # ask alton
    elif prompt == "6":
        # should be same as 5
    elif prompt == "7":
        break
    if prompt not in choices:
        print("You've chosen an invalid option try again")
        continue
    