# Name: Ivy Loi
# Date: 9/11/25
# Purpose: This file is supposed to hold the functions that will be used in main.py

def integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def print_list(contacts):
    """Contact list printing"""
    if not contacts:
        print("The list is empty, put a name in first")
    else:
        print("================== CONTACT LIST ==================")
        print("Index  First Name           Last Name")
        print("====== ==================== ====================")
        for i, contact in enumerate(contacts):
            print(f"{i:<6} {contact['first']:<20} {contact['last']:<20}")

def add_contact(contacts, /, *, first, last):
    """Adds names to the contact list"""
    contacts.append({"first": first, "last": last})

def modify_contact(contacts, /, *, nfirst, nlast, index):
    """Modifying contact information in system"""
    n = input("Enter the index number: ")
    n_int = int(n)
    if -1 <= index < len(contacts) and integer(n_int):
        contacts[index] = [nfirst, nlast]
        return True
    else:
        print("An invalid option was entered, please try again")
        return False
    
def delete_contact(contacts, /, *, index):
    """Deletes contacts in list"""
    n = input("Enter the index number: ")
    n_int = int(n)
    if -1 <= index < len(contacts) and integer(n_int):
        contacts.pop(contacts[index])
        return True
    else:
        print("An invalid option was entered, please try again")
        return False
    
def sort_contacts(contacts, /, *, column):
    """Sorts names by first and last names"""
    if column == 0:
        contacts.sort(key = lambda name: name.split()[0])
    elif column == 1:
        contacts.sort(key = lambda name: name.split()[-1])