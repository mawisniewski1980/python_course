from datetime import date

from weather.model import Weather
from weather.weather_api import get_weather, get_weather_details

# https://openweathermap.org/forecast5


def main(mock=True):
    user_city: str = input('Enter a city: ')

    # Get the current_weather details
    current_weather: dict = get_weather(user_city, mock)
    weather_details: list[Weather] = get_weather_details(current_weather)

    # Get the currenct_days
    dfmt: str = '%d/%m/%y'
    days: list[str] = sorted({f'{date.date:{dfmt}}' for date in weather_details})
    # print(days)

    for day in days:
        print(day)
        print('---')

        grouped: list[Weather] = [current for current in weather_details if f'{current.date:{dfmt}}' == day]
        for element in grouped:
            print(element)

        print('')


if __name__ == '__main__':
    main()
