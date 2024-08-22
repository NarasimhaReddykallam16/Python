import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@company.com'
        self.fname = first + ' ' + last

    def email(self):
        return f'{self.first}.{self.last}@company.com'

    # def fname(self):
    #     return self.first+' '+self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

    def __repr__(self):
        return f'({self.first},{self.last},{self.pay})'

    def __str__(self):
        return f'{self.fname} - {self.email}'


emp1 = Employee('Naveen', 'Reddy', 50000)
emp2 = Employee('Mahesh', 'Babu', 60000)

emp_str_1 = 'john-doe-70000'

emp3 = Employee.from_string(emp_str_1)

my_date = datetime.date(2024, 8, 17)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


dev1 = Developer('Pavan', 'Kalyan', 50000, 'Python')
dev2 = Developer('Chintal', 'Reddy', 70000, 'Java')


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def print_employees(self):
        for employee in self.employees:
            print('--> ', employee.fname)

    def add_employees(self, *emp):
        for i in emp:
            self.employees.append(i)

    def remove_employees(self, *emp):
        for i in emp:
            self.employees.remove(i)


mgr1 = Manager('Maniddep', 'Thota', 90000)
mgr2 = Manager('Ravi', 'Kiran', 100000, [dev1])

mgr1.add_employees(emp1)
