import time
import requests
import json
import datetime
import pause
from twilio.rest import Client
client = Client(TWILIO_API_ID, TWILIO_AUTH_TOK)


LATITUDE = 28.1447625
LONGITUDE = -82.38013
hour = datetime.datetime.now().time().hour
year = 2021
month = 7
day = 10
hour = 21
while True:
    print("waiting!!")
    pause.until(datetime.datetime(year, month, day, hour, 4))
    time.sleep(5)
    weather_data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                                params={
                                    'lat': LATITUDE,
                                    'lon': LONGITUDE,
                                    'appid': WEATHER_API_KEY,
                                    'exclude': 'current,minutely,hourly'
                                })
    message = client.messages \
        .create(
        body="IS THE KITCHEN CLEAN?!?!?!?",
        from_='+18312222233',
        to=AUSTIN_PHONE
    )

    print(message.sid)
    weather_data_dict = weather_data.json()
    with open('dog.json', mode='w') as data:
        data.write(json.dumps(weather_data_dict, indent=4))
    main_weather = weather_data_dict['daily'][0]['weather'][0]['main']
    print(main_weather)
    day += 1
