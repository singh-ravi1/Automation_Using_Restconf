import json
import requests
import yaml
import argparse
from requests.auth import HTTPBasicAuth

def config_load():
	f_devices = open('/home/ravi/projects/restconf/devices.conf', 'r')
	devices = yaml.safe_load(f_devices)
	config = devices #To update
	return config

def get_ospf(device):
	respath = '/data/Cisco-IOS-XE-native:native/router'
	url = 'https://' + device['hostname'] + ':' + str(device['port']) + device['api_root'] + respath	
	auth = HTTPBasicAuth(device['username'], device['password'])
	headers = device['headers']
	resp = requests.get(url, auth=auth, headers=headers, verify=device['verify'])
	response = json.loads(resp.text)
	print(json.dumps(response, indent=4))	

def set_ospf(device):
	ospf_data = yaml.load(open('/home/ravi/projects/restconf/ospf.yml').read())
	ospf_obj = {
		"Cisco-IOS-XE-native:router": ospf_data
	}
	respath = '/data/Cisco-IOS-XE-native:native/router'
	url = 'https://' + device['hostname'] + ':' + str(device['port']) + device['api_root'] + respath
	auth = HTTPBasicAuth(device['username'], device['password'])
	headers = device['headers']
	# PATCH method is adding objects, PUT is overwriting
	# everything recursively under the specified resource.
	resp = requests.patch(url, auth=auth, headers=headers, data=json.dumps(ospf_obj), verify=device['verify'])
	print(resp.status_code)

def main():
	config = config_load()
	requests.packages.urllib3.disable_warnings()
	headers = {
		'Accept': 'application/yang-data+json',
		'Content-Type': 'application/yang-data+json'
	}
	for device in config['devices']:
		device['headers'] = headers
		set_ospf(device)
		get_ospf(device)


if __name__ == "__main__":
	main()
