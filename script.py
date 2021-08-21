import requests
from datetime import datetime, timedelta
import time
import webbrowser

age = 23
district_code = 296
dateToSearch = '26-08-2021' 

def parse_data(response_json):
    centres = response_json["centers"]
    for center in centres:
        if center["fee_type"] == 'Free':
            sessions = center["sessions"]
            for session in sessions:
                if (session["min_age_limit"] <= age and session["available_capacity_dose2"] > 0) and session["vaccine"] == 'COVISHIELD':
                    return 0


while True:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + \
        str(district_code)+"&date="+str(dateToSearch)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    result = requests.get(URL, headers=header)
    if result.ok:
        response_json = result.json()
        if parse_data(response_json) == 0:
            webbrowser.open_new_tab('https://selfregistration.cowin.gov.in/')
            break
        else:
            time.sleep(3)
