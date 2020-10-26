import requests
import urllib3

USER = 'cisco'
PASS = 'cisco'


url = "https://10.0.0.1/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=1/ip/address/primary"

payload = "{\"primary\": {\"address\": \"8.8.8.8\", \"mask\": \"255.255.255.0\"}}"
headers = {
    'Accept': "application/yang-data+json",
    'Content-Type': "application/yang-data+json",
    'cache-control': "no-cache",
    }


print("Configuration Parameters:")

response = requests.request("PATCH",url, auth=HTTPBasicAuth(USER, PASS), data=payload,
                            headers=headers, verify=False)

print(response.status_code)

