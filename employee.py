from person import Person
class Employee(Person):
    def __init__(self,first_name,last_name,birth_date,major,):
        Person.__init__(self,first_name,last_name,birth_date)
        self.first_name = first_name

    def get_name(self):
        return self.first_name
    
