"""
Name: Dylan Embrey
hw11.py
Problem: This will take a class and give out info based on sales from different employees.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson


class SalesForce:
    """
    Represents an algorithm for computing different sales figures and who is making the sales.
    """

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        for line in file:
            half_line = line.split()
            employee_id = int(half_line[0].replace(",", ''))
            name = half_line[1:3]
            name = " ".join(name).replace(",", '')
            sales = half_line[3:len(half_line)]
            sales_person = SalesPerson(employee_id, name)
            for i in sales:
                sale = float(i)
                sales_person.enter_sale(sale)
            self.sales_people.append(sales_person)

    def quota_report(self, quota):
        report = []
        for people in self.sales_people:
            if people.total_sales() >= quota:
                report.append([people.get_id(), people.get_name(), people.total_sales(), True])
            else:
                report.append([people.get_id(), people.get_name(), people.total_sales(), False])
        return report

    def top_seller(self):
        sells = []
        sales = 0
        for person in self.sales_people:
            if person.total_sales() > sales:
                sales = person.total_sales()
                sells = [person]
            if person.total_sales() == sales:
                sells.append(person)
        return sells

    def individual_sales(self, employee_id):
        for guy in self.sales_people:
            if guy.get_id() == employee_id:
                return guy
        return None

    def get_sale_frequencies(self):
        frequent = {}
        for employ in self.sales_people:
            for sale in employ.get_sales():
                if sale in frequent:
                    frequent[sale] += 1
                else:
                    frequent[sale] = 1
        return frequent
