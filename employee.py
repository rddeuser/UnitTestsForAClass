"""
Program: Employee
Author: Becca Deuser
Last date modified: 11/02/2021

The purpose of this program is to create an employee class
"""


class Employee:
    """Employee Class"""
    # Constructor
    def __init__(self, lname, fname, address, phone_number, salaried, start_date, salary):
        self._last_name = lname
        self._first_name = fname
        self._address = address
        self._phone_number = phone_number
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary

    def set_last_name(self, lname):
        self._last_name = lname

    def set_first_name(self, fname):
        self._first_name = fname

    def set_address(self, address):
        self._address = address

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_salaried(self, salaried):
        self._salaried = salaried

    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_salary(self, salary):
        self._salary = salary

    def display(self):
        if self._salaried:
            display_string = str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Salaried Employee: $" + str(self._salary) + "/year\n" + "Start Date: " + str(self._start_date)
        else:
            display_string = str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Hourly Employee: $" + str(self._salary) + "/hour\n" + "Start Date: " + str(self._start_date)

        return display_string

    def __str__(self):
        if self._salaried:
            display_string = str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Salaried Employee: $" + str(self._salary) + "/year\n" + "Start Date: " + str(self._start_date)
        else:
            display_string = str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Hourly Employee: $" + str(self._salary) + "/hour\n" + "Start Date: " + str(self._start_date)

        return display_string

    def __repr__(self):
        if self._salaried:
            display_string = str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Salaried Employee: $" + str(self._salary) + "/year\n" + "Start Date: " + str(self._start_date)
        else:
            display_string = str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Hourly Employee: $" + str(self._salary) + "/hour\n" + "Start Date: " + str(self._start_date)

        return display_string


# Driver
emp = Employee('Ruiz', 'Matthew', '123 Main Street\nUrbandale, Iowa', '515-555-1234', False, '05-01-02', 12.76)   # call the construtor
emp.set_first_name('Matt')
print(emp.display())                # display returns a str, so print the information
del emp
