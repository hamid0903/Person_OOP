from person import Person
class Employee(Person):
    def __init__(self,first_name,last_name,birth_date,title,salary):
        Person.__init__(self,first_name,last_name,birth_date)
        self.title = title
        self.salary=salary


    def get_salary(self):
        return self.salary
    
