from datetime import datetime, timedelta


def main():
    users = []
    with open('birthdays.txt', 'r') as file:
        for line in file:
            data = line.split()
            birthday = data[-1]
            try:
                birthday = datetime.strptime(birthday, '%m.%d.%Y')
            except ValueError:
                birthday = datetime.strptime(birthday, '%m.%d')
            users.append({'name': " ".join(data[:-1]), 'birthday': birthday})

    get_birthday_per_week(users)


def get_birthday_per_week(user_list):
    current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    lst = [[] for i in range(7)]
    for user in who_to_congratulate(user_list):
        day_to_birthday = user['when'] - current_date
        if 0 <= day_to_birthday.days <= 6:  # 6 next days
            lst[day_to_birthday.days].append(user['name'])
    for i in range(current_date.weekday()+1, current_date.weekday()+1+7):
        if lst[i % 7]:  #to start from current day of the week
            print((current_date + timedelta(days=i)).strftime("%A") + ": " + ", ".join(lst[i % 7]))


def who_to_congratulate(user_list):
    lst = []
    for user in user_list:
        if user['birthday'].weekday() == 5:  #Saturaday
            lst.append(
                {'name': user['name'],
                'when': user['birthday'].replace(day=user['birthday'].day+2, year=datetime.now().year)}
            )
        elif user['birthday'].weekday() == 6:  #Sunday
            lst.append(
                {'name': user['name'],
                'when': user['birthday'].replace(day=user['birthday'].day+1, year=datetime.now().year)}
            )
        else:
            lst.append(
                {'name': user['name'],
                'when': user['birthday'].replace(day=user['birthday'].day, year=datetime.now().year)}
            )
    return lst


if __name__ == '__main__':
    main()


