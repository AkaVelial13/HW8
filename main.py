from datetime import datetime, timedelta, date


def get_birthdays_per_week(users):
    today = date.today()
    birthdays_per_week = {day: [] for day in
                          ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()

        if today > birthday_this_year:
            birthday_next_year = datetime(today.year + 1, birthday.month, birthday.day).date()
        else:
            birthday_next_year = birthday_this_year

        if today <= birthday_next_year <= today + timedelta(days=7):
            if birthday_next_year.weekday() == 5:  # Суббота
                birthday_next_year += timedelta(days=2)
            elif birthday_next_year.weekday() == 6:  # Воскресенье
                birthday_next_year += timedelta(days=1)

            day_of_week = birthday_next_year.strftime('%A')
            if birthday_next_year <= today + timedelta(
                    days=7):  # Учитываем только те дни рождения, которые в пределах недели
                birthdays_per_week[day_of_week].append(name.split()[0])

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan", "birthday": datetime(1976, 2, 6).date()},
        {"name": "Rina", "birthday": datetime(1976, 2, 4).date()},
        {"name": "Sabrina", "birthday": datetime(1976, 2, 3).date()},
        {"name": "Marina", "birthday": datetime(1976, 2, 8).date()},
        {"name": "Irina", "birthday": datetime(1976, 2, 7).date()},
        {"name": "Arina", "birthday": datetime(1976, 2, 10).date()},
        {"name": "Angelina", "birthday": datetime(1976, 2, 9).date()},
    ]

    result = get_birthdays_per_week(users)

    for day_name, names in result.items():
        if names:
            print(f"{day_name}: {', '.join(names)}")
