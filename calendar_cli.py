import calendar

def display_calendar(year, month):
    try:
        print(calendar.month(year, month))
    except:
        print("Verifique o ano e o mes informados.")

def main():
    print("Calendario CLI")
    year = int(input("Digite o ano (ex: 2024): "))
    month = int(input("Digite o mes (1-12): "))
    display_calendar(year, month)
if __name__ == "__main__":
    main()