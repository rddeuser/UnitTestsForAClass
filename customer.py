"""
Program: Customer
Author: Becca Deuser
Last date modified: 11/02/2021

The purpose of this program is to create a customer class with driver
"""


class Customer:
    """Customer class"""
    # Constructor
    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number
        self._customer_id = customer_id

    def set_last_name(self, lname):
        self._last_name = lname

    def set_first_name(self, fname):
        self._first_name = fname

    def set_address(self, address):
        self._address = address

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_customer_id(self, cust_id):
        self._customer_id = cust_id

    def display(self):
        return "Customer ID: " + str(self._customer_id) + "\n" + str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Phone Number: " + str(self._phone_number)

    def __str__(self):
        return "Customer ID: " + str(self._customer_id) + "\n" + str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Phone Number: " + str(self._phone_number)


    def __repr__(self):
        return "Customer ID: " + str(self._customer_id) + "\n" + str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Phone Number: " + str(self._phone_number)


# Driver
customer1 = Customer('Ruiz', 'Matthew', '123 Main Street\nUrbandale, Iowa', '515-555-1234', False, '05-01-02', 12.76)   # call the construtor
emp.set_first_name('Matt')
print(emp.display())                # display returns a str, so print the information
del emp
