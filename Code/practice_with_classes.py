# Python OOP tutorial from Corey Schafer on Youtube


class Employee:

    num_of_employees = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.pay = pay
        self.email = ('{}.{}@bjorncorp.com'.format(first, last))

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # @staticmethod
    # def is_workday(day):
    #     if day == datetime.date.weekday(5) or day == datetime.date.weekday(6):
    #         return False
    #     else:
    #         return True


print('Enter employee info (first name, last name, pay) separated by "-": ')
emp_str = input()
emp_1 = Employee.from_string(emp_str)
print(emp_1.fullname(), emp_1.email, emp_1.pay)
