
class Person:
    def __init__(self,first_name,last_name,birth_date):
        self.first_name=first_name
        self.last_name=last_name
        self.birth_date=birth_date
        
    def get_age(self):
        age=2022-self.birth_date
        return age

a=Person('Ravshan','Abdulrakhman',1950)
print(a.get_age())

