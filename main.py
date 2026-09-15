from lib import days_until_summer
def main():
    """
    Головна функція програми для виклику обчислення та виводу.
    """
    days = days_until_summer(15)
    print(f"До літа залишилося орієнтовно: {days} днів!")

if __name__ == "__main__":
    main()