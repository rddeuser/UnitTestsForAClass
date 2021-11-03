"""
Program: Customer
Author: Becca Deuser
Last date modified: 11/02/2021

The purpose of this program is to create an invoice class
"""


class Invoice:
    """Invoice class"""
    # Constructor
    def __init__(self, invoice_id, customer_id, address, last_name, first_name, phone_number, items_with_price=dict()):
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number
        self._customer_id = customer_id
        self._invoice_id = invoice_id
        self._items_with_price = items_with_price

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

    def set_invoice_id(self, invoice_id):
        self._invoice_id = invoice_id

    def set_items_with_price(self, items_with_price):
        self._items_with_price = items_with_price

    def add_item(self, item):
        self._items_with_price.update(item)

    def create_invoice(self):
        total = 0

        for i in self._items_with_price.keys():
            print(i + ".....$" + "{:.2f}".format(self._items_with_price[i]))
            total += self._items_with_price[i]

        tax = total * .06
        print("Tax.....$" + "{:.2f}".format(tax))
        print("Total.....$" + "{:.2f}".format(total))

    def __str__(self):
        return "Invoice ID: " + str(self._invoice_id) + "\nCustomer ID: " + str(self._customer_id) + "\n" + str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Phone Number: " + str(self._phone_number) + "\n" + str(self._items_with_price)

    def __repr__(self):
        return "Invoice ID: " + str(self._invoice_id) + "\nCustomer ID: " + str(self._customer_id) + "\n" + str(self._first_name) + " " + str(self._last_name) + "\n" + str(self._address) + "\n" + "Phone Number: " + str(self._phone_number) + "\n" + str(self._items_with_price)


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
