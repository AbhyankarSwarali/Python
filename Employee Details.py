class Employee:
    emp_count = 101

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.eid = 'e' + str(Employee.emp_count)
        Employee.emp_count += 1

    def show_details(self):
        print('Name: ', self.name)
        print('Employee ID: ',self.eid)
        print('Salary: ', self.salary)
        print('Designation: ', self.designation)
    
    @classmethod
    def total_emp(cls):
        return cls.emp_count - 101
    

e1 = Employee('Swarali', '50000', 'Data Analyst')
e1.show_details()
print(' ')

e2 = Employee('Anuj', '60000', 'Web Developer')
e2.show_details()
print(' ')

print('Total employees: ', e1.total_emp())