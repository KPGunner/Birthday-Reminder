import time

today = time.strftime('%m%d')
print(today)
week = int(today) + 7
week = str(week)
week = week.zfill(4)
#print(week)

birthdays = {'This Script': '0816', 'Individuals Name': 'DOB1'}


def birthday_advance():
    for k, v in birthdays.items():
        # print(k ,v)
        if week in v:
            return'\nWish ' + k + ' a happy birthday on ' + v + '!'
    else:
        pass

    
def birthday_wish():
    for k, v in birthdays.items():
        if today in v:
            return '\nWish ' + k + ' a happy birthday today!'
    else:
        pass


birthday_wish()
birthday_advance()

print(birthday_wish())
print(birthday_advance())
