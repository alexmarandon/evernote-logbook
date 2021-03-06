from datetime import timedelta, datetime
from dateutil.relativedelta import *
import locale

date_format = '%Y%m%d - %A %-d %B %Y'

year_month = raw_input('Enter the Year/Month (YYYYMM): ')
if ( len(year_month) < 1 ) : year_month = '201403'

current_date = datetime.strptime(year_month+'01', '%Y%m%d')
final_date = current_date +relativedelta(months=+1)

while current_date<final_date:
    locale.setlocale(locale.LC_TIME, "fr_FR")
    current_date_formatted = datetime.strftime(current_date, date_format).lower()
    print(current_date_formatted)
    locale.setlocale(locale.LC_TIME, "en_US")
    year_tag = "ww:"+str(current_date.isocalendar()[0])
    month_tag = "mm:"+datetime.strftime(current_date, '%B').lower()
    day_tag = "dd:"+datetime.strftime(current_date, '%A').lower()
    week_tag = "ww:"+str(current_date.isocalendar()[1]).zfill(2)
    print(year_tag, month_tag, week_tag, day_tag)
    current_date+=timedelta(days=1)