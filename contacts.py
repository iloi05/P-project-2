# Name: Ivy Loi
# Date: 9/11/25
# Purpose: This file is supposed to hold the functions that will be used in main.py

def print_list(contacts):
    """Contact list printing"""
    print("================== CONTACT LIST ==================")
    print("Index  First Name           Last Name")
    print("====== ==================== ====================")
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

def add_contact(contacts, /, *, first, last):
    """Adds names to the contact list"""
    contacts.append([first, last])

def modify_contact(contacts, /, *, nfirst, nlast, index):
    """Modifying contact information in system"""
    n = input("Enter the index number: ")
    n_int = int(n)
    if -1 <= index < len(contacts):
        contacts[index] = [nfirst, nlast]
        return True
    else:
        return False
    
def delete_contact(contacts, /, *, index):
    """Deletes contacts in list"""
    if -1 <= index < len(contacts):
        contacts.pop(contacts[index])
        return True
    else:
        return False
    
def sort_contacts(contacts, /, *, column):
    """Sorts names by first and last names"""
    if column == 0:
        contacts.sort(key = lambda name: name.split()[0])
    elif column == 1:
        contacts.sort(key = lambda name: name.split()[-1])