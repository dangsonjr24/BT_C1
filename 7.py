class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next_day(self):
        # Days in each month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check for leap year
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            days_in_month[1] = 29
        
        self.day += 1
        
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
        
        if self.month > 12:
            self.month = 1
            self.year += 1

# Example usage:
date = Date(31, 12, 2023)
date.display()  # Output: 31/12/2023
date.next_day()
date.display()  # Output: 01/01/2024
