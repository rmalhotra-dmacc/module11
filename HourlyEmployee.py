"""
Author: Rajiv Malhotra
Program: HourlyEmployee.py
Date: 11/08/2020

Hourly Employee class definition
"""

from datetime import date


from Employee import Employee

class HourlyEmployee(Employee):
    """ Hourly Employee Class"""
    #Contructor
    def __init__(self, lname, fname, address, pnum, start_dt, hourly_pay):
        super().__init__(lname, fname, address, pnum)  # calls the base constructor
        self.start_dt = start_dt
        self.hourly_pay = hourly_pay

    @property
    def start_dt(self):
        return self._start_dt

    @start_dt.setter
    def start_dt(self, value):
        self._start_dt = value

    @property
    def hourly_pay(self):
        return self._hourly_pay

    @hourly_pay.setter
    def hourly_pay(self, value):
        if not isinstance(value, float):
            raise ValueError
        self._hourly_pay = value

    def give_raise(self, new_hourly_pay):
        """ Function for hourly_pay raise """
        if new_hourly_pay <= self.hourly_pay:
            raise ValueError("Pay raise cannot be less than current rate")
        self.hourly_pay = new_hourly_pay

    def display(self):
        return Employee.display(self) + ", " + str(self.start_dt) + ", $" + str(self.hourly_pay) + "/hr"

#Drivers
try:
    hourly_employee = HourlyEmployee('Doe', 'John', '', '515-222-2222', date.today(), 10.00)
    print(hourly_employee.display())
    hourly_employee.give_raise(12.00)
    print(hourly_employee.display())
except ValueError as err:
    print(err)

del hourly_employee
