import folium
import phonenumbers

from my_number import number
from phonenumbers import geocoder

userNumber = phonenumbers.parse(number)

userLocation = geocoder.description_for_number(userNumber, "en")

print(userLocation)
key = "ebdca0d4320744feaacceed7a8f0e709"
#get carrier
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
from folium import Map
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(userLocation)
results = geocoder.geocode(query)
print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
the_location = (lat,lng)
print(the_location)\
    
myMap = folium.Map(the_location, zoom_start = 9)
folium.Marker([lat,lng], popup= userLocation).add_to(myMap)

#save in html

myMap.save("myLocation.html")

