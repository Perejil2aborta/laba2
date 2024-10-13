from datetime import datetime


def calculate_age():
    while True:
        birth_date = input("Введите дату рождения (дд/мм/гггг): ")
        try:
            day, month, year = map(int, birth_date.split('/'))
            birth_date = datetime(year, month, day)
            break 
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите дату в формате дд/мм/гггг.")

    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    print(f"Ваш возраст: {age} лет")


calculate_age()
