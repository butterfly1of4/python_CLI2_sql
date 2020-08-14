from peewee import *
from models import Contacts


print("My Contacts:")
# False = off- stop running
# True = on- keep running
# on = False
print("Please choose from the following menu options: \n")
print("For a list of All Contacts: Type 'all'; \n")
print("To find One contact by first-name: Type the first name of the person you're looking for;\n ")
print("To create a New contact: Type 'new'\n")

menu = input("Type your choice: ")

# print(menu)


def findAll():

    all = Contacts.select()
    for entry in all:
        print(entry.first_name, entry.last_name, entry.number, entry.email)


    # findAll()
if menu == 'all':  # and on == True:
    findAll()
    # restart()

    # on==False

# CREATE


def createContact():
    # on == True
    first = input("First Name: ")
    last = input("Last Name: ")
    number = input("Phone Number: ")
    email = input("Email: ")
    Contacts.create(first_name=first, last_name=last,
                    number=number, email=email)


    # c.save()
    # createContact()
    # on == False
if (menu == 'new'):
    createContact()
    # restart()


# FIND ONE
def findName():
    # on ==True
    person = Contacts.get(Contacts.first_name == menu)
    print(person.first_name, person.last_name, person.number, person.email)


    # findName()
if menu == Contacts.first_name:
    findName()
    # on == False
    # restart()


# def restart():
#     while on == False:
#         menu == menu
#     if  on==True:
#         print('stop')
# restart()


# if menu == 'exit':
    # on == True;
