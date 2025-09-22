from name_price_validation import*
from visit_date_validation import*
class VisitInfo:
    def __init__(self,visit_date,visit_time,price,name,family):
        self.visit_date = visit_date
        self.visit_time = visit_time
        self.price = price
        self.name = name
        self.family = family
    def save(self):
        print("Visit Info saved",self.visit_date, self.visit_time,self.price,self.name,self.family)

def get_visit_date(self):
    date_validation(get_visit_date)
    return self.vist_date
def get_visit_time(self):
    date_validation(get_visit_time)
    return self.visit_time
def get_price(self):
    price_validation(get_price)
    return self.price
def get_name(self):
    name_validation(get_name)
    return self.name
def get_family(self):
    familyname_validation(get_family)
    return self.family
def set_visit_date(self,vist_date):
    date_validation(set_visit_date)
    self.vist_date = vist_date
def set_visit_time(self,vist_time):
    date_validation(set_visit_time)
    self.vist_date = vist_time
def set_price(self,price):
    price_validation(set_price)
    self.price = price
def set_name(self,name):
    name_validation(set_name())
    self.name = name
def set_family(self,family):
    familyname_validation(set_family)
    self.family = family

visit_price=property(get_price,set_price)
vist_date=property(get_visit_date,set_visit_date,get_visit_date,set_visit_time)
name=property(get_name,set_name)
family=property(get_family,set_family)