
class Person:
    def __init__(self, first_name, last_name, birth_date) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.berth_date = birth_date
        
    def Get_age(self, birth_date):
        self.age = 2022 - birth_date
        return self.age
    
    def get_full_name(self,first_name, last_name):
        self.full_name = first_name + last_name
        return self.full_name

