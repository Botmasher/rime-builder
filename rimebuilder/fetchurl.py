import urllib.request, json

def fetchJSON(path):
	with urllib.request.urlopen(path) as url:
		data = json.loads(url.read().decode())
		url.close()
		return data

def fetchHTML(path):
	with urllib.request.urlopen(path) as url:
		data = url.read().decode()
		url.close()
		return data
