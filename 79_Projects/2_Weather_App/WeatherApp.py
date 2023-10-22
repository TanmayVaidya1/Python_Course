import requests
import json
import os

city = input("Enter the name of the city:- \n")
url = f"https://api.weatherapi.com/v1/current.json?key=5d05989e71bb4252821122147231910&q={city}"

r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)
temp = wdic["current"]["temp_c"]

command=f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('The Current Weather in {city} is {temp} Degrees');"
os.system(command)


