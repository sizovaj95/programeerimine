import datetime


map_dict = {0: "Monday", 1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}


def weekday_name(weekday_num):
    weekday_name_ = map_dict[weekday_num]
    return weekday_name_


def weekdays_counts():
    with open("birthdays.txt", 'r') as f:
        birth_list = f.read()
        birth_list = birth_list.split('\n')

    counts = dict()
    for date_str in birth_list:
        parts = date_str.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        date = datetime.datetime(year, month, day)
        weekday = weekday_name(date.weekday())
        counts[weekday] = counts.get(weekday, 0) + 1
    print(counts)


weekdays_counts()
