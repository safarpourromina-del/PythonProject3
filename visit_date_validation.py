from datetime import datetime
from datetime import time
def date_validation(my_date):
    datetime.strptime(my_date, '%Y-%m-%d').date()

def time_validation(my_time):
    datetime.strptime(my_time, '%H:%M').time()



