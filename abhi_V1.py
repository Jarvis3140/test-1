class Employee:
    def __init__ (self,name ,age):
        self.name = name
        self.age = age
    def display_info(self):
     print(f'the name of employee is {self.name}')
     print(f'the name of employee is {self.age}')


em1 = Employee('Manticore', 24)


em1.display_info()