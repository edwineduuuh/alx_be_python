from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()

    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Today's date: {formatted_datetime}")

display_current_datetime()


def calculate_future_date():
    try:
        number_of_days = int(input("Enter the number of days to add: "))
    except ValueError:
        print("Please enter a valid number of days")
        return

    current_date = datetime.now()

    future_date = current_date + timedelta(days=number_of_days)

    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Future date: {formatted_future_date}")

calculate_future_date()
