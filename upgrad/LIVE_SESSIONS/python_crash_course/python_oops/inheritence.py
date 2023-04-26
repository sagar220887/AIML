class Parent():

    def last_name(self):
        print('sahoo')


class Child(Parent):

    def first_name(self):
        print('sagar')


obj1 = Child()
print(obj1.first_name())
print(obj1.last_name())
