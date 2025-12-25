from datetime import datetime
from dataclasses import dataclass
import json
from typing import List

#Reading
path: str = 'text1.txt'
try:
    with open(file=path, mode='r') as f:
        print(f.read())
except FileNotFoundError:
    print(f'File not found: ({path})')

with open(path) as f:
    print(f.read(21))
    print(f.read(23))
    print()
    f.seek(0)
    print(f.read(121))
    print(f.tell())
    print(f.readline())

    lines: list[str] = f.readlines()
    print(lines)

for line in lines:
    print(line.removesuffix('\n'))

#Writing

with open('text2.txt', 'w') as f:
    print(f.write('Hello World!\n'))
    print(f.write('Hello Space!\n'))
    print(f.write('Hello Earth!\n'))
    print(f.write('Hello Galaxy!\n'))
    print(f.write('Hello Universe!\n'))

print("Contents written successfully!")

#Appending

with open('text1.txt', 'a') as f:
    print(f.write('Nobody is above the law..\n'))
    print(f.write('India is the greatest country..\n'))
    print(f.write(f"This content was added at {datetime.now():%M:%S}\n"))
    print(f.write(f"This line was added at {datetime.now():%M:%S}\n"))
    print(f.write(f"This line ended at {datetime.now():%M:%S}\n"))

#JSON

@dataclass
class DailyForecast:
    forecast_date: str
    weather: str
    min_temp: int
    max_temp: int


@dataclass
class Forecast:
    city_id: int
    city_name: str
    time_zone: str
    days: List[DailyForecast]


def get_forecast(file_path: str) -> Forecast:
    with open(file_path, 'r') as file:
        data = json.load(file)

    city = data['city']
    forecast_days = city['forecast']['forecastDay']

    days: List[DailyForecast] = []

    for day in forecast_days:
        days.append(
            DailyForecast(
                forecast_date=day['forecastDate'],
                weather=day['weather'] or "N/A",
                min_temp=int(day['minTemp']),
                max_temp=int(day['maxTemp'])
            )
        )

    return Forecast(
        city_id=city['cityId'],
        city_name=city['cityName'],
        time_zone=city['timeZone'],
        days=days
    )

def print_forecast_for_day(forecast: Forecast, date: str) -> None:
    for day in forecast.days:
        if day.forecast_date == date:
            print("-" * 40)
            print(f"City       : {forecast.city_name}")
            print(f"Date       : {day.forecast_date}")
            print(f"Weather    : {day.weather}")
            print(f"Min Temp   : {day.min_temp} °C")
            print(f"Max Temp   : {day.max_temp} °C")
            print("-" * 40)
            return

    print(f"No forecast available for {date}")



def main() -> None:
    file_path = "weather.json"
    forecast = get_forecast(file_path)

    date = "2025-12-26"
    print_forecast_for_day(forecast, date)


client = {'name': 'Satyam', 'Profession': 'Programmer', 'Salary': 100000}
with open('client.json' , 'w') as f:
    json.dump(client, f)

if __name__ == "__main__":
    main()
