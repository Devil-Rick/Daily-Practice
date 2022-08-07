import requests as req
from datetime import datetime
import smtplib as smt

MY_LONG = 87.527019
MY_LAT = 23.906927
TODAY = datetime.utcnow().hour
MY_MAIL = "saptarshidhibar424@gmail.com"
PASSWORD = "wxetfrpzzlqgvmxo"
ISS_LONG = 0
ISS_LAT = 0


def location():
    global ISS_LONG, ISS_LAT
    response_position = req.get(url="http://api.open-notify.org/iss-now.json")
    if response_position.status_code == 200:
        data_position = response_position.json()
        ISS_LONG = float(data_position['iss_position']["longitude"])
        ISS_LAT = float(data_position['iss_position']['latitude'])
    else:
        response_position.raise_for_status()

    if (MY_LONG - 5) <= ISS_LONG <= (MY_LONG + 5) and (MY_LAT - 5) <= ISS_LAT <= (ISS_LAT + 5):
        return True


def is_night():
    param = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response_suntime = req.get(url="https://api.sunrise-sunset.org/json", params=param, verify=False)
    response_suntime.raise_for_status()
    data_suntine = response_suntime.json()
    sunrise_hour = int(data_suntine['results']["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data_suntine['results']["sunset"].split("T")[1].split(":")[0])
    if sunset_hour < TODAY < sunrise_hour:
        return True


if location() and is_night():
    with smt.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # tls = Transfer Layer Security
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs="testing793@yahoo.com",
                            msg=f"Subject:'LOOK FOR SATELLITE'\n\nThe satellite is just above your head")
else:
    print("Not in LOCATION YET")
    print(f"Your Corr : {MY_LONG}, {MY_LAT}\nCurrent ISS Corr : {ISS_LONG}, {ISS_LAT}")
