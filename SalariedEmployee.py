"""
Author: Rajiv Malhotra
Program: SalariedEmployee.py
Date: 11/08/2020

Salaried Employee class definition
"""

from datetime import date


from Employee import Employee

class SalariedEmployee(Employee):
    """ Salaried Employee Class"""
    #Contructor
    def __init__(self, lname, fname, address, pnum, start_dt, salary):
        super().__init__(lname, fname, address, pnum)  # calls the base constructor
        self.start_dt = start_dt
        self.salary = salary

    @property
    def start_dt(self):
        return self._start_dt

    @start_dt.setter
    def start_dt(self, value):
        self._start_dt = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, float):
            raise ValueError
        self._salary = value

    def give_raise(self, salary_raise):
        """ Function for Salary raise """
        if salary_raise <= self.salary:
            raise ValueError("New salary cannot be less than current salary")
        self.salary = salary_raise

    def display(self):
        return Employee.display(self) + ", " + str(self.start_dt) + ", $" + str(self.salary) + "/year"

#Driver
try:
    salaried_employee = SalariedEmployee('Doe', 'John', '', '515-222-2222', date.today(), 40000.00)
    print(salaried_employee.display())
    salaried_employee.give_raise(45000.00)
    print(salaried_employee.display())
except ValueError as err:
    print(err)

del salaried_employee
