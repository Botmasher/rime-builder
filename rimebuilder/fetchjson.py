import urllib.request, json

def fetch(path):
	with urllib.request.urlopen(path) as url:
		data = json.loads(url.read().decode())
		url.close()
		return data
