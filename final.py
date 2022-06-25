# program to show timezone in Colombia and the user's timezone

import pytz
import datetime
from time import sleep


#show all the timezones
print('Look all the timezones in the world:')
sleep(2)
for i in pytz.all_timezones:
    print(i)
    sleep(0.01)

#function to compare the timezones
def difference_col(fun):
    def wrapper(text: str):
        Colombia = pytz.timezone('America/Bogota')
        date_col = datetime.datetime.now(Colombia)
        date_user = datetime.datetime.now(fun(text))
        return print('The hour in Bogotá is:', date_col.strftime('%d/%m/%Y %H:%M:%S'), 'and your hour is: ', date_user.strftime('%d/%m/%Y %H:%M:%S'))
    return wrapper

#function to receive the timezone
@difference_col
def user_timezone(zone: str) -> str:
    if zone not in pytz.all_timezones:
        raise ValueError('The timezone is not valid')
    return pytz.timezone(zone)


user_timezone(input('Copy the timezone that you want compare with Colombian Zone: '))


