months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input('Date: ')
    try:
        if "/" in date:
            m, d, y = date.split('/')
            month = int(m)
            day = int(d)
            year = int(y)
            if month <= 12 and day <= 31:
                print (f'year-{month:02}-{day:02}')
                break
        elif "," in date:
            m, d, y = date.replace(',', '').split(' ')
            day = int(d)
            year = int(y)
            if m in months and day < 32:
                month = months.index(m) + 1
                print (f'year-{month:02}-{day:02}')
                break
            else:
                pass
    except ValueError:
        pass
