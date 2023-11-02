# Convert to Dict JSON Response and Print and Booking ID AND checkin and Checkout Data
import json

json_response = '''{

"bookingid": 2384,

"booking": {

"firstname": "PRAMOD",

"lastname": "Dutta",

"totalprice": 432,

"depositpaid": False,

"bookingdates": {

"checkin": "2022-01-01",

"checkout": "2022-01-01"

},

"additionalneeds": "Lunch"

}

}'''
# In the above example the value False is not in json format, hence replacing it to false
json_response = json_response.replace('False', 'false')

data = json.loads(json_response)
print(f'Booking ID is : {data.get("bookingid")}')
print(f'Checkin date is : {data.get("booking").get("bookingdates").get("checkin")}')
print(f'Checkout date is : {data.get("booking").get("bookingdates").get("checkout")}')
