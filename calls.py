import requests
import json
import pycurl
import certifi
from io import BytesIO

def chuck_norris():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
            "accept": "application/json",
            "X-RapidAPI-Key": "8fbc873fd8msh5d43e6022f22f64p15f17ejsnbb456384ba17",
            "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }


    response = requests.request("GET", url, headers=headers)
    y = json.loads(response.text)
    return y["value"]

def num_fact():
    url = "https://numbersapi.p.rapidapi.com/1492/year"

    querystring = {"json":"true","fragment":"true"}

    headers = {
            "X-RapidAPI-Key": "8fbc873fd8msh5d43e6022f22f64p15f17ejsnbb456384ba17",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    y = json.loads(response.text)
    print(y["text"], ":", y["number"])

def weather():
    url = "https://dark-sky.p.rapidapi.com/30.628956,96.328281"

    querystring = {"lang":"en","units":"auto"}

    headers = {
            "X-RapidAPI-Key": "8fbc873fd8msh5d43e6022f22f64p15f17ejsnbb456384ba17",
            "X-RapidAPI-Host": "dark-sky.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    y = json.loads(response.text)
    print(y["latitude"], y["daily"]["summary"])

def daily_quote():
    url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
    querystring = {"count":"1","cat":"famous"}
    headers = {
            "X-RapidAPI-Key": "8fbc873fd8msh5d43e6022f22f64p15f17ejsnbb456384ba17",
            "X-RapidAPI-Host": "andruxnet-random-famous-quotes.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    y = json.loads(response.text)
    print(y[0]["quote"], ":", y[0]["author"])

print(chuck_norris())
num_fact()
# weather()
daily_quote()


