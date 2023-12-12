import json
import requests
import pytest


@pytest.mark.positive
def test_create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Aron",
        "lastname": "Ramsey",
        "totalprice": 199,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(json_payload))
    assert response.status_code == 200
