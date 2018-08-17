import time

today = time.strftime('%m%d')
print(today)

birthdays = {"Rose Garrison": '0111', 'Liam Gunn': '0211', 'Ryan Gunn': '0219', 'Elicia Wicker': '0305',
             'Hudson Wicker': '0310', 'Kathy Garrison': '0327', 'Kirby Garrison': '0409', 'Lily Garrison': '0420',
             'Cameron Timm': '0420', 'Jaxon Mertens': '0612', 'Chelsey Timm': '0611', 'Kyle Gunn': '0619',
             'Owen Gunn': '0627', 'Hallie Mandato': '0708', 'Ava Worcester': '0729', 'Marirose Mandato': '0901',
             'Sophie Garrison': '0913', 'Judy Garrison': '0914', 'Aiden Wicker': '0917', 'Shawn Mortenson': '0919',
             'Greg Gunn': '0920', 'Lorelei Gunn': '0926', 'Ahnna Timm': '0929', 'Kim Mortenson': '1016',
             'Kandice Gunn': '1016', 'Kristin Gunn': '1115', 'Alyssa Burke': '1115', 'Justen Timm': '1229',
             'This Script': '0816'}


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




