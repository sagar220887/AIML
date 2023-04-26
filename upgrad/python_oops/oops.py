
# its a blueprint for the instances
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@company.com"

    def display_details(self):
        print("first name - ", self.first)
        print("last name - ", self.last)
        print("email - ", self.email)
        print("pay - ", self.pay)




# emp1 = Employee()
# emp2 = Employee()

# emp1.first = 'Corey'
# emp1.last = 'derge'
# emp1.email = 'a@gmail.com'
# emp1.pay = 40000


# emp2.first = 'Sagar'
# emp2.last = 'sahoo'
# emp2.email = 'ss@gmail.com'
# emp2.pay = 30000

# print(emp1.first)


emp1 = Employee('sagar', 'sahoo','20000')
emp1.display_details()

