import json
import requests


def generateToken():
    tokenURL = "https://restful-booker.herokuapp.com/auth"

    contentType = {"Content-Type": "application/json"}

    jsonPayload = {

        'username': 'admin',

        'password': 'password123'

    }

    response = requests.post(url=tokenURL, headers=contentType, data=json.dumps(jsonPayload))

    data = response.json()
    print(response.status_code)

    token = data['token']

    return token


print(generateToken())
