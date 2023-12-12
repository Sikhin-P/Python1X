import json

import requests
import AuthToken


def test_put_request():
    booking_id = '1'
    url = 'https://restful-booker.herokuapp.com/booking/' + booking_id
    cookie = 'token=' + AuthToken.generateToken()
    print(url)
    print(cookie)
    headers= {"Content-Type": "application/json",
              'Cookie': cookie}
    print(headers)
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=url, headers=headers, data=json.dumps(payload))
    assert response.status_code == 200
