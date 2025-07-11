import datetime

# 1. Запрос даты у пользователя
def input_date():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    return day, month, year

# 2. Определение дня недели
def get_weekday(day, month, year):
    date = datetime.date(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[date.weekday()]

# 3. Проверка на високосный год
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 4. Расчет возраста
def calculate_age(day, month, year):
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# 5. Вывод даты звёздочками
def print_star_date(day, month, year):
    digit_patterns = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': ['  *', '  *', '  *', '  *', '  *'],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', '***', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['***', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '***']
    }
    date_str = f"{day:02d}{month:02d}{year}"
    for line in range(5):
        for digit in date_str:
            print(digit_patterns.get(digit, ['     '])[line], end=' ')
        print()

# Основная программа
def main():
    day, month, year = input_date()
    
    print(f"\nДень недели: {get_weekday(day, month, year)}")
    print(f"Високосный год: {'Да' if is_leap(year) else 'Нет'}")
    print(f"Возраст: {calculate_age(day, month, year)} лет")
    
    print("\nДата рождения на электронном табло:")
    print_star_date(day, month, year)

if __name__ == "__main__":
    main()
