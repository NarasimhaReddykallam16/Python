class Employee:

    def __init__(self, first: str, last: str):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    @property
    def fname(self):
        return self.first+' '+self.last

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @fname.setter
    def fname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fname.deleter
    def fname(self):
        self.first = None
        self.last = None


emp1 = Employee('John', 'Smith')

emp1.fname = 'hi fg'

print(emp1.first)
print(emp1.fname)
print(emp1.email)

del emp1.fname

print(emp1.email)
