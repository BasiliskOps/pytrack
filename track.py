import phonenumbers 
from test import number
from phonenumbers import geocoder

num = phonenumbers.parse(number)

locate = geocoder.description_for_number(num, "en")
print(locate)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))