import requests
import urllib3

USER = 'cisco'
PASS = 'cisco'


url = "https://10.0.0.1/restconf/data/Cisco-IOS-XE-native:native/hostname"

payload = "{\"hostname\": \"Demo-Router\"}"
headers = {
    'Accept': "application/yang-data+json",
    'Content-Type': "application/yang-data+json",
    'cache-control': "no-cache",
    }

response = requests.request("PUT",url, auth=HTTPBasicAuth(USER, PASS), data=payload,
                            headers=headers, verify=False)

print(response.status_code)
