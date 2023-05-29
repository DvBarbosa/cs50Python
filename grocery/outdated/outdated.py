from datetime import datetime

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
    date_str = input("Enter a date (mm/dd/yyyy or Month day, year): ")
    try:
        date = None
        for fmt in ('%m/%d/%Y', '%B %d, %Y'):
            try:
                date = datetime.strptime(date_str, fmt)
                break
            except ValueError:
                pass
        if not date:
            raise ValueError("Invalid date format")
        year = date.year if date.year >= 100 else date.year + 2000
        date_formatted = date.strftime("%Y-%m-%d")
        print(date_formatted)
        break
    except ValueError as e:
        print("Invalid input:", e)
