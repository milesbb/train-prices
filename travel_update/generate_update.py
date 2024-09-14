from dotenv import load_dotenv

from travel_update.utils.date_utils import get_next_dates_in_office
from travel_update.api.weather_api import generate_weather_update


def generate_travel_update():
    print('Generating Travel Update...')
    load_dotenv()
    

    next_dates_in_office = get_next_dates_in_office()

    weather_updates = generate_weather_update(next_dates_in_office)

    print(weather_updates)
    print('Finished generating Travel Update.')

generate_travel_update()
