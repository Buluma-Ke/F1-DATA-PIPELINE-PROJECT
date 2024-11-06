from urllib.request import urlopen
import json

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
       pit_data_url, position_data_url, race_control_url, sessions_data_url, stints_data_url,
       team_radio_data_url, weather_data_url]

for url in urls:
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    print(data)