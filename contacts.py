# Name: Ivy Loi
# Date: 9/11/25
# Purpose: This file is supposed to hold the functions that will be used in main.py

def add_contact(contacts, /, *, first, last):
    """Adds names to the contact list"""
    contacts.append([first, last])

def modify_contact(contacts, /, *, nfirst, nlast, index):
    if -1 <= index < len(contacts):
        contacts[index] = [nfirst, nlast]
        return True
    else:
        return False
    
def delete_contact(contacts, /, *, index):
    if -1 <= index < len(contacts):
        contacts.pop(contacts[index])
        return True
    else:
        return False
    
def sort_contacts(contacts, /, *, column):
    if column == 0:
        contacts.sort(key = lambda name: name.split()[0])
    elif column == 1:
        contacts.sort(key = lambda name: name.split()[-1])