class Employee:
    def __init__(self,id, name):
        self.id = id
        self.name = name

class Programmer(Employee):
    def __init__(self, id, name,lang):
        super().__init__(id, name)
        self.lang = lang

emp1 = Employee('1234', 'Waleed')
umar = Programmer('1122', 'Umar','Python')

print(emp1.id)
print(emp1.name)
print(umar.id, umar.name, umar.lang)