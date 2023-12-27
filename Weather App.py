import requests
import json
import pyttsx3
engine = pyttsx3.init()
city = input("Enter the name of the city---->")

url = f"https://api.weatherapi.com/v1/current.json?key=9c972187fb28498ab62145557232111&q={city}"

r = requests.get(url)
# print(r.text)
wdict = json.loads(r.text)
print(wdict["current"]["temp_c"])

# engine.say(wdict["current"]["temp_c"]) 
# engine.runAndWait()





