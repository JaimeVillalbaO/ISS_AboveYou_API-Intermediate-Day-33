import requests 
from datetime import datetime, timezone
import smtplib
import time

response = requests.get('http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

data = response.json()

longitude = float(data['iss_position']['longitude'])
latitude = float(data['iss_position']['latitude'])
iss_position = (longitude, latitude)

my_lat = 10.394926
my_lng = -75.508030

time_now_utc = str(datetime.now(timezone.utc)).split()[1].split('+')[0]
time_now_utc_hour = time_now_utc.split(':')[0]
time_now_utc_minut = time_now_utc.split(':')[1]



parameters = {
    'lat': my_lat, 
    'lng' : my_lng,
    'formatted' : 0, #para colocarlo en formato 24h
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split('+')[0]
sunrise_hour = sunrise.split(':')[0]
sunset_minut = sunrise.split(':')[1]


sunset = data['results']['sunset'].split('T')[1].split('+')[0]
sunset_hour = sunset.split(':')[0]
sunset_minut = sunset.split(':')[1]

while True:
    time.sleep(60)
    if latitude <= (my_lat + 5) and latitude >= (my_lat -5) and longitude <= (my_lng + 5) and longitude >= (my_lng - 5): 
        if time_now_utc_hour >= sunset_hour  or time_now_utc_hour <= sunrise_hour:

            my_email = 'jaimevillalbaoyola@gmail.com'
            password = 'sjgwizpxcgmesaps'
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls() #make the conection secure
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, 
                                    to_addrs=my_email, 
                                    msg=f"Subject:ISS is above you\n\nThis email was send by python"
                                    )
            
