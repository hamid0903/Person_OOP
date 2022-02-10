class Student:
    def __init__(self,first_name,last_name,birth_date,major):
        self.first_name=first_name
        self.last_name=last_name
        self.birth_date=birth_date
        self.major=major


    def get_age(self):
        age=2022-self.birth_date
        return age


        
    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

