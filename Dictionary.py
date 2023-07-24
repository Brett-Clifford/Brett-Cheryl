# Classes, classes are a blueprint
import datetime as dt


class Member:
    expiry_days = 365

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)
        
Joe = Member('Joe', 'Anybody')
print(Joe.firstname)
print(Joe.lastname)
print(Joe.expiry_date)
