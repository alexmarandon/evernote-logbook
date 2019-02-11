import datetime

strdate = raw_input('Enter the Date (YYYY-MM-DD):')
if ( len(strdate) < 1 ) : strdate = '2016-01-07'


weekdays = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'] 
months = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']

mydate = datetime.datetime.strptime(strdate, '%Y-%m-%d').date()

mynotetitle = mydate.strftime('%Y%m%d - ')
mynotetitle += '%s ' % weekdays[mydate.weekday()]
if mydate.day==1: mynotetitle += '%ser ' % str(mydate.day)
else: mynotetitle += '%s ' % str(mydate.day)
mynotetitle += '%s ' % months[mydate.month-1]
mynotetitle += '%s ' % str(mydate.year)

print mynotetitle