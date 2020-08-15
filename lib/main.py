from peewee import *
from models import Contacts


print("My Contacts:")

on = True
while on == True:

    def intro():
        print("\nPlease choose from the following menu options: \n")
        print("1: For a list of All Contacts: Type 'all'; \n")
        print("2: To find One contact by first-name: Type the first name of the person you're looking for;\n ")
        print("3: To create a New contact: Type 'new'\n")
        print("4: To exit the program: Type 'exit\n")
    intro()
    menu = input("Type your choice: ")
# EXIT CHECK

    def checkExit():
        if menu == 'exit':
            on == False
            print("Goodbye")
        else:
            print('go on')
        checkExit()
# FIND ALL

    def findAll():
        all = Contacts.select()
        for entry in all:
            print(entry.first_name, entry.last_name, entry.number, entry.email)
    if menu == 'all':
        findAll()

        continue

# CREATE
    def createContact():

        first = input("First Name: ")
        last = input("Last Name: ")
        number = input("Phone Number: ")
        email = input("Email: ")
        Contacts.create(first_name=first, last_name=last,
                        number=number, email=email)
    if (menu == 'new'):
        createContact()

        continue

# FIND ONE BY FIRST NAME
    def findName():
        person = Contacts.get(Contacts.first_name == menu)
        print(person.first_name, person.last_name, person.number, person.email)
    if menu == Contacts.first_name and menu != 'exit':
        findName()
        continue
    elif menu == 'exit':
        break

# EXIT
else:
    on == False
    menu == 'exit'
    print("exiting")
