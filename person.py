
class Person:
    def __init__(self, first_name, last_name, birth_date) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
       
    def Get_age(self):
        age = 2022 - self.birth_date
        return age
    
    
    def get_full_name(self):
        full_name = self.first_name + ' ' +self.last_name
        return full_name
        
    
x = Person("Malik", "Ubaydullaev", 1986)
print(x.get_full_name(), x.Get_age())

