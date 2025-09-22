import re
def name_validation(my_name):
    if re.match("r^[A-Za-z]{3,15}$", my_name):
       return my_name
    else:
        raise ValueError("Invalid Name")

def familyname_validation(my_family):
    if re.match("^[A-Za-z]{3,15}$", my_family):
        return my_family
    else:
        raise ValueError("Invalid FamilyName")

def price_validation(my_price):
    if re.match("^[1-9]{3}[0]{3,7}&toman$", my_price):
        return my_price
    else:
        raise ValueError("Invalid Price")