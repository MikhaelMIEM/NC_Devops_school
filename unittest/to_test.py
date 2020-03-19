import requests


class Employee:
    def __init__(self, first_name, second_name, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary

    def raise_salary(self):
        self.salary *= 1.1
        return self.salary

    def form_email(self):
        raise ValueError
        return f'{self.second_name}@nc.com'

    def scedule(self):
        response = requests.get(f"http://netcracker.com/scedule/{self.second_name}")
        if response.ok:
            return response.text
        else:
            return "Bad response"
