from peewee import *
from models import Contacts

    
print("My Contacts:")
# False = off- stop running
#True = on- keep running
on = True
while True:   
        
    def intro():
        print("Please choose from the following menu options: \n")
        print("1: For a list of All Contacts: Type 'all'; \n")
        print("2: To find One contact by first-name: Type the first name of the person you're looking for;\n ")
        print("3: To create a New contact: Type 'new'\n")
    intro()
    menu = input("Type your choice: ")

# print(menu)
    
    def findAll():
        all = Contacts.select()
        for entry in all:
            print(entry.first_name, entry.last_name,entry.number,entry.email)
    # findAll()
    if menu == 'all': #and on == True:       
        findAll()
        # restart()
        continue
        # break
    # on==False
    # intro()
#CREATE 
    def createContact():
    # on == True
        first = input("First Name: ")
        last = input("Last Name: ")
        number = input("Phone Number: ")
        email = input("Email: ")
        Contacts.create(first_name = first, last_name =last, number = number, email=email)

    if (menu == 'new'):
        createContact()
        # restart()
        continue

#FIND ONE     
    def findName():
    # on ==True
        person = Contacts.get(Contacts.first_name == menu)
        print(person.first_name, person.last_name, person.number, person.email)
    # findName()
    if menu == Contacts.first_name:
        findName()
    # on == False
        # restart()  
        continue

    if menu == 'exit' or menu == 'quit' or menu == 'close':
        on  == False
        print("Goodbye")
    break
    
