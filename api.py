from urllib.request import urlopen
from requests.exceptions import HTTPError
import json
import pandas as pd

#features  ['car_data', ]

car_data_url =  'https://api.openf1.org/v1/car_data'
driver_data_url = 'https://api.openf1.org/v1/drivers'
intervals_data_url= 'https://api.openf1.org/v1/intervals'
laps_data_url = 'https://api.openf1.org/v1/laps'
location_data_url = 'https://api.openf1.org/v1/location'
meetings_data_url = 'https://api.openf1.org/v1/meetings'
pit_data_url = 'https://api.openf1.org/v1/pit'
position_data_url = 'https://api.openf1.org/v1/position'
race_control_url = 'https://api.openf1.org/v1/race_control'
sessions_data_url = 'https://api.openf1.org/v1/sessions'
stints_data_url = 'https://api.openf1.org/v1/stints'
team_radio_data_url = 'https://api.openf1.org/v1/team_radio'
weather_data_url = 'https://api.openf1.org/v1/weather'

urls = [car_data_url, driver_data_url, intervals_data_url, laps_data_url, location_data_url, 
        meetings_data_url, pit_data_url, position_data_url, race_control_url, sessions_data_url, 
        position_data_url, race_control_url, sessions_data_url, stints_data_url,
        team_radio_data_url, weather_data_url]


for url in urls:
    try:
        response = urlopen(url)
        print(f'File {url} response successful')
        data = json.loads(response.read().decode('utf-8'))

        # Create DataFrame and print memory usage details
        df = pd.DataFrame(data)
        print(f"DataFrame shape: {df.shape}")
        print(f"Memory usage: {df.memory_usage(deep=True).sum() / (1024 ** 2):.2f} MB") # memory size in mbs

    except HTTPError as http_err:
        if http_err.code == 500:
            print(f"HTTP 500 Error for {url}. Skipping this URL.")
        else:
            print(f"HTTP error {http_err.code} for {url}: {http_err}")
        # Continue to the next URL in the list
        continue
    except Exception as err:
        print(f"Other error occurred for {url}: {err}")
        continue
