"""
Name: Dylan Embrey
hw11.py
Problem: This will take a class and give out info based on an empolyee at a sales company.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """
    Represents an algorithm for typing out specific people from a sales company and showing their name.
    """

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        sale_total = 0
        for i in self.sales:
            sale_total += i
        return sale_total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        extra_sales = other.total_sales()
        if self.total_sales() < extra_sales:
            return -1
        if self.total_sales() > extra_sales:
            return 1
        return 0

    def __str__(self):
        final = (str(self.get_id())), self.name, (str(self.total_sales()))
        final = list(final)
        return final
