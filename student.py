from person import Person
class Student(Person):
    def __init__(self,first_name,last_name,birth_date,major):
        Person.__init__(self,first_name,last_name,birth_date)
        self.major = major

    def get_major(self):
        return self.major


#student1 = Student("Malik", "Ubaydullaev", 1986, "History")
#print(student1.first_name)

