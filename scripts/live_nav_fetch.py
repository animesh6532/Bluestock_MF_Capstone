import requests

scheme_code = 119551

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print(data["meta"]["scheme_name"])

    print(data["data"][0])

else:

    print("Unable to fetch NAV")