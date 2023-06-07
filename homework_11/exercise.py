def count_by_year():
    file = open("birthdays.txt", "r")
    birthdays = file.read()
    birthdays = birthdays.split('\n')
    counts = dict()
    for date in birthdays:
        parts = date.split('-')
        year = int(parts[0])
        counts[year] = counts.get(year, 0)+1

    list_ = []
    for k, v in counts.items():
        list_.append((v,k))

    list_ = sorted(list_, reverse=True)
    for tup_ in list_[0:3]:
        print(tup_[1])

    file.close()


count_by_year()
