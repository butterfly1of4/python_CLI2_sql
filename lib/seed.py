from peewee import *
from models import *
        
db.drop_tables([Contacts])
db.create_tables([Contacts])
 
judy = Contacts(first_name='Judy', last_name='Houck', number='3016397120', email='judy@gmail.com')
judy.save()
aimee = Contacts(first_name='Aimee', last_name='Houck', number='3014713212', email='aimee0@gmail.com')
aimee.save()

# def findByFirstName():



# print(aimee)
# print(judy)


#Example   
# class Contacts(BaseModel):
#     name = CharField()
#     birthday = DateField()
    
# db.create_tables([Contacts])
    
# zakk = Contacts(name='Zakk', birthday=date(1990, 11, 18))
# zakk.save()