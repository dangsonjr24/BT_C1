class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

class Employee:
    def __init__(self, name, dob, doj):
        self.name = name
        self.dob = dob  # Date of Birth
        self.doj = doj  # Date of Joining

    def display(self):
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob.display()}")
        print(f"Date of Joining: {self.doj.display()}")

# Example usage:
dob = Date(15, 8, 1990)
doj = Date(1, 1, 2020)
employee = Employee("John Doe", dob, doj)
employee.display()
