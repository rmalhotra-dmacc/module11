"""
Author: Rajiv Malhotra
Program: Employee.py
Date: 11/08/2020

Employee class definition
"""


from datetime import date


class Employee:
    """ Employee Class"""
    name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
    #Contructor
    def __init__(self, lname, fname, address, pnum):
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = pnum

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not self.name_characters.issuperset(value):
            raise ValueError
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not self.name_characters.issuperset(value):
            raise ValueError
        self._first_name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value


    def display(self):
        return self.first_name + ", " + self.last_name + " " + self.address + " " + self.phone_number

    def __str__(self):
        return "Employee: first name = " + str(self.first_name) + ", last name = " + str(self.last_name) \
            + ", Address = " + str(self.address) + ", Phone = " + str(self.phone_number)

    def __repr__(self):
        return "Employee: first name = " + repr(self.first_name) + ", last name = " + repr(self.last_name) \
            + ", Address = " + repr(self.address) + ", Phone = " + repr(self.phone_number)


#Driver
"""
tdate = date.today()
empl1 = Employee("Patel", "Sasha", "123 Main Street, Urban, Iowa 12345", "123-123-1234")
print(empl1.display())

empl2 = Employee("Patel", "Sasha", "123 Main Street, Urban, Iowa 12345", "123-123-1234")
print(empl2.display())

empl3 = Employee("Patel", "Sasha", "123 Main Street, Urban, Iowa 12345", "123-123-1234")
print(str(empl3))
print(repr(empl3))
"""
