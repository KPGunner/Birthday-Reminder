import time

today = time.strftime('%m%d')
print(today)

birthdays = {'This Script': '0816', 'Individuals Name': 'DOB1'}


def birthday_wish():
    for k, v in birthdays.items():
        # print(k ,v)
        if today in v:
            return('\nWish ' + k + ' a happy birthday!' )
            break
    else:
        pass

birthday_wish()

print(birthday_wish())




