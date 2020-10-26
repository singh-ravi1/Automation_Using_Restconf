import requests
import urllib3

USER = 'cisco'
PASS = 'cisco'

url = "https://10.0.0.1/restconf/data/Cisco-IOS-XE-native:native/hostname"

payload = ""
headers = {
    'Accept': "application/yang-data+json",
    'Content-Type': "application/yang-data+json",
    'cache-control': "no-cache",
    }

print("Configuration Parameters:")

response = requests.request("GET",url, auth=HTTPBasicAuth(USER, PASS), data=payload,
                            headers=headers, verify=False)

print(response.text)

