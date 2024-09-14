from travel_update.utils.api_utils import load_data_for_type, InformationType, Locations

LOCATIONS_TO_GET_WEATHER_FOR = [Locations.OXFORD, Locations.BRISTOL]


def generate_weather_update(dates: list[str]):
    param_data_for_api = []

    for date in dates:
        for location in LOCATIONS_TO_GET_WEATHER_FOR:
            param_data_for_api.append((date, location))

    weather_data = []

    for date, location in param_data_for_api:
        params = {
            'q': location.value,
            'dt': date
        }
        data = load_data_for_type(InformationType.WEATHER, params)

        return ((date, location), data)
