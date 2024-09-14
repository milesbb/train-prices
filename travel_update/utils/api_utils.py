from requests import get, RequestException
import os
from enum import Enum

class InformationType(Enum):
    WEATHER = 'WEATHER'
    TRAINS = 'TRAINS'


class Locations(Enum):
    BRISTOL = 'Bristol'
    OXFORD = 'Oxford'


BASE_URL = {
    InformationType.WEATHER: 'http://api.weatherapi.com/v1/future.json',
    InformationType.TRAINS: ''
}


def load_data_for_type(information_type: InformationType, params: dict) -> dict:
    api_key = load_api_key(information_type)

    params['key'] = api_key

    data = get_request(BASE_URL[information_type], params)

    return data


def get_request(url: str, params: dict[str]):
    try:
        target_url = url

        request_parameters = []
        for key, value in params.items():
            request_parameters.append(f'{key}={value}')

        target_url = target_url + '?' + '&'.join(request_parameters)

        print(f'Target url: {target_url}')

        response = get(target_url)

        if response.status_code == 200:
            print(f'Successfull request to {url}')
            print(response.json())
        else:
            print(f'Request errored with {response.status_code} - {response.reason}:')
    except RequestException as err:load_dotenv()


def load_api_key(information_type: InformationType) -> str:
    

    api_key = os.getenv(f'{information_type.value}_API_KEY')

    if api_key is None or len(api_key) == 0:
        raise ValueError(f'Could not find api key for {information_type.value} api service. Please check your .env file.')
    
    return api_key
